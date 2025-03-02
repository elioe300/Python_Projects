# Project 10: Finding a Shared Motif

## Descripción

Este proyecto de Python tiene como propósito encontrar la subcadena común más larga entre varias secuencias, superando el desafío de Rosalind ["Finding a Shared Motif"](https://rosalind.info/problems/lcsm/). El programa toma como entrada un archivo en formato FASTA con secuencias y encuentra la subcadena más larga que se encuentra en todas las secuencias. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `lcsm.py` que aceptará un archivo FASTA como argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./lcsm.py -h
usage: lcsm.py [-h] FILE

Longest Common Substring

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `lcsm.py` acepta como input:

1. **Archivo FASTA con secuencias (argumento posicional)**

```sh
$ cat tests/inputs/1.fa
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
```

## Salida del Programa

El programa imprimirá la subcadena común más larga encontrada en todas las secuencias del archivo FASTA:

```sh
$ ./lcsm.py tests/inputs/input.fasta
AGGTAC
```

## Ejemplo de Uso

Para ejecutar el programa y encontrar la subcadena común más larga entre varias secuencias en un archivo FASTA:

```sh
$ ./lcsm.py tests/inputs/1.fa
# En este caso, el programa puede imprimir estas cadenas, puesto que son las más largas: CA ó AC ó TA
```

---
