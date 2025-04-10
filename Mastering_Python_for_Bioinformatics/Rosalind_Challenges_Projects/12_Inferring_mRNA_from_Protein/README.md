# Project 12: Inferring mRNA from Protein

## Description

This Python project aims to infer the mRNA sequence from a protein sequence, addressing the Rosalind challenge ["Inferring mRNA from Protein"](https://rosalind.info/problems/mrna/). The program takes a protein sequence as input and calculates the number of possible mRNA sequences that could have encoded it. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as detailed below:

---

## Instructions

Create a Python program called `mrna.py` that accepts a protein sequence as a positional argument or a filename, along with an optional "modulo" argument with a default value of 1,000,000. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./mrna.py -h
usage: mrna.py [-h] [-m int] protein

Infer mRNA from Protein

positional arguments:
  protein          Input protein or file

optional arguments:
  -h, --help       show this help message and exit
  -m int, --modulo int
                   Modulo value (default: 1000000)
```

---

## Program Inputs

The file `mrna.py` accepts the following inputs:

1. **Protein sequence or a file containing the protein sequence (positional argument)**:
```sh
$ cat 1.txt
MSVHDQCHHQLSFSMMECLLPRSEHTRMEWKTWDVVVWMPRRWPWGPSRDKTCIYAHTCMQGKDPIFHRIIP
```

2. **Optional modulo value (optional argument)**

---

## Program Output

The program will print the number of possible mRNA sequences that could have coded for the provided protein sequence, using the optional modulo value:

```sh
$ ./mrna.py -m 1000000 MYPROTEIN
196608
```

---

## Usage Example

To run the program and calculate the number of possible mRNA sequences:

```sh
$ ./mrna.py MA
12

$ ./mrna.py -m 1000000 tests/inputs/1.txt
448832
```

---
