# Project 1. Tetranucleotide Frequency

# Descripción

Este proyecto de Python supera el desafío Rosalind titulado ["Counting DNA Nucleotides"](https://rosalind.info/problems/dna/), donde el programa tomará una secuencia de ADN y contará cuántas A, C, G y T se encuentran. Además, sigue las instrucciones que nos invita a seguir el libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `dna.py` que aceptará una secuencia de ADN como un único argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./dna.py -h
usage: dna.py [-h] DNA

Tetranucleotide frequency

positional arguments:
  DNA     Input DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```
### Entradas del Programa
El archivo `dna.py` acepta como input:

1. **Secuencia de ADN desde un archivo**
2. **Secuencia de ADN directamente desde la línea de comandos independientemente de si están en mayúscula o minusculas**

### Salida del Programa

El programa debe imprimir las frecuencias de las bases A, C, G y T:

```sh
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
20 12 17 21
```
