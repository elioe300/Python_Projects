from Bio import Entrez
import os
from plyer import notification


def mostrar_notificacion(titulo, mensaje):
    """
    Muestra una notificación en el sistema operativo.
    """
    if notification:
        notification.notify(title=titulo, message=mensaje, timeout=5)

def ID_finder(search_term, download_route):
    """
    Función para descargar secuencias de nucleótidos en formato FASTA utilizando su ID.
    """
    while True:
            # Solicitar el ID de la secuencia a descargar
        try:
            handle = Entrez.efetch(db="nucleotide", id=search_term, rettype="fasta", retmode="text")
            sequence = handle.read()
            handle.close()
        except Exception:
            print(f"Error: No se encontró el ID {search_term}. Intente con otro.\n")
            break 
        path = os.path.join(download_route, f"{search_term}.fasta")
        with open(path, "w") as file:
            file.write(sequence)
        break

def menu():
    """
    Menú principal para seleccionar opciones de descarga.
    """
    print("Bienvenido al descargador de secuencias biológicas.")
    while True:
        email = input("Introduzca un email: ").strip()
        if "@" not in email or "." not in email:  
            print("Introduzca un email válido.\n")
            continue
        else:
            Entrez.email = email
            break
    while True:
        try:
            opcion = int(input("""¿Qué es lo que desea hacer?
Teclee el número mostrado en las siguientes opciones:
1 - Introducir una ruta.
2 - Salir del menú.\n"""))
            if opcion == 1:
                download_route = input("Introduzca la ruta absoluta de dónde quiere guardar lo(s) archivo(s): ")
                if not os.path.isdir(download_route):
                    print("La ruta ingresada no existe. Intente de nuevo.\n")
                    break
                while True:
                    try:
                        opcion = int(input("""¿Qué es lo que desea hacer?
Teclee el número mostrado en las siguientes opciones:
    1 - Descargar por secuencia específica por ID.
    2 - Buscar por secuencia de NCBI.
    3 - Salir del programa.\n"""))
                        if opcion == 1:
                            search_term = input("Introduzca el ID a descargar: ").strip()
                            ID_finder(search_term, download_route)
                            mostrar_notificacion("Descarga Completada", f"Secuencia {search_term} descargada en {download_route}")
                        elif opcion == 2:
                            search_term = input("Introduzca un término a buscar en el NCBI:\n")
                            NCBI_finder(search_term, download_route)
                        elif opcion == 3:
                            print("Ha salido del programa.")
                            break
                        else:
                            print("Seleccione una opción correcta.")
                    except ValueError:
                        print("Error: Debe ingresar un número válido. Intente de nuevo.")
            elif opcion == 2:
                break
            else:
                print("Seleccione una opción correcta.")
        except ValueError:
            print("Error: Debe ingresar un número válido. Intente de nuevo.")


def NCBI_finder(search_term, download_route):
    while True:
        handle = Entrez.esearch(db = "nucleotide", term= search_term, retmax=10)
        record = Entrez.read(handle)
        handle.close()
        id_list = record["IdList"]
        if not id_list:
                print("⚠ No se encontraron resultados. Intente con otra búsqueda.\n")
                return
        print("Se encontraron los siguientes IDs:")
        for index, id in enumerate(id_list, start=1):
            print(f"{index} - {id}") # Usar '+=' para concatenar cada línea al mensajes
        choices = input("\nIngrese los números de los IDs a descargar (ej: 1,3,5) o '0' para salir: ").strip()
        
        if choices == "0":
            return

        selected_indices = [int(x) for x in choices.split(",") if x.isdigit()]
        selected_ids = [id_list[i - 1] for i in selected_indices if 1 <= i <= len(id_list)]

        if not selected_ids:
            print("Selección inválida. Intente de nuevo.")
            return
        
        print("\nDescargando secuencias seleccionadas...")
        for seq_id in selected_ids:
            ID_finder(seq_id, download_route)
        mostrar_notificacion("Descarga concluida", f"Lo(s) archivo(s) {search_term} descargada en {download_route}")
        exit_program = input("\n¿Desea descargar otra secuencia? (Y/N): ").strip().upper()
        if exit_program == "Y":
            break

        if exit_program == "N":
            print("\n👋 Saliendo del programa.")
            return  # Sale de la función correctamente
