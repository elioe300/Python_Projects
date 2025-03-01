# Project 6: Compute the Hamming Distance Between Two Strings

## Descripción

Este proyecto de Python tiene como propósito calcular la distancia de Hamming entre dos secuencias de ADN, superando el desafío de Rosalind ["Compute the Hamming Distance Between Two Strings"](https://rosalind.info/problems/ba1g/). El programa toma un único argumento posicional, que es un archivo legible que contendrá dos líneas de secuencias de ADN y que imprimirá la distancia de Hamming entre ellas. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `hamm.py` que aceptará dos secuencias de ADN como argumentos posicionales. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./hamm.py -h
usage: calculate_hamming_distance.py [-h] str str

Calculate Hamming distance

positional arguments:
  str         First DNA sequence
  str         Second DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `hamm.py` acepta como input:

1. **Dos secuencias de ADN (argumentos posicionales)**
```sh
$ cat tests/inputs/1.txt
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```
## Salida del Programa

El programa imprimirá la distancia de Hamming entre las dos secuencias de ADN proporcionadas:

```sh
$ ./hamm.py tests/inputs/1.txt
7
```

## Ejemplo de Uso

Para ejecutar el programa y calcular la distancia de Hamming entre dos secuencias de ADN:

```sh
$ ./hamm.py tests/inputs/2.txt
503
```

---
