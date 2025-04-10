# Project 10: Finding a Shared Motif

## Description

This Python project aims to find the longest common substring among multiple sequences, addressing the Rosalind challenge ["Finding a Shared Motif"](https://rosalind.info/problems/lcsm/). The program takes a FASTA-formatted file with sequences as input and identifies the longest substring shared by all sequences. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `lcsm.py` that accepts a FASTA file as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./lcsm.py -h
usage: lcsm.py [-h] FILE

Longest Common Substring

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `lcsm.py` accepts the following input:

1. **FASTA file with sequences (positional argument)**

```sh
$ cat tests/inputs/1.fa
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
```

---

## Program Output

The program will print the longest common substring found across all sequences in the FASTA file:

```sh
$ ./lcsm.py tests/inputs/input.fasta
AGGTAC
```

---

## Usage Example

To run the program and find the longest common substring among multiple sequences in a FASTA file:

```sh
$ ./lcsm.py tests/inputs/1.fa
# In this case, the program may output any of the longest substrings found, such as: CA, AC, or TA
```

---

