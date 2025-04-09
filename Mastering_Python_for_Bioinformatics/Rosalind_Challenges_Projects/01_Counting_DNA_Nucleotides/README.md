# Project 1: Tetranucleotide Frequency

## Description

This Python project tackles the Rosalind challenge titled ["Counting DNA Nucleotides"](https://rosalind.info/problems/dna/), where the program processes a DNA sequence and counts the occurrences of A, C, G, and T. Additionally, it follows the guidelines provided by the book *Mastering Python for Bioinformatics*, which are as follows:

---

## Instructions

Create a program named `dna.py` that accepts a DNA sequence as a single positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./dna.py -h
usage: dna.py [-h] DNA

Tetranucleotide frequency

positional arguments:
  DNA     Input DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `dna.py` accepts the following inputs:

1. **DNA sequence either from a file or directly from the command line, regardless of uppercase or lowercase characters**
```sh
File containing DNA
$ cat tests/inputs/input1.txt
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# --------------------------------------------------
DNA sequence directly from the command line
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

---

## Program Output

The program should print the frequencies of the bases A, C, G, and T:

```sh
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A counts: 20 | C counts: 12 | G counts: 17 | T counts: 21
```

---

