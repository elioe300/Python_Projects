# Project 14: Open Reading Frames

## Descripción

Este proyecto de Python tiene como propósito identificar marcos de lectura abiertos (ORFs, por sus siglas en inglés) en secuencias de ADN, superando el desafío de Rosalind ["Open Reading Frames"](https://rosalind.info/problems/orf/). El programa toma como entrada un archivo en formato FASTA con secuencias de ADN y encuentra todos los ORFs en las cadenas de ARN y sus complementos reversos. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `orf.py` que aceptará un archivo FASTA como argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./orf.py -h
usage: open_reading_frames.py [-h] FILE

Open Reading Frames

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `orf.py` acepta como input:

1. **Archivo FASTA con secuencias de ADN (argumento posicional)**

```sh
$ cat tests/inputs/1.fa
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTC\
TTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

## Salida del Programa

El programa imprimirá todos los marcos de lectura abiertos (ORFs) encontrados en las secuencias del archivo FASTA:

```sh
$ ./orf.py tests/inputs/input.fasta
MKTIIALSYIFCLVFA
MGSQGGISAG
```

## Ejemplo de Uso

Para ejecutar el programa y localizar marcos de lectura abiertos en un archivo FASTA:

```sh
$ ./orf.py tests/inputs/1.fa
M
MGMTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
MTPRLGLESLLE
```

---
