# Project 2: Transcribe DNA into RNA

## Description

This Python project transcribes DNA sequences into RNA sequences, addressing the Rosalind challenge ["Transcribing DNA into RNA"](https://rosalind.info/problems/rna/). The program takes one or more DNA files as input and generates corresponding files with the transcribed RNA sequences in a specified output directory. The objective of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as detailed below:

---

## Instructions

Create a program called `rna.py` that accepts one or more DNA files as positional arguments. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./rna.py -h
usage: rna.py [-h] [--out_dir DIR] FILE [FILE ...]

Transcribe DNA into RNA

positional arguments:
  FILE          Input DNA file(s)

optional arguments:
  -h, --help    show this help message and exit
  -o DIR, --out_dir DIR
                Output directory (default: out)
```

---

## Program Inputs

The file `rna.py` accepts the following inputs:

1. **One or more DNA files (positional argument(s))**
```sh
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
```
2. **Optional output directory (optional argument)**

---

## Program Output

The default output directory is "out". The program should print a message indicating how many sequences were transcribed and how many output files were created in the specified directory:

```sh
$ ./rna.py -o rna_out input1.txt input2.txt
Done, wrote 3 sequences in 2 files to directory "rna_out".
```

Each output file will contain the transcribed RNA sequences corresponding to the DNA sequences in the input files.

---

## Usage Example

To run the program and transcribe the DNA sequences in one or more input files:

```sh
$ ./rna.py --out_dir rna tests/inputs/*
Done, wrote 5 sequences in 3 files to directory "rna".
```

This will create an output file in the `rna` directory for each input file with the transcribed RNA sequences.

---
