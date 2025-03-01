# Project 2: Transcribe DNA into RNA

## Descripción

Este proyecto de Python transcribe secuencias de ADN a secuencias de ARN, superando el desafio de Rosalind ["Transcribing DNA into RNA"](https://rosalind.info/problems/rna/). El programa toma uno o más archivos de ADN como entrada y genera archivos correspondientes con las secuencias de ARN transcritas en un directorio de salida especificado. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instruciones

Crea un programa llamado `transcribe_dna.py` que aceptará uno o más archivos de ADN como argumentos posicionales. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./transcribe_dna.py -h
usage: transcribe_dna.py [-h] [--out_dir DIR] FILE [FILE ...]

Transcribe DNA into RNA

positional arguments:
  FILE          Input DNA file(s)

optional arguments:
  -h, --help    show this help message and exit
  -o DIR, --out_dir DIR
                Output directory (default: out)
```

## Entradas del Programa

El archivo `transcribe_dna.py` acepta como input:

1. **Uno o más archivos de ADN (argumento(s) posicional(es))**
```sh
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
```
2. **Directorio de salida opcional (argumento opcional)**


## Salida del Programa

El directorio de salida predeterminado es "out". El programa debe imprimir un mensaje indicando cuántas secuencias se han transcrito y cuántos archivos de salida se han creado en el directorio especificado:

```sh
$ ./transcribe_dna.py -o rna_out input1.txt input2.txt
Done, wrote 3 sequences in 2 files to directory "rna_out".
```

Cada archivo de salida contendrá las secuencias de ARN transcritas correspondientes a las secuencias de ADN de los archivos de entrada.

## Ejemplo de Uso

Para ejecutar el programa y transcribir las secuencias de ADN en uno o más archivos de entrada:

```sh
$ ./transcribe_dna.py -o rna_out input1.txt input2.txt
Done, wrote 3 sequences in 2 files to directory "rna_out".
```

Esto creará un archivo de salida en el directorio `rna_out` para cada archivo de entrada con las secuencias de ARN transcritas.

---
