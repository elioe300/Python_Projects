# Project: Mimic seqmagick

## Description

This Python project aims to mimic the functionality of the `seqmagick` program by providing statistics about sequences in FASTA files. The program takes one or more FASTA files as input and generates a table showing various statistics for the sequences in each file. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `seqmagique.py` that accepts one or more FASTA files as positional arguments and an optional table format. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./seqmagique.py -h
usage: seqmagique.py [-h] [-t table] FILE [FILE ...]

Mimic seqmagick

positional arguments:
  FILE                  Input FASTA file(s)

optional arguments:
  -h, --help            show this help message and exit
  -t table, --table_format table
                        Tabulate table style (default: plain)
                        choices: ['plain', 'simple', 'grid', 'pipe', 'orgtbl',
                                  'rst', 'mediawiki', 'latex', 'latex_raw',
                                  'latex_booktabs']
```

---

## Program Inputs

The file `seqmagique.py` accepts the following inputs:

1. **One or more FASTA files (positional arguments)**
2. **Optional table format (optional argument)**

---

## Program Output

The program will print a table with statistics about the sequences in each FASTA file:

```sh
$ ./seqmagique.py tests/inputs/*.fa
name                     min_len    max_len    avg_len    num_seqs
tests/inputs/1.fa             50         50      50.00           1
tests/inputs/2.fa             49         79      64.00           5
tests/inputs/empty.fa          0          0       0.00           0
```

---

## Usage Example

To run the program and generate a table with sequence statistics for one or more FASTA files:

```sh
$ ./seqmagique.py -t grid tests/inputs/file1.fasta tests/inputs/file2.fasta
+----------------+---------+---------+---------+-----------+
| name           | min_len | max_len | avg_len | num_seqs  |
+================+=========+=========+=========+===========+
| tests/inputs/file1.fasta | 10      | 15      | 12.50    | 4         |
+----------------+---------+---------+---------+-----------+
| tests/inputs/file2.fasta | 20      | 30      | 25.00    | 2         |
+----------------+---------+---------+---------+-----------+
```

---
