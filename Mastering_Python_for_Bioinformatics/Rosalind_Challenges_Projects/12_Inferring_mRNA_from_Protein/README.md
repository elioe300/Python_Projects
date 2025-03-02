# Project 12: Inferring mRNA from Protein

## Descripción

Este proyecto de Python tiene como propósito inferir la secuencia de mRNA a partir de una secuencia de proteínas, superando el desafío de Rosalind ["Inferring mRNA from Protein"](https://rosalind.info/problems/mrna/). El programa toma como entrada una secuencia de proteínas y calcula el número de posibles secuencias de mRNA que podrían haberla codificado. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa en Python llamado `mrna.py` que acepte una secuencia de proteína como un argumento posicional o un nombre de archivo junto con un argumento opcional "módulo" que por defecto sea 1,000,000.. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./mrna.py -h
usage: mrna.py [-h] [-m int] protein

Infer mRNA from Protein

positional arguments:
  protein          Input protein or file

optional arguments:
  -h, --help       show this help message and exit
  -m int, --modulo int
                   Modulo value (default: 1000000)
```

## Entradas del Programa

El archivo `mrna.py` acepta como input:

1. **Secuencia de proteínas o archivo que contiene la secuencia de proteínas (argumento posicional)**
```sh
$ cat 1.txt
MSVHDQCHHQLSFSMMECLLPRSEHTRMEWKTWDVVVWMPRRWPWGPSRDKTCIYAHTCMQGKDPIFHRIIP
```
2. **Valor de módulo opcional (argumento opcional)**

## Salida del Programa

El programa imprimirá el número de posibles secuencias de mRNA que podrían haber codificado la secuencia de proteínas proporcionada, utilizando el valor de módulo opcional:

```sh
$ ./mrna.py -m 1000000 MYPROTEIN
196608
```

## Ejemplo de Uso

Para ejecutar el programa y calcular el número de posibles secuencias de mRNA:

```sh
$ ./mrna.py MA
12

$ ./mrna.py -m 1000000 tests/inputs/1.txt
448832
```

---
