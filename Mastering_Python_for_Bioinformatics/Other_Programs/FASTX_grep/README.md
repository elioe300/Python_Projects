# Project: Grep through FASTX files

## Description

This Python project aims to search for patterns in FASTX files, providing functionality similar to the `grep` command. The program takes one or more FASTX files (FASTA or FASTQ) and a search pattern as input and outputs sequences matching the pattern. The goal of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `fastx_grep.py` that accepts a search pattern, one or more FASTX files, and additional optional arguments. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./fastx_grep.py -h
usage: fastx_grep.py [-h] [-f str] [-O str] [-o FILE] [-i] PATTERN FILE [FILE ...]

Grep through FASTX files

positional arguments:
  PATTERN              Search pattern
  FILE                 Input file(s)

optional arguments:
  -h, --help           show this help message and exit
  -f str, --format str Input file format (choices: ['fasta', 'fastq'])
  -O str, --outfmt str Output file format (choices: ['fasta', 'fastq', 'fasta-2line'])
  -o FILE, --outfile FILE
                       Output file
  -i, --insensitive    Case-insensitive search
```

---

## Program Inputs

The file `fastx_grep.py` accepts the following inputs:

1. **Search pattern (positional argument)**
2. **One or more FASTX files (positional argument)**
3. **Input file format (optional argument)**
4. **Output file format (optional argument)**
5. **Output file (optional argument)**
6. **Case-insensitive search (optional argument)**

```sh
$ ./fastx_grep.py -i "pattern" input.f[aq] -f fasta -O fasta -o output
```

---

## Program Output

The program will print the sequences matching the search pattern in the specified output format.

---

## Usage Example

To run the program and search for a pattern in one or more FASTX files, with the following input file:

```sh
$ cat lsu.fa
>ITSLSUmock2p.ITS_M01380:138:000000000-C9GKM:1:1101:14440:2042 2:N:0
CAAGTTACTTCCTCTAAATGACCAAGCCTAGTGTAGAACCATGTCGTCAGTGTCAGTCTG
AGTGTAGATCTCGGTGGTCGCCGTATCATTAAAAAAAAAAATGTAATACTACTAGTAATT
ATTAATATTATAATTTTGTCTATTAGCATCTTATTATAGATAGAAGATATTATTCATATT
TCACTATCTTATACTGATATCAGCTTTATCAGATCACACTCTAGTGAAGATTGTTCTTAA
CTGAAATTTCCTTCTTCATACAGACACATTAATCTTACCTA
>ITSLSUmock2p.ITS_M01384:138:000000000-C9GKM:1:1101:14440:2043 2:N:0
ACCCGTCAATTTCTTTAAGTTTTAGCCTTGCGACCGTACTCCCCAGGCGGTGCACTTAGT
GGTTTTCCGGCGACCCGGGCGGCGTCAGAGCCCCCCAAGTCTCGTGCACATCGTTTACGG
CGTGGACTACCAGGGTATCTAATCCTGTTTGATCCCCACGCTTTCGTGCCTCAGCGTCAG
TACCGGCCCAGCCACCCGTCTTCACCTTCGGCGTTCCTGTAGATATCTACGCATTTCACC
GCTACACCTACAGTTCCGGTGGCGCCTACCGGCCTCAAGAAACGCAGTATGCCCAGCTAT
T
```

Running the program with:

```sh
$ ./fastx_grep.py -i mo1380 tests/inputs/lsu.fa
```

Will output:

```sh
>ITSLSUmock2p.ITS_M01380:138:000000000-C9GKM:1:1101:14440:2042 2:N:0
CAAGTTACTTCCTCTAAATGACCAAGCCTAGTGTAGAACCATGTCGTCAGTGTCAGTCTG
AGTGTAGATCTCGGTGGTCGCCGTATCATTAAAAAAAAAAATGTAATACTACTAGTAATT
ATTAATATTATAATTTTGTCTATTAGCATCTTATTATAGATAGAAGATATTATTCATATT
TCACTATCTTATACTGATATCAGCTTTATCAGATCACACTCTAGTGAAGATTGTTCTTAA
CTGAAATTTCCTTCTTCATACAGACACATTAATCTTACCTA
```

---
