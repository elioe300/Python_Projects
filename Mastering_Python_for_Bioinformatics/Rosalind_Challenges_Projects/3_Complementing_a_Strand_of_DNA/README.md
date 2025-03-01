# Project 3: Complementing a Strand of DNA

## Descripción

Este proyecto de Python tiene como propósito imprimir la cadena complementaria reversa de una secuencia de ADN, superando el desafío de Rosalind ["Complementing a Strand of DNA"](https://rosalind.info/problems/revc/). El programa toma una secuencia de ADN o un archivo que contiene la secuencia de ADN como entrada y genera la secuencia complementaria reversa. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `reverse_complement.py` que aceptará una secuencia de ADN o el nombre de un archivo que contiene la secuencia de ADN como argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./revc.py -h
usage: reverse_complement.py [-h] DNA

Print the reverse complement of DNA

positional arguments:
  DNA     Input DNA sequence or file

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `reverse_complement.py` acepta como input:

1. **Secuencia de ADN directamente desde la línea de comandos o desde un archivo (argumento posicional)**
```sh
Archivo que contiene ADN
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
# --------------------------------------------------
Secuencia de ADN directamente desde la línea de comandos
$ ./revc.py AAAACCCGGT
ACCGGGTTTT
```

## Salida del Programa

El programa imprimirá la cadena complementaria reversa de la secuencia de ADN proporcionada.

```sh
$ ./revc.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

Para ejecutar el programa y obtener la cadena complementaria reversa de una secuencia de ADN desde un archivo:

```sh
$ ./revc.py sequence.txt
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

## Ejemplo de Uso

Para ejecutar el programa y obtener la cadena complementaria reversa de una secuencia de ADN proporcionada directamente en la línea de comandos o desde un archivo de entrada:

```sh
$ ./revc.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT

$ ./revc.py sequence.txt
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

Esto imprimirá la secuencia complementaria reversa correspondiente a la secuencia de ADN proporcionada.

---
