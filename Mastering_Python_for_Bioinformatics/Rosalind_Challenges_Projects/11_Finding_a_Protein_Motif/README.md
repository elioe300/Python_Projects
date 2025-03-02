# Project 11: Finding a Protein Motif

## Descripción

Este proyecto de Python tiene como propósito encontrar las ubicaciones del motivo de N-glicosilación en secuencias de proteínas, superando el desafío de Rosalind ["Finding a Protein Motif"](https://rosalind.info/problems/mprt/). El programa toma como entrada un archivo de texto con IDs de UniProt, descarga los archivos FASTA correspondientes y busca motivos de N-glicosilación en las secuencias de proteínas. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `mprt.py` que aceptará un archivo de texto con IDs de UniProt como argumento posicional y un directorio de descarga opcional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

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

## Entradas del Programa

El archivo `mprt.py` acepta como input:

1. **Archivo de texto con IDs de UniProt (argumento posicional)**
```sh
$ cat tests/inputs/1.txt
A2Z669
B5ZC00
P07204
P20840
```
2. **Directorio de descarga opcional (argumento opcional)**


## Salida del Programa

El programa imprimirá los IDs de UniProt y las posiciones de los motivos de N-glicosilación encontrados en las secuencias de proteínas:

```sh
$ ./mprt.py tests/inputs/1.txt
B5ZC00
85 118 142 306 395
P07204
47 115 116 382 409
P20840
79 109 135 248 306 348 364 402 485 501 614
```

## Ejemplo de Uso

Es importante descargar el bash script para descargar los archivos FASTA, ejecutar el programa y encontrar las ubicaciones de los motivos de N-glicosilación en las secuencias de proteínas descargadas:

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
