class Transaction:
    """
    Clase que representa una transacción bancaria.
    """
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

class Account:
    """
    Clase que representa una cuenta bancaria.
    """
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        """
        Método para depositar dinero en la cuenta.
        """
        if amount > 0:
            self.transactions.append(Transaction(amount, "Depósito"))
            self.balance += amount
            print(f"Depósito de {amount}€ exitoso. Nuevo balance: {self.balance}€")
        else:
            print("Cantidad inválida.")

    def withdraw(self, amount):
        """
        Método para retirar dinero de la cuenta.
        """
        if (self.balance - amount) >= 0:
            self.transactions.append(Transaction(amount, "Retiro"))
            self.balance -= amount
            print(f"Retiro de {amount}€ exitoso. Nuevo balance: {self.balance}€")
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")
    
    def display_transactions(self):
        """
        Método para mostrar el historial de transacciones.
        """
        for transaction in self.transactions:
            print(f"{transaction.amount}€ - {transaction.transaction_type}")
    
    def display_balance(self):
        """
        Método para mostrar el balance actual de la cuenta.
        """
        print(f"Balance actual para la cuenta de {self.holder_name} ({self.account_number}): {self.balance}€")

class Bank:
    """
    Clase que representa un banco.
    """
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, holder_name, initial_balance=0):
        """
        Método para crear una nueva cuenta bancaria.
        """
        if account_number not in self.accounts:
            account = Account(account_number, holder_name, initial_balance)
            self.accounts[account_number] = account
            print(f"Cuenta creada exitosamente para {holder_name}. Número de cuenta: {account_number}")
        else:
            print("Ya existe una cuenta con ese número.")
            
    def get_account(self, account_number):
        """
        Método para obtener una cuenta bancaria existente.
        """
        return self.accounts.get(account_number)

def menu():
    """
    Función principal para mostrar el menú del sistema bancario y manejar las opciones del usuario.
    """
    bank = Bank()
    print("Bienvenido al sistema bancario de Python.")
    try:
        while True:
            num = int(input("""Seleccione una opción:
1 - Crear una cuenta.
2 - Acceder a una cuenta existente.
3 - Salir del sistema\n"""))
            if num == 1:
                account_number = int(input("Introduzca el número de cuenta: "))
                holder_name = input("Introduzca el titular de la cuenta: ")
                balance = float(input("Introduzca el balance: "))
                bank.create_account(account_number, holder_name, balance)
            elif num == 2:
                account_number = int(input("Introduzca el número de cuenta: "))
                account = bank.get_account(account_number)
                if account:
                    print("¿Qué desea realizar? Seleccione una opción:")
                    while True:
                        try:
                            option = int(input("""1 - Depositar dinero.
2 - Retirar dinero.
3 - Ver historial de transacciones.
4 - Mostrar saldo.
5 - Salir de la cuenta.\n"""))
                            if option == 1:
                                amount = float(input("Introduzca la cantidad a depositar: "))
                                account.deposit(amount)
                            elif option == 2:
                                amount = float(input("Introduzca la cantidad a retirar: "))
                                account.withdraw(amount)
                            elif option == 3:
                                account.display_transactions()
                            elif option == 4:
                                account.display_balance()
                            elif option == 5:
                                break
                            else:
                                print("Introduzca un número válido.")
                        except ValueError:
                            print("No se ha introducido un número.")
                else:
                    print("No existe una cuenta con ese número, por favor cree una nueva cuenta.\n")
            elif num == 3:
                decision = input("¿Estás seguro de que quieres salir del banco?\nY o N\n").strip().upper()
                if decision == "Y":
                    break
                else:
                    pass
    except ValueError:
        print("Por favor, ingrese un número válido.")

menu()
