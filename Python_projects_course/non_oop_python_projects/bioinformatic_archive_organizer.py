import os
import shutil

def bioinformatics_file_organizer(route):
    """
    Organiza archivos en carpetas según su extensión en un directorio dado.
    
    :param route: Ruta del directorio donde se encuentran los archivos.
    """
    try:
        file_list = os.listdir(route)  # Listar los archivos en la ruta dada
    except FileNotFoundError:
        print("Error: La ruta especificada no existe.")
        return
    except PermissionError:
        print("Error: No tienes permisos para acceder a esta carpeta.")
        return
    
    extensions = {}  # Diccionario para almacenar las extensiones y sus carpetas
    while True:
        keys = input("Introduzca la extensión de esta forma [\".extension\"] que quiera mover (o 'q' para salir): ").strip()
        if keys.lower() == 'q':
            break
        if not keys.startswith('.'):
            print("Error: La extensión debe comenzar con un punto (ejemplo: .txt)")
            continue
        key = [x.strip() for x in keys.split(",") if x.strip().startswith('.')]
        value = input("Introduzca cómo quiere que se llame la carpeta: ").strip()
        if not value:
            print("Error: El nombre de la carpeta no puede estar vacío.")
            continue
        extensions[value] = key
    
    # Crear directorios si no existen
    for directory in extensions.keys():
        folder_path = os.path.join(route, directory)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
    
    # Mover archivos a los directorios correspondientes
    for file in file_list:
        file_path = os.path.join(route, file)
        if os.path.isfile(file_path):  # Asegurarse de que es un archivo y no un directorio
            extension = os.path.splitext(file)[1]
            for folder, ext_list in extensions.items():
                if extension in ext_list:
                    extension_path = os.path.join(route, folder)
                    try:
                        shutil.move(file_path, extension_path)
                        print(f"Movido: {file} -> {extension_path}")
                    except Exception as e:
                        print(f"Error al mover {file}: {e}")
                    break

    print("Organización completada.")
