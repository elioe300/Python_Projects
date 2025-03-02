# Project: Grep through FASTX files

## Descripción

Este proyecto de Python tiene como propósito buscar patrones en archivos FASTX, proporcionando una funcionalidad similar a la del comando `grep`. El programa toma como entrada uno o más archivos FASTX (FASTA o FASTQ) y un patrón de búsqueda, y genera una salida con las secuencias que coinciden con el patrón. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `fastx_grep.py` que aceptará un patrón de búsqueda, uno o más archivos FASTX, y otros argumentos opcionales. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./fastx_grep.py -h
usage: fastx_grep.py [-h] [-f str] [-O str] [-o FILE] [-i] PATTERN FILE [FILE ...]

Grep through FASTX files

positional arguments:
  PATTERN              Search pattern
  FILE                 Input file(s)

optional arguments:
  -h, --help           show this help message and exit
  -f str, --format str Input file format (choices: ['fasta', 'fastq'])
  -O str, --outfmt str Output file format (choices: ['fasta', 'fastq', 'fasta-2line'])
  -o FILE, --outfile FILE
                       Output file
  -i, --insensitive    Case-insensitive search
```

## Entradas del Programa

El archivo `fastx_grep.py` acepta como input:

1. **Patrón de búsqueda (argumento posicional)**
2. **Uno o más archivos FASTX (argumento posicional)**
3. **Formato de archivo de entrada (argumento opcional)**
4. **Formato de archivo de salida (argumento opcional)**
5. **Archivo de salida (argumento opcional)**
6. **Búsqueda insensible a mayúsculas/minúsculas (argumento opcional)**

```sh
$ ./fastx_grep.py -i  "pattern" input.f[aq] -f fasta -O fasta -o output
```

## Salida del Programa

El programa imprimirá las secuencias que coinciden con el patrón de búsqueda en el formato especificado

## Ejemplo de Uso

Para ejecutar el programa y buscar un patrón en uno o más archivos FASTX, teniendo como archivo de entrada:
```sh
$ cat lsu.fa
>ITSLSUmock2p.ITS_M01380:138:000000000-C9GKM:1:1101:14440:2042 2:N:0
CAAGTTACTTCCTCTAAATGACCAAGCCTAGTGTAGAACCATGTCGTCAGTGTCAGTCTG
AGTGTAGATCTCGGTGGTCGCCGTATCATTAAAAAAAAAAATGTAATACTACTAGTAATT
ATTAATATTATAATTTTGTCTATTAGCATCTTATTATAGATAGAAGATATTATTCATATT
TCACTATCTTATACTGATATCAGCTTTATCAGATCACACTCTAGTGAAGATTGTTCTTAA
CTGAAATTTCCTTCTTCATACAGACACATTAATCTTACCTA
>ITSLSUmock2p.ITS_M01384:138:000000000-C9GKM:1:1101:14440:2043 2:N:0
ACCCGTCAATTTCTTTAAGTTTTAGCCTTGCGACCGTACTCCCCAGGCGGTGCACTTAGT
GGTTTTCCGGCGACCCGGGCGGCGTCAGAGCCCCCCAAGTCTCGTGCACATCGTTTACGG
CGTGGACTACCAGGGTATCTAATCCTGTTTGATCCCCACGCTTTCGTGCCTCAGCGTCAG
TACCGGCCCAGCCACCCGTCTTCACCTTCGGCGTTCCTGTAGATATCTACGCATTTCACC
GCTACACCTACAGTTCCGGTGGCGCCTACCGGCCTCAAGAAACGCAGTATGCCCAGCTAT
T

```sh
$ ./fastx_grep.py -i mo1380 tests/inputs/lsu.fa
>ITSLSUmock2p.ITS_M01380:138:000000000-C9GKM:1:1101:14440:2042 2:N:0
CAAGTTACTTCCTCTAAATGACCAAGCCTAGTGTAGAACCATGTCGTCAGTGTCAGTCTG
AGTGTAGATCTCGGTGGTCGCCGTATCATTAAAAAAAAAAATGTAATACTACTAGTAATT
ATTAATATTATAATTTTGTCTATTAGCATCTTATTATAGATAGAAGATATTATTCATATT
TCACTATCTTATACTGATATCAGCTTTATCAGATCACACTCTAGTGAAGATTGTTCTTAA
CTGAAATTTCCTTCTTCATACAGACACATTAATCTTACCTA
```

---
