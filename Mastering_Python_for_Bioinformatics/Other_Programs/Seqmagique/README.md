# Project: Mimic seqmagick

## Descripción

Este proyecto de Python tiene como propósito imitar la funcionalidad del programa `seqmagick`, proporcionando estadísticas sobre secuencias en archivos FASTA. El programa toma como entrada uno o más archivos FASTA y genera una tabla que muestra varias estadísticas sobre las secuencias en cada archivo. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `seqmagique.py` que aceptará uno o más archivos FASTA como argumentos posicionales y un formato de tabla opcional. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

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

## Entradas del Programa

El archivo `seqmagique.py` acepta como input:

1. **Uno o más archivos FASTA (argumento posicional)**
2. **Formato de tabla opcional (argumento opcional)**


## Salida del Programa

El programa imprimirá una tabla con estadísticas sobre las secuencias en cada archivo FASTA:

```sh
$ ./seqmagique.py tests/inputs/*.fa
name                     min_len    max_len    avg_len    num_seqs
tests/inputs/1.fa             50         50      50.00           1
tests/inputs/2.fa             49         79      64.00           5
tests/inputs/empty.fa          0          0       0.00           0
```

## Ejemplo de Uso

Para ejecutar el programa y generar una tabla con estadísticas de secuencias en uno o más archivos FASTA:

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
