# Project 5: Computing GC Content

## Description

This Python project aims to calculate the GC (guanine and cytosine) content of a DNA sequence, addressing the Rosalind challenge ["Computing GC Content"](https://rosalind.info/problems/gc/). The program takes a FASTA-formatted file with DNA sequences as input, calculates the GC content for each sequence, and identifies the sequence with the highest GC content, printing its ID and GC percentage. The objective is to follow the instructions from the book *Mastering Python for Bioinformatics*, as detailed below:

---

## Instructions

Create a program called `cgc.py` that accepts a FASTA-formatted DNA sequence file as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./cgc.py -h
usage: cgc.py [-h] FILE

Compute GC content

positional arguments:
  FILE        Input sequence file

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `cgc.py` accepts the following input:

1. **FASTA-formatted DNA sequence file (positional argument)**
```sh
$ cat tests/inputs/1.fa
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

---

## Program Output

The program will print the ID of the sequence with the highest GC content and its percentage:

```sh
$ ./cgc.py tests/inputs/input2.fa
Rosalind_5723 52.806415
```

---

## Usage Example

To execute the program and calculate the GC content of the sequences in a FASTA file:

1. Calling the program directly with the positional argument:
```sh
$ ./cgc.py tests/inputs/1.fa
Rosalind_0808 60.919540
```
2. Using the `<` operator to redirect input from a file:
```sh
$ ./cgc.py < tests/inputs/1.fa
Rosalind_0808 60.919540
```
3. Using a pipe:
```sh
$ cat tests/inputs/1.fa | ./cgc.py
Rosalind_0808 60.919540
```

---
