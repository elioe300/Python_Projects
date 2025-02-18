# Proyectos de Python Orientado a Objetos (OOP)  

Este documento proporciona una descripción detallada de dos proyectos desarrollados con Programación Orientada a Objetos en Python: **Sistema de Biblioteca** y **Sistema Bancario**.  

---

## [1. Sistema de Biblioteca](./biblioteca.py) 

### Descripción  
Este proyecto simula el funcionamiento de una biblioteca, permitiendo a los usuarios **retirar y devolver libros**, así como gestionar cuentas y transacciones.  

### Clases y Métodos  

#### **Clase `Transaction`**  
Representa una transacción de préstamo o devolución de un libro.  
- **Atributos:**  
  - `book` (str): Título del libro.  
  - `transaction_type` (str): Tipo de transacción ("prestado" o "depositado").  
- **Métodos:**  
  - `__init__(self, book, transaction_type)`: Constructor de la clase.  

#### **Clase `Library`**  
Representa la biblioteca con un sistema de préstamos y devoluciones.  
- **Atributos:**  
  - `accounts` (dict): Diccionario de usuarios y sus libros prestados.  
  - `inventory` (list): Lista de libros disponibles.  
  - `transactions` (dict): Historial de transacciones de cada usuario.  
- **Métodos:**  
  - `withdrawal(self, book, holder_name)`: Retira un libro de la biblioteca.  
  - `deposit(self, book, holder_name)`: Devuelve un libro a la biblioteca.  
  - `inventorio(self)`: Muestra el inventario disponible.  
  - `display_transactions(self, holder_name)`: Muestra el historial de transacciones de un usuario.  
  - `contenido(self, holder_name)`: Lista los libros prestados a un usuario.  
  - `create_account(self, holder_name)`: Crea una cuenta de usuario.  

#### **Función `menu()`**  
Permite la interacción del usuario con la biblioteca, incluyendo:  
1. Creación de cuenta.  
2. Acceso a una cuenta existente.  
3. Préstamo y devolución de libros.  
4. Consulta de inventario.  

---

## [2. Sistema Bancario](./sistema_bancario.py)

### Descripción  
Este proyecto simula un sistema bancario en Python, donde los usuarios pueden **crear cuentas, realizar depósitos y retiros, y consultar su historial de transacciones**.  

### Clases y Métodos  

#### **Clase `Transaction`**  
Representa una transacción bancaria.  
- **Atributos:**  
  - `amount` (float): Cantidad de la transacción.  
  - `transaction_type` (str): Tipo de transacción ("Depósito" o "Retiro").  
- **Métodos:**  
  - `__init__(self, amount, transaction_type)`: Constructor de la clase.  

#### **Clase `Account`**  
Representa una cuenta bancaria.  
- **Atributos:**  
  - `account_number` (int): Número de cuenta.  
  - `holder_name` (str): Nombre del titular.  
  - `balance` (float): Saldo de la cuenta.  
  - `transactions` (list): Lista de transacciones.  
- **Métodos:**  
  - `deposit(self, amount)`: Deposita dinero en la cuenta.  
  - `withdraw(self, amount)`: Retira dinero de la cuenta.  
  - `display_transactions(self)`: Muestra el historial de transacciones.  
  - `display_balance(self)`: Muestra el saldo de la cuenta.  

#### **Clase `Bank`**  
Administra múltiples cuentas bancarias.  
- **Atributos:**  
  - `accounts` (dict): Diccionario de cuentas bancarias.  
- **Métodos:**  
  - `create_account(self, account_number, holder_name, initial_balance=0)`: Crea una nueva cuenta.  
  - `get_account(self, account_number)`: Obtiene una cuenta existente.  

#### **Función `menu()`**  
Permite la interacción del usuario con el banco, incluyendo:  
1. Creación de cuenta.  
2. Acceso a una cuenta existente.  
3. Depósitos y retiros.  
4. Consulta de saldo.

 ---
