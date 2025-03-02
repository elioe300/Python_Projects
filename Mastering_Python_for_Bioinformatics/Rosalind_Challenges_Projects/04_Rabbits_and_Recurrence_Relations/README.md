# Project 4: Rabbits and Recurrence Relations

## Descripción

Este proyecto de Python calcula la secuencia de Fibonacci en función del número de generaciones y el tamaño de la camada (litter), superando el desafío de Rosalind ["Rabbits and Recurrence Relations"](https://rosalind.info/problems/fib/). El programa toma como entrada el número de generaciones y el tamaño de la camada, y calcula el valor correspondiente de la secuencia de Fibonacci. El objetivo de este proyecto es seguir las instrucciones del libro "Mastering Python for Bioinformatics", las cuales son las siguientes:

## Instrucciones

Crea un programa llamado `fib.py` que aceptará dos argumentos posicionales: el número de generaciones y el tamaño de la camada. El programa debe imprimir una declaración de "uso" para las banderas `-h` o `--help`:

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

## Entradas del Programa

El archivo `fib.py` acepta como input:

1. **Número de generaciones (argumento posicional)**
2. **Tamaño de la camada por generación (argumento posicional)**

### Validación de Entradas

El programa valida que el número de generaciones esté entre 1 y 40, y que el tamaño de la camada esté entre 1 y 5.
```sh
$ ./fib.py -3 2
usage: fib.py [-h] generations litter
fib.py: error: generations "-3" must be between 1 and 40 
$ ./fib.py 5 10
usage: fib.py [-h] generations litter
fib.py: error: litter "10" must be between 1 and 5 
```

## Salida del Programa

El programa imprimirá el valor de la secuencia de Fibonacci para los parámetros proporcionados:

```sh
$ ./fib.py 5 3
19
```

## Ejemplo de Uso

Para ejecutar el programa y calcular la secuencia de Fibonacci en función del número de generaciones y el tamaño de la camada:

```sh
$ ./fib.py 30 4 
436390025825
```

---
