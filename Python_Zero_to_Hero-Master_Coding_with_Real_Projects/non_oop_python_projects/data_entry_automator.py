import pandas as pd
import os

def data_entry_automator(input_file, output_csv):
    """
    Automatiza la entrada de datos y la creación/actualización de un archivo CSV.

    La función convierte los datos de entrada en un DataFrame de pandas y guarda/concatena
    los datos en un archivo CSV en la ruta especificada.

    Args:
        input_file (list): Lista de diccionarios con los datos a introducir.
        output_csv (str): Nombre del archivo CSV de salida (sin la extensión).

    Returns:
        None: Esta función no devuelve ningún valor.
    """
    # Construir la ruta completa del archivo CSV
    rute = os.path.join(os.getcwd(), f"{output_csv}.csv")
    
    try:
        # Verificar si el archivo CSV ya existe
        if not os.path.exists(rute):
            # Crear un nuevo DataFrame y guardarlo en un archivo CSV
            new_dataframe = pd.DataFrame(input_file)
            new_dataframe.to_csv(rute, index=False)
            print("¡Se han transformado tus datos a CSV!")
        else:
            # Manejar el caso en el que el archivo CSV ya existe
            try:
                election = input("Ya existe este archivo, ¿desea concatenarlo?\nY or N\n").strip().upper()
                if election == "Y":
                    # Leer el archivo CSV existente y concatenar los nuevos datos
                    existing_csv = pd.read_csv(rute)
                    existing_dataframe = pd.DataFrame(input_file)
                    concat_csv = pd.concat([existing_csv, existing_dataframe], ignore_index=True)
                    concat_csv.to_csv(rute, index=False)
                    print("¡Se han concatenado tus datos al existente CSV!")
                elif election == "N":
                    print("Ha deseado no concatenar el existente CSV.")
                else:
                    print("Elección no válida. Por favor, introduzca Y o N.")
            except Exception as e:
                print("Se ha detectado un error al procesar su elección.")
                print(str(e))
    except Exception:
        print("Se ha detectado un error, inténtelo de nuevo.")

# Ejemplo de uso:
data_to_enter = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 32, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

# Llamada a la función con los datos de ejemplo
data_entry_automator(data_to_enter, "output_file")
