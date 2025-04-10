# Project 3: Complementing a Strand of DNA

## Description

This Python project aims to print the reverse complement of a DNA sequence, addressing the Rosalind challenge ["Complementing a Strand of DNA"](https://rosalind.info/problems/revc/). The program takes either a DNA sequence or a file containing the DNA sequence as input and generates the reverse complement sequence. The objective of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as detailed below:

---

## Instructions

Create a program called `revc.py` that accepts either a DNA sequence or the name of a file containing the DNA sequence as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./revc.py -h
usage: revc.py [-h] DNA

Print the reverse complement of DNA

positional arguments:
  DNA     Input DNA sequence or file

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `revc.py` accepts the following inputs:

1. **DNA sequence directly from the command line or from a file (positional argument)**
```sh
File containing DNA
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
# --------------------------------------------------
DNA sequence directly from the command line
$ ./revc.py AAAACCCGGT
ACCGGGTTTT
```

---

## Program Output

The program will print the reverse complement of the provided DNA sequence.

```sh
$ ./revc.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

To execute the program and obtain the reverse complement of a DNA sequence from a file:

```sh
$ ./revc.py sequence.txt
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

---

## Usage Example

To execute the program and obtain the reverse complement of a DNA sequence provided directly on the command line or from an input file:

```sh
$ ./revc.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
# ------------------------------------------------------------------------------------
$ ./revc.py sequence.txt
GCTATCAGACACTCTTTTTTAATCCACACAGAGACATATTGCCCGTTGCAGTCAGAATGAAAAGCT
```

This will print the reverse complement sequence corresponding to the provided DNA sequence.

---
