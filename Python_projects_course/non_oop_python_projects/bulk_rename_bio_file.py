import os

def bulk_rename(folder_path, prefix, extension):
    """
    Renombra en masa archivos en un directorio especificado.

    La función toma todos los archivos en un directorio dado con una extensión específica
    y los renombra con un prefijo y un índice numerado.

    Args:
        folder_path (str): La ruta al directorio que contiene los archivos a renombrar.
        prefix (str): El prefijo a añadir al nuevo nombre de los archivos.
        extension (str): La extensión de los archivos que deben ser renombrados.

    Returns:
        None
    """
    try:
        # Obtener la lista de archivos en el directorio especificado
        file_list = os.listdir(folder_path)
        index = 0  # Inicializar el índice para el renombrado
        for name in file_list:
            old_file_path = os.path.join(folder_path, name)
            file_name_no_extension, file_extension = os.path.splitext(name)
            if file_extension == extension:
                index += 1
                new_file_name = f"{prefix}_" + str(index) + f"{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                # Renombrar el archivo
                os.rename(old_file_path, new_file_path)
    except FileNotFoundError:
        print("Error: Folder not found. Please provide a valid folder path.")

# Ejemplo de uso
# bulk_rename('ruta/al/directorio', 'prefijo', '.txt')
