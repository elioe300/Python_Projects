import re

def bmi_tracker():
    """
    Calculadora de Índice de Masa Corporal (BMI).

    La función solicita al usuario que introduzca la altura en centímetros y el peso en kilogramos.
    Luego calcula el BMI y proporciona una interpretación basada en el valor calculado.

    Returns:
        str: Una interpretación del BMI calculado.
    """
    print("Bienvenido a la calculadora BMI. A continuación deberá introducir la altura y el peso del sujeto.")
    
    while True:
        try:
            altura = input("Introduzca la altura del sujeto en centímetros:\n")
            peso = input("Introduzca el peso del sujeto en kilogramos:\n")
            
            # Verificar si las entradas contienen letras
            if re.search(r'[a-zA-Z]', altura) or re.search(r'[a-zA-Z]', peso):
                print("Detalles no válidos. Las entradas no deben contener letras.")
                continue
            
            # Convertir altura a metros y peso a float
            altura = float(altura) / 100
            peso = float(peso)
            
            # Verificar que los valores sean mayores que 0
            if altura <= 0 or peso <= 0:
                print("Por favor, introduzca un valor superior a 0.")
            else:
                break
        except ValueError:
            print("Se ha producido un error. Por favor, introduzca un valor numérico.")
    
    # Calcular el BMI
    valor_bmi = peso / (altura * altura)
    
    # Proporcionar una interpretación del BMI calculado
    if valor_bmi <= 16:
        return "El usuario está severamente bajo de peso."
    elif valor_bmi <= 18.5:
        return "El usuario está bajo de peso."
    elif valor_bmi <= 25:
        return "El usuario tiene un peso saludable."
    elif valor_bmi <= 30:
        return "El usuario tiene sobrepeso."
    else:
        return "El usuario está severamente con sobrepeso."