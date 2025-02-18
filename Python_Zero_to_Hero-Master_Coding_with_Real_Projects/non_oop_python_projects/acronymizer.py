import re

def acronymizer():
    """
    Transforma una frase dada por el usuario en un acrónimo.
    
    La función solicita al usuario que introduzca una frase,
    separa las palabras y crea un acrónimo tomando la primera
    letra de cada palabra y convirtiéndola en mayúscula.
    
    Returns:
        str: El acrónimo generado a partir de la frase ingresada.
    """
    # Solicita al usuario introducir una frase
    frase = input("Introduzca una frase que desee transformar en acrónimo: ")
    # Divide la frase en palabras usando un patrón regex que separa por cualquier caracter no alfabético
    palabras = re.split(r'[^a-zA-Z]', frase)
    acronimo = ""
    for palabra in palabras:
        if palabra:  # Verifica que la palabra no esté vacía
            # Toma la primera letra de cada palabra y la convierte en mayúscula
            acronimo += palabra[0].upper()
    return acronimo

