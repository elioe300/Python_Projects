# Project 7: Translating RNA into Protein

## Description

This Python project is designed to translate RNA sequences into protein sequences, addressing the Rosalind challenge ["Translating RNA into Protein"](https://rosalind.info/problems/prot/). The program takes an RNA sequence as input and translates it into the corresponding protein sequence using the standard genetic code. The goal is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `prot.py` that accepts an RNA sequence as a positional argument. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./prot.py -h
usage: prot.py [-h] RNA

Translate RNA to proteins

positional arguments:
  RNA         RNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

---

## Program Inputs

The file `prot.py` accepts the following input:

1. **RNA sequence (positional argument)**

```sh
$ ./prot.py AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUGACUGAAGGUUUGGGAUCCCG
```

---

## Program Output

The program will print the protein sequence translated from the provided RNA sequence:

```sh
$ ./prot.py AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
MAMAPRTEINSTRING
```

---

## Usage Example

To run the program and translate an RNA sequence into proteins:

```sh
$ ./prot.py AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUGACUGAAGGUUUGGGAUCCCG
MAIVMGR
```

---
