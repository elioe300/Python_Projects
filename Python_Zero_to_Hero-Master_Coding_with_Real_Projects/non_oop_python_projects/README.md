# Python Projects - Procedural Programming (Non-OOP)

This document provides a detailed description of various Python projects developed using a procedural programming approach (without Object-Oriented Programming). Below, you will find their main features, explanations of the functions used, and usage examples.

---

## [1. Note App](./note_app.py)

### Description
A command-line application that allows users to create, view, edit, and delete notes.

### Main Functions

- **menu()**: Displays the options menu.
- **view_notes()**: Shows the content of a selected note.
- **create_note()**: Allows the creation of a new note or editing an existing one.
- **delete_note()**: Deletes a note selected by the user.

### Usage Example
```python
menu()  # Starts the interactive CLI application
```

---

## [2. File Synchronizer with Change Log](./file_synchronizer_with_change_log.py)

### Description
This project synchronizes files between two folders while maintaining a change log.

### Main Functions

- **calculate_md5(archive_route)**: Calculates the MD5 hash of a file.
- **copy_archives(source_route, backup_route)**: Copies files from a source folder to a backup folder.
- **clean_archives(source_route, backup_route)**: Deletes obsolete files in the backup folder.
- **backup_and_sync(source_route, backup_route)**: Synchronizes files between two folders.

### Usage Example
```python
backup_and_sync("C:\\path\\to\\source", "C:\\path\\to\\backup")
```

---

## [3. Downloader FASTA](./downloader_FASTA.py)

### Description
Downloads biological sequences in FASTA format from NCBI using an ID or a search term.

### Main Functions

- **ID_finder(search_term, download_route)**: Downloads a sequence by its ID.
- **NCBI_finder(search_term, download_route)**: Searches for sequences on NCBI and allows selecting IDs for download.
- **show_notification(title, message)**: Displays a system notification.

### Usage Example
```python
ID_finder("NM_001301717", "C:\\downloads")
```

---

## [4. Bioinformatic Archive Organizer](./bioinformatic_archive_organizer.py)

### Description
This script organizes files in a specified directory based on user-defined output paths and extensions.

### Main Functions

- **bioinformatics_file_organizer(route)**: Organizes files by their extension within the specified path.

### Usage Example
```python
bioinformatics_file_organizer("C:\\path\\to\\files")
```

---

## [5. Acronymizer](./acronymizer.py)

### Description
Transforms a user-provided phrase into an acronym.

### Main Functions

- **acronymizer()**: Asks the user for a phrase and generates an acronym using the first letter of each word.

### Usage Example
```python
acronym = acronymizer()
print(acronym)  # Output: 'NASA' if the input is 'National Aeronautics and Space Administration'
```

---

## [6. BMI Tracker](./bmi_tracker.py)

### Description
Calculates the Body Mass Index (BMI) and provides an interpretation.

### Main Functions

- **bmi_tracker()**: Asks the user for their height and weight, calculates the BMI, and provides an interpretation based on the result.

### Usage Example
```python
result = bmi_tracker()
print(result)
```

---

## [7. Bulk Rename Bio Files](./bulk_rename_bio_file.py)

### Description
Mass renames files in a directory with a prefix and a numbered index.

### Main Functions

- **bulk_rename(folder_path, prefix, extension)**: Renames files based on their extension in a specified directory.

### Usage Example
```python
bulk_rename('path/to/directory', 'prefix', '.txt')
```

---

## [8. CPU RAM Monitor](./CPU_RAM_monitor.py)

### Description
This script monitors CPU and RAM usage, sending notifications if values exceed certain thresholds.

### Main Functions

- **monitor_system_usage()**: Continuously monitors CPU and RAM usage, sending notifications if thresholds are exceeded.

### Usage Example
```python
monitor_system_usage()
```

---

## [9. Data Entry Automator](./data_entry_automator.py)

### Description
Automates data entry and the creation/update of a CSV file.

### Main Functions

- **data_entry_automator(input_file, output_csv)**: Converts input data into a pandas DataFrame and saves/concatenates it into a CSV file.

### Usage Example
```python
data_to_enter = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 32, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]
data_entry_automator(data_to_enter, "output_file")
```

---

## [10. Data Guardian](./data_guardian.py)

### Description
This script copies files and subdirectories from the source directory to the backup directory and deletes obsolete files in the backup directory.

### Main Functions

- **copy_archives(source_route, backup_route)**: Copies files and subdirectories from the source directory to the backup directory.
- **clean_archives(source_route, backup_route)**: Deletes files in the backup directory that no longer exist in the source directory.
- **backup_and_sync(source_route, backup_route)**: Backs up and synchronizes files between two directories.

### Usage Example
```python
backup_and_sync('path/to/source', 'path/to/backup')
```

---

## [11. FASTA Information Slicer](./fasta_information_slicer.py)

### Description
This script processes a FASTA file and extracts information about identifiers and their sequences.

### Main Functions

- **fasta_info_slicer(fasta_file)**: Processes a FASTA file and extracts information about identifiers and sequences.
- **iterator(directory)**: Iterates over files in a given directory and processes found FASTA files.

### Usage Example
```python
result = iterator('path/to/directory')
print(result)
```

---

## [12. File Renamer](./file_renamer.py)

### Description
Renames files in a specified directory using a prefix and a numbered index.

### Main Functions

- **file_rename(folder_path, prefix, extension)**: Renames files in a given directory with a prefix and a numbered index.

### Usage Example
```python
file_rename('path/to/directory', 'prefix', 'txt')
```

---

## [13. Folder Refiner](./folder_refiner.py)

### Description
This script deletes files with specific extensions in a given directory.

### Main Functions

- **folder_refiner(folder_path, extension)**: Deletes files with specific extensions in a given directory.

### Usage Example
```python
folder_refiner('path/to/directory', '.txt')
folder_refiner('path/to/directory', ['.txt', '.log'])
```

---

## [14. PDF Text Grabber](./PDFTextGrabber.py)

### Description
This script extracts text from specific pages of PDF files.

### Main Functions

- **extract_text(pdf_path, page_number)**: Extracts text from a specific page of a PDF file.
- **show_page_count(pdf_path)**: Shows the number of pages in a PDF file.
- **PDFTextGrabber()**: Interacts with the user and extracts text from a PDF file.

### Usage Example
```python
if __name__ == "__main__":
    PDFTextGrabber()
```

---

## [15. Pomodoro Timer](./pomodoro_timer.py)

### Description
This script runs a Pomodoro study cycle for 25 minutes and a break cycle for 5 minutes, sending notifications at the start and end of each cycle.

### Main Functions

- **pomodoro_timer()**: Runs the Pomodoro study cycle for 25 minutes and sends a notification at the start and end of the cycle.
- **rest_timer()**: Runs the break cycle for 5 minutes and sends a notification at the start and end of the cycle.
- **main**: Asks the user how many Pomodoro cycles they want to perform and runs the study and break cycles.

### Usage Example
```python
if __name__ == "__main__":
    cycles = int(input("Enter the number of Pomodoro cycles you want to perform: "))
    for cycle in range(cycles):
        pomodoro_timer()
        rest_timer()
```

---

## [16. Random Guessing Game](./random_guessing_game.py)

### Description
This script starts a number-guessing game. The program generates a random number, and the user has to guess it in the fewest attempts possible.

### Main Functions

- **random_guessing_game()**: Starts a number-guessing game. The user has to guess the number generated by the program.

### Usage Example
```python
random_guessing_game()
```

---
