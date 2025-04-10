# Project 14: Open Reading Frames

## Description

This Python project aims to identify Open Reading Frames (ORFs) in DNA sequences, addressing the Rosalind challenge ["Open Reading Frames"](https://rosalind.info/problems/orf/). The program takes a FASTA-formatted DNA sequence file as input and finds all ORFs in RNA strands and their reverse complements. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `orf.py` that accepts a FASTA file as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./orf.py -h
usage: orf.py [-h] FILE

Open Reading Frames

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `orf.py` accepts the following input:

1. **FASTA file with DNA sequences (positional argument)**

```sh
$ cat tests/inputs/1.fa
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTC\
TTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

---

## Program Output

The program will print all Open Reading Frames (ORFs) found in the DNA sequences of the FASTA file:

```sh
$ ./orf.py tests/inputs/input.fasta
MKTIIALSYIFCLVFA
MGSQGGISAG
```

---

## Usage Example

To run the program and locate Open Reading Frames in a FASTA file:

```sh
$ ./orf.py tests/inputs/1.fa
M
MGMTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
MTPRLGLESLLE
```

---

