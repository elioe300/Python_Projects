# Project 8: Finding a Motif in DNA

## Descripción

Este proyecto de Python tiene como propósito encontrar subsecuencias dentro de una secuencia dada, superando el desafío de Rosalind ["Finding a Motif in DNA"](https://rosalind.info/problems/subs/). El programa toma como entrada una secuencia y una subsecuencia, y encuentra todas las posiciones en las que la subsecuencia aparece dentro de la secuencia principal. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `subs.py` que aceptará una secuencia y una subsecuencia como argumentos posicionales. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./subs.py -h
usage: find_subsequences.py [-h] seq subseq

Find subsequences

positional arguments:
  seq         Sequence
  subseq      Sub-sequence

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `subs.py` acepta como input:

1. **Secuencia principal (argumento posicional)**
2. **Subsecuencia (argumento posicional)**

```sh
$ ./subs.py GATATATGCATATACTT ATAT
```

## Salida del Programa

El programa imprimirá las posiciones en las que se encuentra la subsecuencia dentro de la secuencia principal:

```sh
$ ./find_subsequences.py GATATATGCATATACTT ATAT
2 4 10
```

## Ejemplo de Uso

Para ejecutar el programa y encontrar todas las posiciones en las que aparece una subsecuencia dentro de una secuencia principal:

```sh
$ ./find_subsequences.py TCGAAACCAGAGATCACCTGAAAACCAGCCAGAAACCAGTCAAACCAGGGCGTAAACCAGTCAAAACCAGAAACCAGCGTAAACCAGAAACCAGTTTAAAACCAGAAACCAGATAAACCAGGTCAGAAACCAGCATCAAACCAGAAACCAGAAACCAGCCCTTAAACCAGAAACCAGAAAACCAGCGCAAAACCAGTGAAAACCAGGAAACCAGAAACCAGCTCAAAACCAGAAAAACCAGAAACCAGAAACCAGTAAAACCAGCCGTAAACCAGCTAAACCAGAAAACCAGCTACAAACCAGAAACCAGCAAACCAGCAATGAAAACCAGACCAGAAACCAGCTAAAAACCAGGAGAGAAACCAGTAAACCAGAGCTTAAACCAGAAAACCAGAAACCAGTCAAACCAGAAAACCAGCAAACCAGATTGAAAACCAGAAACCAGCAAAACCAGGAAACCAGTAGATTGAAACCAGAAACCAGACTTATACAAACCAGTACATGGGCTCTAACAAACCAGCCTATGGCTGTGTGGATAAACCAGAAACCAGAATAAACCAGGGGCCAAACCAGGCGTAAACCAGGCTGAAACCAGAAACCAGAAACCAGCAAAACCAGCCGTTTTGCTCGAAACCAGGAAAACCAGAAACCAGCCAATAAACCAGAAACCAGGGAAACCAGGGCAAAACCAGTAAACCAGGCATAAACCAGCCCCGAAAAACCAGTTCTTAAACCAGGATCGATAAAACCAGTATAAAACCAGGAGTAAACCAGGAAACCAGGGACAAACCAGCTAAACCAGGTGAAACCAGGAAACCAGAAACCAGACTTAAACCAGGAAACCAGGTATGAAACCAGTAAAAACCAGGGAAAACCAGAAACCAGAAACCAGCCTAAACCAGTAAACCAGAAACCAGGAAACCAGAGAAACCAG AAACCAGAA
64 81 99 138 145 164 171 208 226 235 242 278 297 380 388 404 432 470 538 545 589 596 640 659 814 872 879 904
```

---
