# Project 11: Finding a Protein Motif

## Description

This Python project aims to find the locations of the N-glycosylation motif in protein sequences, addressing the Rosalind challenge ["Finding a Protein Motif"](https://rosalind.info/problems/mprt/). The program takes a text file with UniProt IDs as input, downloads the corresponding FASTA files, and searches for N-glycosylation motifs in the protein sequences. The goal of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as detailed below:

---

## Instructions

Create a program called `mprt.py` that accepts a text file of UniProt IDs as a positional argument and an optional download directory. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./mprt.py -h
usage: mprt.py [-h] [-d DIR] FILE

Find locations of N-glycosylation motif

positional arguments:
  FILE        Input text file of UniProt IDs

optional arguments:
  -h, --help  show this help message and exit
  -d DIR, --download_dir DIR
              Directory to download FASTA files (default: fasta)
```

---

## Program Inputs

The file `mprt.py` accepts the following inputs:

1. **Text file with UniProt IDs (positional argument)**:
```sh
$ cat tests/inputs/1.txt
A2Z669
B5ZC00
P07204
P20840
```
2. **Optional download directory (optional argument)**

---

## Program Output

The program will print the UniProt IDs and the positions of the N-glycosylation motifs found in the protein sequences:

```sh
$ ./mprt.py tests/inputs/1.txt
B5ZC00
85 118 142 306 395
P07204
47 115 116 382 409
P20840
79 109 135 248 306 348 364 402 485 501 614
```

---

## Usage Example

To download the FASTA files, execute the program, and find the locations of N-glycosylation motifs in the downloaded protein sequences:

```sh
$ ./mprt.py tests/inputs/2.txt
A3DF24
178
P01042
48 169 205 294
P07204
47 115 116 382 409
P07585
211 262 303
P13473
32 38 49 58 75 101 123 179 229 242 257 275 300 307 317 356
P20840
79 109 135 248 306 348 364 402 485 501 614
P42098
124 146 179 271
P80069
7 161
Q13VE3
95
Q7S432
173
Q9QSP4
```

---
