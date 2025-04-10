# Project 4: Rabbits and Recurrence Relations

## Description

This Python project calculates the Fibonacci sequence based on the number of generations and litter size, tackling the Rosalind challenge ["Rabbits and Recurrence Relations"](https://rosalind.info/problems/fib/). The program takes the number of generations and litter size as input and calculates the corresponding value of the Fibonacci sequence. The goal of this project is to follow the guidelines from the book *Mastering Python for Bioinformatics*, as outlined below:

---

## Instructions

Create a program called `fib.py` that accepts two positional arguments: the number of generations and the litter size. The program should print a usage statement for the flags `-h` or `--help`:

```sh
$ ./fib.py -h
usage: fib.py [-h] generations litter

Calculate Fibonacci sequence

positional arguments:
  generations  Number of generations
  litter       Size of litter per generation

optional arguments:
  -h, --help   show this help message and exit
```

---

## Program Inputs

The file `fib.py` accepts the following inputs:

1. **Number of generations (positional argument)**
2. **Litter size per generation (positional argument)**

### Input Validation

The program validates that the number of generations is between 1 and 40, and the litter size is between 1 and 5.
```sh
$ ./fib.py -3 2
usage: fib.py [-h] generations litter
fib.py: error: generations "-3" must be between 1 and 40
$ ./fib.py 5 10
usage: fib.py [-h] generations litter
fib.py: error: litter "10" must be between 1 and 5
```

---

## Program Output

The program will print the Fibonacci sequence value for the given parameters:

```sh
$ ./fib.py 5 3
19
```

---

## Usage Example

To run the program and calculate the Fibonacci sequence based on the number of generations and litter size:

```sh
$ ./fib.py 30 4
436390025825
```

---
