# Project 8: Finding a Motif in DNA

## Description

This Python project aims to find subsequences within a given sequence, addressing the Rosalind challenge ["Finding a Motif in DNA"](https://rosalind.info/problems/subs/). The program takes a sequence and a subsequence as input and finds all the positions where the subsequence appears in the main sequence. The goal is to follow the instructions from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `subs.py` that accepts a sequence and a subsequence as positional arguments. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./subs.py -h
usage: subs.py [-h] seq subseq

Find subsequences

positional arguments:
  seq         Sequence
  subseq      Sub-sequence

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `subs.py` accepts the following inputs:

1. **Main sequence (positional argument)**
2. **Subsequence (positional argument)**

```sh
$ ./subs.py GATATATGCATATACTT ATAT
```

---

## Program Output

The program will print the positions where the subsequence is found within the main sequence:

```sh
$ ./subs.py GATATATGCATATACTT ATAT
2 4 10
```

---

## Usage Example

To run the program and find all positions where a subsequence appears in a main sequence:

```sh
$ ./subs.py TCGAAACCAGAGATCACCTGAAAACCAGCCAGAAACCAGTCAAACCAGGGCGTAAACCAGTCAAAACCAGAAACCAGCGTAAACCAGAAACCAGTTTAAAACCAGAAACCAGATAAACCAGGTCAGAAACCAGCATCAAACCAGAAACCAGAAACCAGCCCTTAAACCAGAAACCAGAAAACCAGCGCAAAACCAGTGAAAACCAGGAAACCAGAAACCAGCTCAAAACCAGAAAAACCAGAAACCAGAAACCAGTAAAACCAGCCGTAAACCAGCTAAACCAGAAAACCAGCTACAAACCAGAAACCAGCAAACCAGCAATGAAAACCAGACCAGAAACCAGCTAAAAACCAGGAGAGAAACCAGTAAACCAGAGCTTAAACCAGAAAACCAGAAACCAGTCAAACCAGAAAACCAGCAAACCAGATTGAAAACCAGAAACCAGCAAAACCAGGAAACCAGTAGATTGAAACCAGAAACCAGACTTATACAAACCAGTACATGGGCTCTAACAAACCAGCCTATGGCTGTGTGGATAAACCAGAAACCAGAATAAACCAGGGGCCAAACCAGGCGTAAACCAGGCTGAAACCAGAAACCAGAAACCAGCAAAACCAGCCGTTTTGCTCGAAACCAGGAAAACCAGAAACCAGCCAATAAACCAGAAACCAGGGAAACCAGGGCAAAACCAGTAAACCAGGCATAAACCAGCCCCGAAAAACCAGTTCTTAAACCAGGATCGATAAAACCAGTATAAAACCAGGAGTAAACCAGGAAACCAGGGACAAACCAGCTAAACCAGGTGAAACCAGGAAACCAGAAACCAGACTTAAACCAGGAAACCAGGTATGAAACCAGTAAAAACCAGGGAAAACCAGAAACCAGAAACCAGCCTAAACCAGTAAACCAGAAACCAGGAAACCAGAGAAACCAG AAACCAGAA
64 81 99 138 145 164 171 208 226 235 242 278 297 380 388 404 432 470 538 545 589 596 640 659 814 872 879 904
```

This will output all the positions in the sequence where the subsequence is found.

---

