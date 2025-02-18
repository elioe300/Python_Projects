import PyPDF2
import os

def extract_text(pdf_path, page_number):
    """
    Extrae el texto de una página específica de un archivo PDF.

    Args:
        pdf_path (str): La ruta del archivo PDF.
        page_number (int): El número de la página de la que se desea extraer el texto.

    Returns:
        str: El texto extraído de la página, o un mensaje de error si no se pudo extraer el texto.
    """
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        page = pdf_reader.pages[page_number - 1]
    text = page.extract_text()
    return text if text else "No se pudo extraer texto de esta página."

def show_page_count(pdf_path):
    """
    Muestra el número de páginas de un archivo PDF.

    Args:
        pdf_path (str): La ruta del archivo PDF.

    Returns:
        int: El número de páginas del archivo PDF.
    """
    file_name = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        page_count = len(pdf_reader.pages)
        print(f"El archivo {file_name} tiene {page_count} páginas.")
    return page_count

def PDFTextGrabber():
    """
    Función principal para interactuar con el usuario y extraer texto de un archivo PDF.
    """
    try:
        pdf_path = input("Introduzca la ruta absoluta del PDF a leer:")
        if os.path.exists(pdf_path) and os.path.isfile(pdf_path):
            try:
                pages = show_page_count(pdf_path)
                page_number = int(input(f"Introduzca un número entre [1 - {pages}].\n"))
                if 1 <= page_number <= pages:
                    text = extract_text(pdf_path, page_number)
                    print(f"A continuación se va a imprimir el texto extraído:\n{text}")
                else:
                    print("Número de página fuera de rango, inténtelo de nuevo.")
            except ValueError:
                print("Valor no válido, inténtelo de nuevo.")
        else:
            print("No existe la ruta, introduzca una correcta.")
    except Exception as e:
        print(f"Error {e}, inténtelo de nuevo.")

if __name__ == "__main__":
    PDFTextGrabber()
