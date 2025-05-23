"""Cajero automático"""

import os
import json


class SamCash():

    """Clase cajero automático"""

    def __init__(self, route_user_data):
        # Ruta de json con información de usuarios
        self.route_user_data = route_user_data
        self.user_data = {}                     # Variable que almacenará los datos del json
        self.user = ""                          # Nombre del usuario actual
        self.load_data_users()                  # Carga los datos de usuario

    def load_data_users(self):
        """Carga datos de usuarios desde archivo json"""

        with open(self.route_user_data, "r", encoding="utf-8") as data:
            self.user_data = json.load(data)

    def save_data_user(self):
        """Actualiza datos de json con new_data"""

        with open(self.route_user_data, "w", encoding="utf-8") as data:
            json.dump(self.user_data, data, indent=4)

    def login(self):
        """Función para login de usuario"""

        # Limpia la consola
        os.system('cls')

        while True:

            # Carga datos de usuarios e imprime encabezado
            self.load_data_users()
            login_head = "Bienvenido a Sam Cash"
            self.print_head(login_head)

            # Pide datos al usuario
            user = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña de 4 dígitos: ")

            # Limpia la consola
            os.system('cls')

            # Si el usuario no es válido reinicia el bucle
            if user not in self.user_data:
                print("Usuario incorrecto")
                continue

            # Actualiza el valor del usuario actual
            self.user = user

            # Verifica si la contraseña está bloqueada
            if not self.user_data[user]["active"]:
                print("Su contraseña está bloqueada")
                print("Debe comunicarse con servicio al cliente")
                continue

            # Verifica que la contraseña sea de 4 dígitos
            if self.check_password(password):

                # Si la contraseña es correcta termina el bucle
                if password == self.user_data[user]["pin"]:
                    self.user_data[user]["attempts"] = 3
                    self.save_data_user()
                    return True

            # Resta un intento e informa cuantos intentos quedan
            print("Contraseña incorrecta")
            self.user_data[user]["attempts"] -= 1

            if self.user_data[user]["attempts"] > 0:
                print(f'Quedan {self.user_data[user]["attempts"]} intentos')
            else:
                print("Ya no quedan intentos")
                self.user_data[user]["active"] = False

            # Actualiza los datos
            self.save_data_user()

    def check_password(self, password: str):
        """Valida contraseña de 4 dígitos"""

        if password.isdigit() and len(password) == 4:
            return True

        # Retorna falso si la contraseña tiene errores
        return False

    def print_head(self, text_head):
        """Imprime el encabezado de cada menú"""

        left = int((44-len(text_head))/2)
        right = 42 - len(text_head) - left
        print("┌" + "─" * 42 + "┐")
        print("│" + " " * left + text_head + " " * right + "│")
        print("└" + "─" * 42 + "┘")

    def show_menu(self, options: dict, head=""):
        """Imprime en pantalla las opciones disponibles en el diccionario options
        y permite ejecutar las funciones asociadas a cada opción"""

        while True:

            # Imprime encabezado
            self.print_head(head)

            # Lista en consola las opciones disponibles
            for option in options.items():
                print(option[0])

            # Consulta al usuario la opción que desea
            try:
                print("─"*43)
                op = int(input("Ingrese el número de la opción que desea: "))
                op -= 1

                os.system('cls')

                # Si la opción es válida ejecuta la función asociada
                if 0 <= op < len(options):
                    fun_op = list(options.items())[op][1]
                    fun_op()
                    break

                print("La opción ingresada no es válida")
                print(f"Ingrese números solo entre 1 y {len(options)}")

            except ValueError:
                os.system('cls')
                print(f"Ingrese números solo entre 1 y {len(options)}")

    def show_main_menu(self):
        """Menú principal luego del login"""

        # Limpia la consola y declara las opciones disponibles
        os.system('cls')
        mm_options = {
            "1. Cuenta corriente": self.show_debit_card_menu,
            "2. Cambiar contraseña": self.change_password,
            "3. Salir": self.exit,
        }

        # Imprime en pantalla las opciones disponibles
        smm_head = "Menú Principal"
        self.show_menu(mm_options, smm_head)

    def change_password(self):
        """Cambiar contraseña"""

        # Declara las opciones disponibles
        cp_option = {
            "1. Volver": self.show_main_menu,
            "2. Salir": self.exit
        }

        cp_head = "Cambio de PIN"

        while True:
            # Imprime encabezado
            self.print_head(cp_head)

            # Verifica que el pin ingresado tenga solo 4 dígitos
            new_pin = input(
                "Ingrese una nueva contraseña de 4\n")
            if self.check_password(new_pin):
                break

            os.system('cls')
            print("Error al cambiar contraseña")
            print("Ingrese solo 4 dígitos entre 0 y 9")

        # Actualiza el valor de la contraseña en el json
        self.user_data[self.user]["pin"] = new_pin
        self.save_data_user()

        # Confirma el cambio de contraseña e imprime opciones disponibles
        os.system('cls')
        print("Contraseña modificada con éxito")
        self.show_menu(cp_option, cp_head)

    def show_debit_card_menu(self):
        """Ingresa a menú de tarjeta de débito"""

        # Limpia la consola y declara las opciones disponibles
        os.system('cls')
        dc_options = {
            "1. Consultar saldo": self.check_debit_balance,
            "2. Giro": self.show_debit_withdraw_menu,
            "3. Depósito": self.debit_deposit,
            "4. Atrás": self.show_main_menu,
            "5. Salir": self.exit
        }

        # Imprime en consola las opciones disponibles
        sdcm_head = "Cuenta Corriente"
        self.show_menu(dc_options, sdcm_head)

    def check_debit_balance(self):
        "Muestra saldo en cuenta corriente"

        # Declara opciones disponibles
        ch_option = {
            "1. Volver": self.show_debit_card_menu,
            "2. Salir": self.exit
        }

        # Carga datos actualizado e muestra saldo
        self.load_data_users()
        balance = self.user_data[self.user]["debit_amount"]

        # Imprime opciones disponibles
        cdb_head = f"Saldo: {balance}"
        self.show_menu(ch_option, cdb_head)

    def show_debit_withdraw_menu(self):
        """Retiro cuenta corriente"""

        # Declara opciones disponibles
        # Envuelve funciones que requieren un argumento para ser ejecutadas
        bd_options = {
            "1. 10.000": lambda: self.debit_withdraw(10000),
            "2. 20.000": lambda: self.debit_withdraw(20000),
            "3. 50.000": lambda: self.debit_withdraw(50000),
            "4. 100.000": lambda: self.debit_withdraw(100000),
            "5. 200.000": lambda: self.debit_withdraw(200000),
            "6. Otro monto": lambda: self.debit_withdraw(self.enter_amount()),
            "7. Volver": self.show_debit_card_menu,
            "8. Salir": self.exit,
        }

        # Imprime opciones disponibles
        sdwm_head = "Retiro Cuenta Corriente"
        self.show_menu(bd_options, sdwm_head)

    def debit_withdraw(self, amount):
        """Retiro de cuenta corriente"""

        # Declara opciones disponibles
        dw_option = {
            "1. Retirar otro monto": self.show_debit_withdraw_menu,
            "2. Volver": self.show_debit_card_menu,
            "3. Salir": self.exit
        }

        # Carga datos actualizados y limpia la consola
        self.load_data_users()
        os.system('cls')

        # Verifica que el retiro sea posible
        if self.user_data[self.user]["debit_amount"] >= amount:

            # Actualiza datos y confirma transacción
            self.user_data[self.user]["debit_amount"] -= amount
            self.save_data_user()
            print(f"Ha retirado {amount}")
            print(
                f'Su nuevo saldo es: {self.user_data[self.user]["debit_amount"]}')

        # Informa en el caso de que el retiro no se pueda ejecutar
        else:
            print("Su saldo es insuficiente")
            print(
                f'El monto máximo de retiro es de {self.user_data[self.user]["debit_amount"]}')

        # Imprime las opciones disponibles
        dw_head = "Retiro Cuenta Corriente"
        self.show_menu(dw_option, dw_head)

    def debit_deposit(self):
        " Realiza depósitos a la cuenta corriente"

        # Declara opciones disponibles
        dd_options = {
            "1. Volver": self.show_debit_card_menu,
            "2. Salir": self.exit,
        }

        # Verifica monto
        deposit_amount = self.enter_amount()

        # Actualiza datos del usuario
        self.load_data_users()
        self.user_data[self.user]["debit_amount"] += deposit_amount
        self.save_data_user()

        # Confirma transacción y muestra opciones disponibles
        os.system('cls')
        print("Depósito realizado con éxito")
        print(
            f'Su nuevo saldo es: {self.user_data[self.user]["debit_amount"]}')
        dd_head = "Depósito Cuenta Corriente"
        self.show_menu(dd_options, dd_head)

    def enter_amount(self):
        """Ingresar monto específico"""

        amount = 0
        while True:
            self.print_head("Ingrese monto")
            amount = input()

            # Verifica que el monto ingresado sea mayor a cero
            if amount.isdigit() and int(amount) >= 0:
                break

            os.system('cls')
            print("Ingrese solo números")

        # Retorna el monto ingresado
        return int(amount)

    def exit(self):
        """Cierra el programa"""
        print("Cerrando sesión y sistema")
        input("Presiona enter para cerrar la consola")
        os.system('exit')
        # sys.exit()

    def start_atm(self):
        """Ingresa a login y luego muestra menú principal"""

        os.system('cls')
        if self.login():
            self.show_main_menu()


# Ruta json
# SAM_CASH_USERS = "/sam_cash_users.json"

SAM_CASH_USERS = "C:/Users/samue/Desktop/Github_MadoScientista/Python/Ejercicios_Basicos/cajero_automatico/sam_cash_users.json"

cajero = SamCash(SAM_CASH_USERS)

cajero.start_atm()
