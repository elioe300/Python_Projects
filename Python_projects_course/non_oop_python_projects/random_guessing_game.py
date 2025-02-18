import random
import time

def random_guessing_game():
    """
    Inicia un juego de adivinanza de números. El programa genera un número aleatorio y el usuario debe adivinarlo en el menor número de intentos posibles.
    """
    print("""¡Bienvenido usuario al adivinador de números! 
El programa generará un número aleatorio y usted deberá adivinarlo en el menor número de intentos posibles.""")
    
    # Pausa de 5 segundos para que el usuario lea la introducción
    time.sleep(5)
    
    # Solicita al usuario introducir un rango superior para el número aleatorio
    while True:
        try:
            upper_limit = int(input("Se va a generar un número entre (1 - X), introduzca la X: "))
            break   
        except ValueError:
            # Manejo de excepciones para asegurarse de que el usuario ingrese un número válido
            print("Por favor, introduzca un número.")
    
    # Genera un número aleatorio entre 1 y el número ingresado por el usuario
    random_number = random.randint(1, upper_limit)
    attempts = 0  # Contador de intentos fallidos
    
    # Bucle para que el usuario adivine el número
    while True:
        guess = int(input("Toca adivinar, introduzca un número: "))
        
        # Verifica si el número adivinado es mayor, menor o igual al número generado
        if guess > random_number:
            print("Demasiado alto. Intenta de nuevo.")
            attempts += 1
        elif guess < random_number:
            print("Demasiado bajo. Intenta de nuevo.")
            attempts += 1
        elif guess == random_number:
            # El usuario ha adivinado correctamente, se muestra el número de intentos y se sale del bucle
            print(f"¡Felicidades! Has adivinado el número en {attempts} intentos.")
            break

# Ejemplo de uso
# random_guessing_game()
