import os

def file_rename(folder_path, prefix, extension):
    """
    Renombra archivos en un directorio especificado.

    La función toma todos los archivos en un directorio dado y los renombra con un prefijo y un índice numerado.

    Args:
        folder_path (str): La ruta al directorio que contiene los archivos a renombrar.
        prefix (str): El prefijo a añadir al nuevo nombre de los archivos.
        extension (str): La extensión de los archivos que deben ser renombrados.

    Returns:
        None: Esta función no devuelve ningún valor.
    """
    try:
        # Verificar si la ruta del directorio existe
        if os.path.exists(folder_path):
            file_list = os.listdir(folder_path)
            # Iterar sobre los archivos en el directorio
            for index, file_name in enumerate(file_list):
                old_file_path = os.path.join(folder_path, file_name)
                new_name_file = f"{prefix}_{index+1}.{extension}"
                new_file_path = os.path.join(folder_path, new_name_file)
                # Renombrar el archivo
                os.rename(old_file_path, new_file_path)
            print("Renombre de archivos completado.")
        else:
            # Mensaje de error si la ruta del directorio no existe
            print("El directorio especificado no existe.")
    except Exception as e:
        # Mensaje de error detallado si ocurre una excepción
        print(f"Error detectado: {e}\nIntroduzca una ruta correcta.")

# Ejemplo de uso
# file_rename('ruta/al/directorio', 'prefijo', 'txt')
