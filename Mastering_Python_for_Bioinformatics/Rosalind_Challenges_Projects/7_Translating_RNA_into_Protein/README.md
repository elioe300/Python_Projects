# Project 7: Translating RNA into Protein

## Descripción

Este proyecto de Python tiene como propósito traducir secuencias de ARN a secuencias de proteínas, superando el desafío de Rosalind ["Translating RNA into Protein"](https://rosalind.info/problems/prot/). El programa toma como entrada una secuencia de ARN y traduce esa secuencia a la correspondiente secuencia de proteínas utilizando el código genético estándar. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `prot.py` que aceptará una secuencia de ARN como argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./prot.py -h
usage: translate_rna_to_protein.py [-h] RNA

Translate RNA to proteins

positional arguments:
  RNA         RNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `prot.py` acepta como input:

1. **Secuencia de ARN (argumento posicional)**

```sh
$ ./prot.py AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUGACUGAAGGUUUGGGAUCCCG
```

## Salida del Programa

El programa imprimirá la secuencia de proteínas traducida de la secuencia de ARN proporcionada:

```sh
$ ./prot.py AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUGACUGAAGGUUUGGGAUCCCG
MAMAPRTEINSTRING
```

## Ejemplo de Uso

Para ejecutar el programa y traducir una secuencia de ARN a proteínas:

```sh
$ ./prot.py AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUGACUGAAGGUUUGGGAUCCCG
MAMAPRTEINSTRING
```

---
