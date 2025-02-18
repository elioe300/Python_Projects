import os

def folder_refiner(folder_path, extension):
    """
    Elimina archivos con extensiones específicas en un directorio dado.

    Parameters:
    folder_path (str): Ruta del directorio a limpiar.
    extension (str or list): Extensión o lista de extensiones de los archivos a eliminar.
    """
    try:
        # Verificar si la ruta del directorio existe
        if not os.path.exists(folder_path):
            print("La ruta indicada no existe.")
            return

        files_counter = 0  # Contador de archivos eliminados

        # Iterar sobre los elementos en el directorio
        for file in os.listdir(folder_path):
            file_path_name = os.path.join(folder_path, file)

            # Verificar si es un archivo (no un directorio)
            if os.path.isfile(file_path_name):
                _, file_extension = os.path.splitext(file)

                # Verificar si la extensión del archivo está en las extensiones a eliminar
                if isinstance(extension, list):
                    if file_extension in extension:
                        try:
                            os.remove(file_path_name)  # Eliminar el archivo
                            files_counter += 1
                            print(f"Archivo eliminado: {file_path_name}")
                        except PermissionError:
                            print(f"No se pudo eliminar {file_path_name}. Permiso denegado.")
                        except Exception as e:
                            print(f"No se pudo eliminar {file_path_name}. Error: {e}")
                else:
                    if file_extension == extension:
                        try:
                            os.remove(file_path_name)  # Eliminar el archivo
                            files_counter += 1
                            print(f"Archivo eliminado: {file_path_name}")
                        except PermissionError:
                            print(f"No se pudo eliminar {file_path_name}. Permiso denegado.")
                        except Exception as e:
                            print(f"No se pudo eliminar {file_path_name}. Error: {e}")

        if files_counter > 0:
            print(f"\nSe han eliminado {files_counter} archivo(s) con la extensión {extension}.")
        else:
            print("\nNo se encontraron archivos con las extensiones especificadas.")

    except Exception as e:
        print(f"Error detectado: {e}\nIntroduzca una ruta correcta.")

# Ejemplo de uso
# folder_refiner('ruta/al/directorio', '.txt')
# folder_refiner('ruta/al/directorio', ['.txt', '.log'])
