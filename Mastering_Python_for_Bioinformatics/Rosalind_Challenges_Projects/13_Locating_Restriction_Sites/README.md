# Project 13: Locating Restriction Sites

## Description

This Python project aims to identify restriction sites in DNA sequences, addressing the Rosalind challenge ["Locating Restriction Sites"](https://rosalind.info/problems/revp/). The program takes a FASTA-formatted DNA sequence file as input and finds all palindromic sequences within a specified size range. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `revp.py` that accepts a FASTA file as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./revp.py -h
usage: revp.py [-h] FILE

Locating Restriction Sites

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `revp.py` accepts the following input:

1. **FASTA file with DNA sequences (positional argument)**

```sh
$ cat tests/inputs/1.fa
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
```

---

## Program Output

The program will print the positions and lengths of palindromic sequences found in the FASTA file:

```sh
$ ./revp.py tests/inputs/input.fasta
1 4
2 6
3 8
```

---

## Usage Example

To run the program and locate restriction sites in a FASTA file:

```sh
$ ./revp.py tests/inputs/1.fa
5 4
7 4
17 4
18 4
21 4
4 6
6 6
20 6
```

---
