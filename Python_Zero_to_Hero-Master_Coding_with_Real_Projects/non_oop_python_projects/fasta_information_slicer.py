import os

def fasta_info_slicer(fasta_file):
    """
    Procesa un archivo FASTA y extrae información sobre identificadores y sus secuencias.

    Args:
        fasta_file (str): La ruta al archivo FASTA que se desea procesar.

    Returns:
        dict: Un diccionario con el nombre del archivo como clave y un diccionario de identificadores,
              descripciones y secuencias como valor. Devuelve None si el archivo no tiene la extensión .fasta.
    """
    # Obtener el nombre del archivo y su extensión
    file_name = os.path.basename(fasta_file)
    _, extension = os.path.splitext(fasta_file)
    
    if extension == ".fasta":
        file_data = {}
        with open(fasta_file, "r") as f:
            information = {}
            sequence = ""
            identifier = ""
            
            # Leer el archivo línea por línea
            for line in f:
                if line.startswith(">"):
                    if identifier:
                        # Guardar la secuencia para el identificador previo
                        information[identifier].update({"sequence": sequence})
                        sequence = ""  # Reiniciar la secuencia para el próximo identificador
                        
                    parts = line.split(" ", 1)
                    identifier = parts[0][1:]  # Remover el carácter '>'
                    descriptor = parts[1].strip() if len(parts) > 1 else ""
                    information[identifier] = {"descriptor": descriptor}
                else:
                    sequence += line.strip()
            
            # Guardar la secuencia del último identificador
            if identifier:
                information[identifier].update({"sequence": sequence})
            
            file_data[file_name] = information
        
        return file_data
    else:
        return None  # Devolver None si el archivo no es un archivo .fasta

def iterator(directory):
    """
    Itera sobre los archivos en un directorio dado y procesa los archivos FASTA encontrados.

    Args:
        directory (str): La ruta al directorio que contiene los archivos FASTA.

    Returns:
        dict: Un diccionario que contiene la información de todos los archivos FASTA en el directorio.
    """
    file_paths = os.listdir(directory)
    all_files_data = {}  # Inicializar un diccionario para almacenar los resultados
    
    # Iterar sobre cada archivo en el directorio
    for file in file_paths:
        fasta_file = os.path.join(directory, file)
        result = fasta_info_slicer(fasta_file)
        if result:  # Añadir al diccionario solo si el resultado no es None
            all_files_data.update(result)  # Actualizar el diccionario con el resultado
    
    return all_files_data

# Ejemplo de uso
# result = iterator('path/to/directory')
# print(result)
