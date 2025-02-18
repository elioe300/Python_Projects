import os

def menu():
    """
    Muestra el menú principal de la aplicación de tomar notas por CLI y maneja las opciones seleccionadas por el usuario.
    """
    print("Bienvenido a la aplicación de tomar notas por CLI.\nEstas son sus funciones:")
    while True:
        try:
            option = int(input("""\nSe encuentra en el menú principal:
1 - Ver notas existentes
2 - Agregar una nueva nota.
3 - Eliminar una nota existente.
4 - Salir del programa.
Selecciona lo que desee: """))
            if option == 1:
                view_notes()
            elif option == 2:
                create_directory()
                create_note()
            elif option == 3:
                delete_note()
            elif option == 4:
                print("\nHa salido del programa.")
                break
            else:
                print("Número invalido, intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

global current_path
current_path = os.getcwd() + "/Notas"

def view_notes():
    """
    Muestra el contenido de una nota seleccionada por el usuario.
    """
    file_path = select_file()
    if file_path:
        with open(file_path, "r") as note:
            print(f"\nEste es el contenido del archivo:\n" + note.read())

def select_file():
    """
    Permite al usuario seleccionar un archivo de notas existente.

    Returns:
        str: La ruta del archivo seleccionado.
    """
    current_path = os.getcwd() + "/Notas"
    if not os.path.exists(current_path) or not os.path.isdir(current_path):
        print("\nLa ruta no existe o no es un directorio.")
        return None
    files = os.listdir(current_path)
    if not files:
        print("\nLa ruta está vacía.")
        return None
    while True:
        title = input(f"\nEstos son los archivos existentes a leer:\n{files}\n¿Cuál desea interactuar? ")
        file_path = f"{current_path}/{title}.txt"
        if os.path.exists(file_path):
            return file_path
        print("Título no encontrado, introduzca correctamente el título sin extensión.")

def delete_note():
    """
    Elimina una nota seleccionada por el usuario.
    """
    file_path = select_file()
    if file_path:
        os.remove(file_path)
        print("\nSe ha eliminado el archivo.")

def create_directory():
    """
    Crea el directorio 'Notas' si no existe.
    """
    if not os.path.exists(current_path):
        os.makedirs(current_path)

def overwrite_note():
    """
    Sobrescribe una nota existente con nuevo contenido.
    """
    os.remove(note_path)
    content = input("\nEscriba el nuevo contenido de la nota: \n")
    with open(note_path, "w") as note:
        note.write(content)
    print("\nNota sobreescrita.")

def add_note():
    """
    Añade contenido a una nota existente.
    """
    content = input("\nEscriba el contenido de la nota que desea añadir: \n")
    with open(note_path, "a") as note:
        note.write(content)
    print("\nContenido añadido.")

def create_note():
    """
    Crea una nueva nota o añade contenido a una nota existente.
    """
    title = input("\nIntroduzca el título de tu nota: ")
    global note_path
    note_path = f"{current_path}/{title}.txt"
    if os.path.exists(note_path):
        decision = input("\nArchivo ya creado, ¿desea sobreescribir? \nY o N \n").strip().upper()
        if decision == "Y":
            overwrite_note()
        elif decision == "N":
            add_note()
        return  
    else:
        content = input("\nEscriba el contenido de la nota: \n")
    with open(note_path, "w") as note:
        note.write(content)
    print("\nNota creada.")

# Ejecutar el menú principal
menu()
