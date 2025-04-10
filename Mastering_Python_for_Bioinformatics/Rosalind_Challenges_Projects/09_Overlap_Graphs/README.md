# Project 9: Overlap Graphs

## Description

This Python project aims to create a graph using sequences, tackling the Rosalind challenge ["Overlap Graphs"](https://rosalind.info/problems/grph/). The program takes a FASTA-formatted file with sequences as input and an optional overlap size as an argument. The goal of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `graph.py` that accepts a FASTA file as a positional argument and an optional overlap size. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./graph.py -h
usage: graph.py [-h] [-k size] [-d] FILE

Graph through sequences

positional arguments:
  FILE                  FASTA file

optional arguments:
  -h, --help            show this help message and exit
  -k size, --overlap_size size
                        Size of overlap (default: 3)
  -d, --debug           Enable debug mode
```

---

## Program Inputs

The file `graph.py` accepts the following inputs:

1. **FASTA file with sequences (positional argument)**:
```sh
$ cat tests/inputs/1.fa
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
```

2. **Overlap size (optional argument)**:
```sh
$ ./graph.py -k 3 tests/inputs/input.fasta
```

---

## Program Output

The program will print the edges of the graph representing overlaps between the sequences:

```sh
$ ./graph.py -k 3 tests/inputs/input.fasta
seq1 seq2
seq3 seq4
```

---

## Usage Example

To run the program and create a graph using sequences with an overlap size of 3:

```sh
$ ./grph.py tests/inputs/1.fa
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
```

---
