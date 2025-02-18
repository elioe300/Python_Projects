import re

class Transaction:
    """
    Representa una transacción en la biblioteca.

    Attributes:
        book (str): El título del libro involucrado en la transacción.
        transaction_type (str): El tipo de transacción (prestado o depositado).
    """
    
    def __init__(self, book, transaction_type):
        self.book = book
        self.transaction_type = transaction_type
    

class Library:
    """
    Representa una biblioteca con un sistema de préstamos y devoluciones de libros.

    Attributes:
        accounts (dict): Un diccionario que mapea nombres de titulares a listas de libros prestados.
        inventory (list): Una lista de libros disponibles en la biblioteca.
        transactions (dict): Un diccionario que mapea nombres de titulares a listas de transacciones.
    """
    
    def __init__(self):
        self.accounts = {}
        self.inventory = ["El Principito", "1984", "Patito Feo"]
        self.transactions = {}

    def withdrawal(self, book, holder_name):
        """
        Permite al usuario retirar un libro de la biblioteca.

        Args:
            book (str): El título del libro a retirar.
            holder_name (str): El nombre del titular de la cuenta.
        """
        if book in self.inventory:
            if holder_name not in self.accounts:
                self.accounts[holder_name] = []
            self.accounts[holder_name].append(book)
            self.inventory.remove(book)
            print(f"Usted ha prestado - {book}")
            if holder_name not in self.transactions:
                self.transactions[holder_name] = []
            self.transactions[holder_name].append(Transaction(book, "prestado"))
        else:
            print("Este libro no se encuentra disponible en estos momentos, o introduzca correctamente el título. Disculpa las molestias.")
    
    def deposit(self, book, holder_name):
        """
        Permite al usuario devolver un libro a la biblioteca.

        Args:
            book (str): El título del libro a devolver.
            holder_name (str): El nombre del titular de la cuenta.
        """
        if book in self.accounts.get(holder_name, []):
            self.accounts[holder_name].remove(book)
            self.inventory.append(book)
            print(f"Usted ha depositado - {book}")
            self.transactions[holder_name].append(Transaction(book, "depositado"))
        else:
            print("Movimiento inválido, no tiene el libro a su nombre.")

    def inventorio(self):
        """
        Muestra el inventario actual de la biblioteca.
        """
        print("Estos son los libros que tiene la biblioteca:")
        for book in self.inventory:
            print(f"- {book}")
    
    def display_transactions(self, holder_name):
        """
        Muestra el historial de transacciones de un usuario.

        Args:
            holder_name (str): El nombre del titular de la cuenta.
        """
        print(f"Este es el historial del usuario {holder_name}:")
        if not self.transactions.get(holder_name):
            print("No hay transacciones registradas.")
        else:
            for linea in self.transactions[holder_name]:
                print(f"- Ha {linea.transaction_type} el libro con el título {linea.book}")

    def contenido(self, holder_name):
        """
        Muestra los libros prestados por un usuario.

        Args:
            holder_name (str): El nombre del titular de la cuenta.
        """
        print(f"\n📕 Libros de {holder_name}:")
        if not self.accounts.get(holder_name):
            print("No tiene libros prestados.")
        else:
            for libro in self.accounts[holder_name]:
                print(f" - {libro}")
        
    def create_account(self, holder_name):
        """
        Crea una nueva cuenta de usuario en la biblioteca.

        Args:
            holder_name (str): El nombre del titular de la cuenta.
        """
        if holder_name in self.accounts:
            print("Una cuenta ya ha sido creada con ese nombre.")
        else:
            print(f"Cuenta creada con éxito para {holder_name}.")
            self.accounts[holder_name] = []
            self.transactions[holder_name] = []


def menu():
    """
    Muestra el menú principal de la biblioteca y permite al usuario seleccionar opciones.
    """
    library = Library()
    print("Bienvenido a la biblioteca de Python.")
    while True:
        try:
            num = int(input("""¿Qué desea realizar?
1 - Crear una cuenta
2 - Acceder a una cuenta
3 - Salir de la biblioteca\n"""))
            if num == 1:
                nombre = input("Introduzca el nombre de la cuenta que desee crear:\n")
                library.create_account(nombre)
            elif num == 2:
                nombre = input("Introduzca el nombre de la cuenta que desee acceder:\n")
                if nombre in library.accounts:
                    print("¿Qué desea realizar?")
                    while True:
                        try:
                            print("\nSeleccione una opción")
                            opcion = int(input("""1 - Depositar libro.
2 - Prestar libro.
3 - Ver historial de transacciones.
4 - Mostrar inventario de la biblioteca.
5 - Libros a tu disposición.
6 - Salir de la cuenta.\n"""))
                            if opcion == 1:
                                print("Este es su inventario:\n")
                                library.contenido(nombre)
                                libro = input("Introduzca el libro a depositar:\n").rstrip()
                                library.deposit(libro, nombre)
                            elif opcion == 2:
                                print("Estos son los libros disponibles:\n")
                                library.inventorio()
                                libro = input("Introduzca el libro a retirar:\n").rstrip()
                                library.withdrawal(libro, nombre)
                            elif opcion == 3:
                                library.display_transactions(nombre)
                                input("Presione ENTER para continuar...\n")
                            elif opcion == 4:
                                library.inventorio()
                                input("Presione ENTER para continuar...\n")
                            elif opcion == 5:
                                library.contenido(nombre)
                                input("Presione ENTER para continuar...\n")
                            elif opcion == 6:
                                break
                            else:
                                print("Introduzca un número válido.\n")
                        except ValueError:
                            print("No se ha introducido un número.\n")
                else:
                    print("No hay ninguna cuenta registrada a ese nombre, introduzca correctamente su nombre o cree una nueva cuenta\n")
            elif num == 3:
                decision = input("¿Está seguro de que quiere salir de la biblioteca?\nY or N\n").strip().upper()
                if decision == "Y":
                    break
            else:
                print("Seleccione una opción válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")