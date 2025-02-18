# Proyectos de Python - Programación Procedural (Non-OOP)

Este documento proporciona una descripción detallada de varios proyectos desarrollados en Python que siguen un enfoque procedural (sin Programación Orientada a Objetos). A continuación, se presentan sus funcionalidades principales, explicaciones sobre las funciones utilizadas y ejemplos de uso.

---

## [1. Note App](./note_app.py)

### Descripción
Una aplicación de línea de comandos que permite a los usuarios crear, ver, editar y eliminar notas.

### Funciones principales

- **menu()**: Muestra el menú de opciones.
- **view_notes()**: Muestra el contenido de una nota seleccionada.
- **create_note()**: Permite crear una nueva nota o editar una existente.
- **delete_note()**: Elimina una nota seleccionada por el usuario.

### Ejemplo de uso
```python
menu() # Inicia la aplicación interactiva en CLI
```

---

## [2. File Synchronizer with Change Log](./file_synchornizer_with_change_log.py)

### Descripción
Este proyecto permite sincronizar archivos entre dos carpetas, manteniendo un registro de los cambios en un archivo log.

### Funciones principales

- **calculate_md5(archive_route)**: Calcula el hash MD5 de un archivo.
- **copy_archives(source_route, backup_route)**: Copia archivos desde una carpeta de origen a una de respaldo.
- **clean_archives(source_route, backup_route)**: Elimina archivos obsoletos en la carpeta de respaldo.
- **backup_and_sync(source_route, backup_route)**: Sincroniza archivos entre dos carpetas.

### Ejemplo de uso
```python
backup_and_sync("C:\\ruta\\origen", "C:\\ruta\\respaldo")
```

---

## [3. Downloader FASTA](./downloader_FASTA.py)

### Descripción
Descarga secuencias biológicas en formato FASTA desde NCBI utilizando un ID o un término de búsqueda.

### Funciones principales

- **ID_finder(search_term, download_route)**: Descarga una secuencia por su ID.
- **NCBI_finder(search_term, download_route)**: Busca secuencias en NCBI y permite seleccionar IDs para descargar.
- **mostrar_notificacion(titulo, mensaje)**: Muestra una notificación en el sistema operativo.

### Ejemplo de uso
```python
ID_finder("NM_001301717", "C:\\ruta\\descargas")
```

---

## [4. Bioinformatic Archive Organizer](./bioinformatic_archive_organizer.py)

### Descripción
Organiza archivos en carpetas según su extensión dentro de un directorio.

### Funciones principales

- **bioinformatics_file_organizer(route)**: Organiza archivos según su extensión dentro de la ruta especificada.

### Ejemplo de uso
```python
bioinformatics_file_organizer("C:\\ruta\\archivos")
```

---

## [5. Acronymizer](./acronymizer.py)

### Descripción
Transforma una frase dada por el usuario en un acrónimo.

### Funciones principales

- **acronymizer()**: Solicita una frase al usuario y genera un acrónimo tomando la primera letra de cada palabra.

### Ejemplo de uso
```python
acronym = acronymizer()
print(acronym) # Output: 'NASA' si la entrada es 'National Aeronautics and Space Administration'
```

---

## [6. BMI Tracker](./bmi_tracker.py)

### Descripción
Calcula el Índice de Masa Corporal (BMI) y proporciona una interpretación.

### Funciones principales

- **bmi_tracker()**: Solicita al usuario su altura y peso, calcula el BMI y devuelve una interpretación basada en el resultado.

### Ejemplo de uso
```python
resultado = bmi_tracker()
print(resultado)
```

---

## [7. Bulk Rename Bio Files](./bulk_rename_bio_file.py)

### Descripción
Renombra en masa archivos dentro de un directorio con un prefijo y un índice numerado.

### Funciones principales

- **bulk_rename(folder_path, prefix, extension)**: Renombra archivos según su extensión dentro de un directorio especificado.

### Ejemplo de uso
```python
bulk_rename('ruta/al/directorio', 'prefijo', '.txt')
```

---

# [10. CPU RAM Monitor](./CPU_RAM_monitor.py)

## Visión General
Este script monitorea el uso del CPU y la RAM, y envía notificaciones si los valores superan ciertos umbrales.

---

## Funciones

### Función: monitor_system_usage

#### Descripción
- **monitor_system_usage**: Monitorea continuamente el uso del CPU y la RAM, enviando notificaciones si los valores superan ciertos umbrales.
  ```python
  monitor_system_usage()
  ```

---

# [11. Data Entry Automator](./data_entry_automator.py)

## Visión General
Este script automatiza la entrada de datos y la creación/actualización de un archivo CSV.

---

## Funciones

### Función: data_entry_automator

#### Descripción
- **data_entry_automator**: Convierte datos de entrada en un DataFrame de pandas y los guarda/concatena en un archivo CSV.
  ```python
  data_to_enter = [
      {"name": "Alice", "age": 30, "city": "New York"},
      {"name": "Bob", "age": 32, "city": "San Francisco"},
      {"name": "Charlie", "age": 35, "city": "Los Angeles"}
  ]
  data_entry_automator(data_to_enter, "output_file")
  ```

---

# [12. Data Guardian](./data_guardian.py)

## Visión General
Este script copia archivos y subdirectorios desde el directorio de origen al directorio de respaldo y elimina archivos obsoletos en el directorio de respaldo.

---

## Funciones

### Función: copy_archives

#### Descripción
- **copy_archives**: Copia archivos y subdirectorios desde el directorio de origen al directorio de respaldo.

### Función: clean_archives

#### Descripción
- **clean_archives**: Elimina archivos en el directorio de respaldo que ya no existen en el directorio de origen.

### Función: backup_and_sync

#### Descripción
- **backup_and_sync**: Realiza una copia de seguridad y sincronización de archivos entre dos directorios.
  ```python
  backup_and_sync('ruta/al/directorio/origen', 'ruta/al/directorio/respaldo')
  ```

---

# [13. FASTA Information Slicer](./fasta_information_slicer.py)

## Visión General
Este script procesa un archivo FASTA y extrae información sobre identificadores y sus secuencias.

---

## Funciones

### Función: fasta_info_slicer

#### Descripción
- **fasta_info_slicer**: Procesa un archivo FASTA y extrae información sobre identificadores y secuencias.

### Función: iterator

#### Descripción
- **iterator**: Itera sobre los archivos en un directorio dado y procesa los archivos FASTA encontrados.
  ```python
  resultado = iterator('ruta/al/directorio')
  print(resultado)
  ```

---

# [14. File Renamer](./file_renamer.py)

## Visión General
Este script renombra archivos en un directorio especificado usando un prefijo y un índice numerado.

---

## Funciones

### Función: file_rename

#### Descripción
- **file_rename**: Renombra archivos en un directorio dado con un prefijo y un índice numerado.
  ```python
  file_rename('ruta/al/directorio', 'prefijo', 'txt')
  ```

---

# [15. Folder Refiner](./folder_refiner.py)

## Visión General
Este script elimina archivos con extensiones específicas en un directorio dado.

---

## Funciones

### Función: folder_refiner

#### Descripción
- **folder_refiner**: Elimina archivos con extensiones específicas en un directorio dado.
  ```python
  folder_refiner('ruta/al/directorio', '.txt')
  folder_refiner('ruta/al/directorio', ['.txt', '.log'])
  ```

---

# [16. PDF Text Grabber](./PDFTextGrabber.py)

## Visión General
Este script extrae el texto de páginas específicas de archivos PDF.

---

## Funciones

### Función: extract_text

#### Descripción
- **extract_text**: Extrae el texto de una página específica de un archivo PDF.

### Función: show_page_count

#### Descripción
- **show_page_count**: Muestra el número de páginas de un archivo PDF.
 
### Función: PDFTextGrabber

#### Descripción
- **PDFTextGrabber**: Interactúa con el usuario y extrae texto de un archivo PDF.
  ```python
  if __name__ == "__main__":
      PDFTextGrabber()
  ```

---

# [17. Pomodoro Timer](./pomodoro_timer.py)

## Visión General
Este script ejecuta el ciclo de estudio Pomodoro durante 25 minutos y el ciclo de descanso durante 5 minutos, enviando notificaciones al inicio y al final de cada ciclo.

---

## Funciones

### Función: pomodoro_timer

#### Descripción
- **pomodoro_timer**: Ejecuta el ciclo de estudio Pomodoro durante 25 minutos y envía una notificación al inicio y al final del ciclo.

### Función: rest_timer

#### Descripción
- **rest_timer**: Ejecuta el ciclo de descanso durante 5 minutos y envía una notificación al inicio y al final del ciclo.

### Función: main

#### Descripción
- **main**: Pregunta al usuario la cantidad de ciclos Pomodoro que quiere realizar y ejecuta los ciclos de estudio y descanso.
  ```python
  if __name__ == "__main__":
      cycles = int(input("Introduzca la cantidad de ciclos pomodoro que quiera realizar: "))
      for cycle in range(cycles):
          pomodoro_timer()
          rest_timer()
  ```
  
---

# [18. Random Guessing Game](./random_guessing_game.py)

## Visión General
Este script inicia un juego de adivinanza de números. El programa genera un número aleatorio y el usuario debe adivinarlo en el menor número de intentos posibles.

---

## Funciones

### Función: random_guessing_game

#### Descripción
- **random_guessing_game**: Inicia un juego de adivinanza de números. El usuario debe adivinar el número generado por el programa.
  ```python
  random_guessing_game()
  ```

---

