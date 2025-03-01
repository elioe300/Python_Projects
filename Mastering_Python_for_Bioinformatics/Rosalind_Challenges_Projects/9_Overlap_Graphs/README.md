# Project 9: Overlap Graphs

## Descripción

Este proyecto de Python tiene como propósito crear un grafo a través de secuencias, superando el desafío de Rosalind ["Overlap Graphs"](https://rosalind.info/problems/grph/). El programa toma como entrada un archivo en formato FASTA con secuencias y un tamaño de solapamiento como argumento opcional. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `graph.py` que aceptará un archivo FASTA como argumento posicional y un tamaño de solapamiento como argumento opcional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./graph.py -h
usage: graph_through_sequences.py [-h] [-k size] [-d] FILE

Graph through sequences

positional arguments:
  FILE                  FASTA file

optional arguments:
  -h, --help            show this help message and exit
  -k size, --overlap_size size
                        Size of overlap (default: 3)
  -d, --debug           Enable debug mode
```

## Entradas del Programa

El archivo `graph.py` acepta como input:

1. **Archivo FASTA con secuencias (argumento posicional)**
2. **Tamaño de solapamiento (argumento opcional)**

```sh
$ ./graph.py -k 3 tests/inputs/input.fasta
```

## Salida del Programa

El programa imprimirá las aristas del grafo representando los solapamientos entre las secuencias:

```sh
$ ./graph.py -k 3 tests/inputs/input.fasta
seq1 seq2
seq3 seq4
```

## Ejemplo de Uso

Para ejecutar el programa y crear un grafo a través de secuencias con un tamaño de solapamiento de 3:

```sh
$ ./grph.py tests/inputs/1.fa
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
seq1 seq2
seq3 seq4
```

---

Con esta descripción detallada y los comentarios del código, cualquier persona que consulte tu proyecto podrá entender fácilmente cómo utilizar el programa y cómo funciona.
