import os
import shutil

def copy_archives(source_rute, backup_rute):
    """
    Copia archivos y subdirectorios desde el directorio de origen al directorio de respaldo.

    Args:
        source_rute (str): Ruta al directorio de origen.
        backup_rute (str): Ruta al directorio de respaldo.

    Returns:
        None: Esta función no devuelve ningún valor.
    """
    for rute_directory, subdirectories, archives in os.walk(source_rute):
        # Crear subdirectorios en el directorio de respaldo
        for subdirectory in subdirectories:
            backup_subdir = os.path.join(backup_rute, os.path.relpath(os.path.join(rute_directory, subdirectory), source_rute))
            os.makedirs(backup_subdir, exist_ok=True)

        # Copiar archivos al directorio de respaldo
        for archive in archives:
            source_archive_rute = os.path.join(rute_directory, archive)
            backup_archive_rute = os.path.join(backup_rute, os.path.relpath(source_archive_rute, source_rute))
            shutil.copy2(source_archive_rute, backup_archive_rute)

def clean_archives(source_rute, backup_rute):
    """
    Elimina archivos en el directorio de respaldo que ya no existen en el directorio de origen.

    Args:
        source_rute (str): Ruta al directorio de origen.
        backup_rute (str): Ruta al directorio de respaldo.

    Returns:
        None: Esta función no devuelve ningún valor.
    """
    for rute_directory, _, archives in os.walk(backup_rute):
        for archive in archives:
            backup_archive_rute = os.path.join(rute_directory, archive)
            source_archive_rute = os.path.join(source_rute, os.path.relpath(backup_archive_rute, backup_rute))
            # Eliminar archivos en el directorio de respaldo que no existen en el directorio de origen
            if not os.path.exists(source_archive_rute):
                os.remove(backup_archive_rute)

def backup_and_sync(source_rute, backup_rute):
    """
    Realiza una copia de seguridad y sincronización de archivos entre dos directorios.

    La función crea una copia de seguridad de los archivos y subdirectorios del directorio de origen
    en el directorio de respaldo. También limpia los archivos en el directorio de respaldo que ya no 
    existen en el directorio de origen.

    Args:
        source_rute (str): Ruta al directorio de origen.
        backup_rute (str): Ruta al directorio de respaldo.

    Returns:
        None: Esta función no devuelve ningún valor.
    """
    # Crear el directorio de respaldo si no existe
    if not os.path.exists(backup_rute):
        os.makedirs(backup_rute, exist_ok=True)
    
    # Copiar archivos y subdirectorios del directorio de origen al directorio de respaldo
    copy_archives(source_rute, backup_rute)
    
    # Limpiar archivos en el directorio de respaldo que ya no existen en el directorio de origen
    clean_archives(source_rute, backup_rute)

# Ejemplo de uso:
# backup_and_sync('ruta/al/directorio/origen', 'ruta/al/directorio/respaldo')

