from mpi4py import MPI
import numpy as np
import pickle
import argparse
from Bio import SeqIO


def sequence_str_to_uint8(sequence):
    return np.frombuffer(sequence.encode(), dtype=np.uint8)


def merge_sequences_from_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences = np.append(sequences, record.seq)
    return "".join(sequences)


e_coli_sequence = sequence_str_to_uint8(
    merge_sequences_from_fasta("archivosParaDotplot/E_coli.fna")
)
salmonella_sequence = sequence_str_to_uint8(
    merge_sequences_from_fasta("archivosParaDotplot/Salmonella.fna")
)


def mpi_dotplot_worker(rank, size, seq1, seq2, block_size, n):
    # This function will be run by each worker process
    matches_blocks = []
    block_indices = []
    for i in range(rank, n, size * block_size):
        block_start = i
        block_end = min(i + block_size, n)
        matches = np.equal.outer(seq1[block_start:block_end], seq2)
        matches_blocks.append(np.where(matches, 1, 0))
        block_indices.append(block_start)
    return matches_blocks, block_indices


def mpi_dotplot(seq1, seq2, block_size=1000):
    n = len(seq1)
    m = len(seq2)

    # Initialize MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()  # Total number of processes
    rank = comm.Get_rank()  # Rank of this process

    results, indices = mpi_dotplot_worker(rank, size, seq1, seq2, block_size, n)
    all_results = comm.gather(results, root=0)
    all_indices = comm.gather(indices, root=0)

    if rank == 0:
        # Only the root process creates the dotplot
        dotplot = np.zeros((n, m), dtype=np.uint8)
        for res, ind in zip(all_results, all_indices):
            for block, start in zip(res, ind):
                dotplot[start : start + block.shape[0], :] = block

        # Save the dotplot to a pickle file
        with open("dotplot.pkl", "wb") as f:
            pickle.dump(dotplot, f)

        return dotplot


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Perform a dotplot analysis on two DNA sequences."
    )
    parser.add_argument(
        "--file1", type=str, required=True, help="Path to the first fasta file."
    )
    parser.add_argument(
        "--file2", type=str, required=True, help="Path to the second fasta file."
    )
    parser.add_argument(
        "--test-size",
        type=int,
        default=15000,
        help="Size of the sequence subset for testing.",
    )
    args = parser.parse_args()

    # Load sequences from files
    seq1 = sequence_str_to_uint8(merge_sequences_from_fasta(args.file1))
    seq2 = sequence_str_to_uint8(merge_sequences_from_fasta(args.file2))

    # Perform dotplot analysis
    dotplot = mpi_dotplot(seq1[: args.test_size], seq2[: args.test_size])
