# Project 5: Computing GC Content

## Descripción

Este proyecto de Python tiene como propósito calcular el contenido de GC (guanina y citosina) de una secuencia de ADN, superando el desafío de Rosalind ["Computing GC Content"](https://rosalind.info/problems/gc/). El programa toma como entrada un archivo en formato FASTA con secuencias de ADN y calcula el contenido de GC de cada secuencia. Luego, identifica la secuencia con el contenido de GC más alto y la imprime junto con su porcentaje de GC. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `cgc.py` que aceptará un archivo de secuencias de ADN en formato FASTA como argumento posicional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

```sh
$ ./cgc.py -h
usage: compute_gc_content.py [-h] FILE

Compute GC content

positional arguments:
  FILE        Input sequence file

optional arguments:
  -h, --help  show this help message and exit
```

## Entradas del Programa

El archivo `cgc.py` acepta como input:

1. **Archivo de secuencias de ADN en formato FASTA (argumento posicional)**
```sh
$ cat tests/inputs/1.fa
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

## Salida del Programa

El programa imprimirá el ID de la secuencia con el contenido de GC más alto y su porcentaje de GC:

```sh
$ ./cgc.py tests/inputs/input2.fa
Rosalind_5723 52.806415
```

## Ejemplo de Uso

Para ejecutar el programa y calcular el contenido de GC de las secuencias en un archivo FASTA:

```sh
$ ./cgc.py tests/inputs/1.fa
Rosalind_0808 60.919540
```

---
