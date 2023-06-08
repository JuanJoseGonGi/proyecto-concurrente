# Dotplot Genomic Sequences

Este proyecto genera un dotplot para dos secuencias genómicas utilizando tres métodos diferentes: secuencial, multiprocessing y Message Passing Interface (MPI). Los dotplots son una forma útil de visualizar las similitudes entre dos secuencias genómicas, lo que puede ayudar a identificar regiones de similitud y posibles homologías.

## Prerrequisitos

Este proyecto utiliza Python 3.7 o superior y las siguientes bibliotecas:

Numpy
Matplotlib
Biopython
MPI for Python (mpi4py)
OpenCV (cv2)
Para instalar estas dependencias, puedes utilizar el administrador de paquetes de Python, pip:

```shell
pip install numpy matplotlib biopython mpi4py opencv-python-headless
```

## Cómo ejecutar el proyecto

Puedes ejecutar cada uno de los tres métodos (secuencial, multiprocessing y MPI) modificando y ejecutando el script de Python correspondiente (sequential_dotplot.py, multiprocessing_dotplot.py y mpi_dotplot.py).

Cada script toma dos argumentos de la línea de comando: las rutas a los dos archivos FASTA que contienen las secuencias genómicas que deseas comparar. Para el script de MPI, también necesitas especificar el número de procesos que quieres utilizar utilizando el comando mpirun.

Puedes ejecutar cada uno de los tres métodos (secuencial, multiprocessing y MPI) modificando y ejecutando el script de Python correspondiente (sequential_dotplot.py, `multiprocessing_dotplot.py` y `mpi_dotplot.py`).

Cada script toma dos argumentos de la línea de comando: las rutas a los dos archivos FASTA que contienen las secuencias genómicas que deseas comparar. Para el script de MPI, también necesitas especificar el número de procesos que quieres utilizar utilizando el comando mpirun.

Aquí hay un ejemplo de cómo podrías ejecutar el script de dotplot secuencial:

```shell
python3 sequential_dotplot.py --file1=path/to/file1.fasta --file2=path/to/file2.fasta
```

Y aquí hay un ejemplo de cómo podrías ejecutar el script de dotplot MPI con 4 procesos:

```shell
mpirun -n 4 python3 mpi_dotplot.py --file1=path/to/file1.fasta --file2=path/to/file2.fasta
```

## Interpretación de los resultados

Después de ejecutar uno de los scripts de dotplot, se generará una imagen de un dotplot. Los puntos en el dotplot representan regiones de similitud entre las dos secuencias genómicas. Un grupo de puntos que forman una línea diagonal puede representar una región de similitud que se conserva en la misma ubicación relativa en ambas secuencias. Un grupo de puntos que no forman una línea diagonal puede representar una región de similitud que ha sido reubicada en una de las secuencias.

## Medición del rendimiento

El script también imprimirá el tiempo que llevó generar el dotplot. Esto te permite comparar el rendimiento de los tres métodos diferentes. Ten en cuenta que el tiempo de ejecución puede variar dependiendo del hardware y software específicos de tu sistema.

Esperamos que encuentres útil este proyecto y que te ayude en tu análisis de secuencias genómicas. No dudes en contactarnos si tienes alguna pregunta o comentario.
