import os
import hashlib
import shutil
from datetime import datetime

def calculate_md5(archive_route):
    """
    Calcula el hash MD5 de un archivo.

    Args:
        archive_route (str): La ruta del archivo.

    Returns:
        str: El valor hash en formato hexadecimal.
    """
    hasher = hashlib.md5()  # Crea un nuevo objeto hash MD5.
    with open(archive_route, "rb") as f:  # Abre el archivo en modo binario (lectura).
        for block in iter(lambda: f.read(4096), b""):  # Lee el archivo en bloques de 4096 bytes hasta que se alcance el final.
            hasher.update(block)  # Actualiza el hash con el contenido del bloque.
    return hasher.hexdigest()  # Retorna el valor hash en formato hexadecimal.

def hash_datetime_log_copy(log_route, archive_route):
    """
    Guarda en un archivo log el hash del archivo copiado y la hora en que se produce la copia.

    Args:
        log_route (str): La ruta del archivo log.
        archive_route (str): La ruta del archivo copiado.

    Returns:
        None
    """
    hash_file = calculate_md5(archive_route)  # Calcula el hash MD5 del archivo.
    timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y")  # Obtiene la marca de tiempo actual en el formato especificado (HH:MM:SS dd:mm:YYYY).
    with open(log_route, "a") as log:  # Abre el archivo log en modo adjunto (append).
        log.write(f"{timestamp} - Archivo {archive_route} copiado con el siguiente hash {hash_file}:\n")  # Escribe la marca de tiempo, la ruta del archivo y su hash en el log.

def hash_datetime_log_eliminate(log_route, archive_route):
    """
    Guarda en un archivo log el hash del archivo eliminado y la hora en que se produce el borrado.

    Args:
        log_route (str): La ruta del archivo log.
        archive_route (str): La ruta del archivo eliminado.

    Returns:
        None
    """
    hash_file = calculate_md5(archive_route)  # Calcula el hash MD5 del archivo.
    timestamp = datetime.now().strftime("%H:%M:%S %d-%m-%Y")  # Obtiene la marca de tiempo actual en el formato especificado (HH:MM:SS dd:mm:YYYY).
    with open(log_route, "a") as log:  # Abre el archivo log en modo adjunto (append).
        log.write(f"{timestamp} - Archivo {archive_route} eliminado con el siguiente hash {hash_file}:\n")  # Escribe la marca de tiempo, la ruta del archivo y su hash en el log.

def copy_archives(source_route, backup_route):
    """
    Copia archivos desde la carpeta de origen a la carpeta de respaldo y registra la copia en un log.

    Args:
        source_route (str): La ruta de la carpeta de origen.
        backup_route (str): La ruta de la carpeta de respaldo.

    Returns:
        None
    """
    log_route = os.path.join(backup_route, "sync_log.txt")  # Establece la ruta del archivo log en la carpeta de respaldo.
    for root, sub_directories, archives in os.walk(source_route):  # Itera sobre los subdirectorios y archivos en la carpeta de origen.
        for sub_directory in sub_directories:
            backup_subdirectory_route = os.path.join(backup_route, os.path.relpath(os.path.join(root, sub_directory), source_route))  # Obtiene la ruta del subdirectorio en la carpeta de respaldo.
            os.makedirs(backup_subdirectory_route, exist_ok=True)  # Crea el subdirectorio en la carpeta de respaldo si no existe.

        for archive in archives:
            source_archive_route = os.path.join(root, archive)  # Obtiene la ruta completa del archivo en el directorio de origen.
            backup_archive_route = os.path.join(backup_route, os.path.relpath(source_archive_route, source_route))  # Obtiene la ruta completa del archivo en el directorio de respaldo.
            hash_datetime_log_copy(log_route, source_archive_route)  # Registra el hash y la marca de tiempo del archivo copiado en el log.
            shutil.copy2(source_archive_route, backup_archive_route)  # Copia el archivo de origen a la ruta de respaldo.
            print("Se han copiado archivos en tu carpeta de respaldo.")

def clean_archives(source_route, backup_route):
    """
    Elimina archivos en la carpeta de respaldo que ya no existen en la carpeta de origen y registra la eliminación en un log.

    Args:
        source_route (str): La ruta de la carpeta de origen.
        backup_route (str): La ruta de la carpeta de respaldo.

    Returns:
        None
    """
    log_route = os.path.join(backup_route, "sync_log.txt")  # Establece la ruta del archivo log en la carpeta de respaldo.
    for root, _, archives in os.walk(backup_route):  # Itera sobre los archivos en la carpeta de respaldo.
        for archive in archives:
            backup_archive_route = os.path.join(root, archive)  # Obtiene la ruta completa del archivo en el directorio de respaldo.
            source_archive_route = os.path.join(source_route, os.path.relpath(backup_archive_route, backup_route))  # Obtiene la ruta completa del archivo correspondiente en el directorio de origen.
            if not os.path.exists(source_archive_route):  # Verifica si el archivo no existe en el directorio de origen.
                hash_datetime_log_eliminate(log_route, backup_archive_route)  # Registra el hash y la marca de tiempo del archivo eliminado en el log.
                try:
                    os.remove(backup_archive_route)  # Elimina el archivo de la carpeta de respaldo.
                    print("Se han eliminado archivos en tu carpeta de respaldo.")
                except Exception as e:
                    print(f"Error al eliminar {backup_archive_route}: {e}")  # Muestra un mensaje de error si la eliminación falla.

def backup_and_sync(source_route, backup_route):
    """
    Sincroniza archivos entre dos carpetas mediante el uso de hash. Limpia archivos obsoletos y copia archivos nuevos o modificados.

    Args:
        source_route (str): La ruta de la carpeta de origen.
        backup_route (str): La ruta de la carpeta de respaldo.

    Returns:
        None
    """
    if os.path.exists(backup_route):  # Verifica si la ruta de respaldo existe.
        clean_archives(source_route, backup_route)  # Limpia archivos obsoletos en la ruta de respaldo.
        copy_archives(source_route, backup_route)  # Copia archivos desde la carpeta de origen a la de respaldo.
    else:
        os.makedirs(backup_route, exist_ok=True)  # Crea la carpeta de respaldo si no existe.
        copy_archives(source_route, backup_route)  # Copia archivos desde la carpeta de origen a la de respaldo.

# Ejemplo de uso
backup_and_sync("C:\\Users\\USUARIO\\Desktop\\Elías\\Variados\\Python\\Simple_projects\\", "C:\\Users\\USUARIO\\Desktop\\Elías\\Variados\\Python\\backup_folder")
