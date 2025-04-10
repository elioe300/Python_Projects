# Project 6: Compute the Hamming Distance Between Two Strings

## Description

This Python project calculates the Hamming distance between two DNA sequences, addressing the Rosalind challenge ["Compute the Hamming Distance Between Two Strings"](https://rosalind.info/problems/ba1g/). The program takes two positional arguments, which are two DNA sequence strings, and prints the Hamming distance between them. The objective is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `hamm.py` that accepts two DNA sequences as positional arguments. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./hamm.py -h
usage: hamm.py [-h] str str

Calculate Hamming distance

positional arguments:
  str         First DNA sequence
  str         Second DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `hamm.py` accepts the following inputs:

1. **Two DNA sequences (positional arguments)**
```sh
$ cat tests/inputs/1.txt
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```

---

## Program Output

The program will print the Hamming distance between the two provided DNA sequences:

```sh
$ ./hamm.py GAGCCTACTAACGGGAT CATCGTAATGACGGCCT
7
```

---

## Usage Example

To execute the program and calculate the Hamming distance between two DNA sequences:

```sh
$ ./hamm.py GAGCCTACTAACGGGAT CATCGTAATGACGGCCT
7
```

---
