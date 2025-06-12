import os


class Sessions():
    def __init__(self, user_data):
        self.user_data = user_data
        self.current_user = ""

    def print_head(self, text_head: str, width=35):
        print("-"*width)
        print(text_head.center(width))
        print("-"*width)

    def show_menu(self, options: dict, head):
        """Muestra menú interactivo"""

        # os.system('cls')
        while True:
            self.print_head(head)

            for i in options:
                print(i)

            print("-"*35)
            option = input("Ingrese la opción que desea: ")
            if option.isdigit():
                option = int(option) - 1
                if 0 <= option < len(options):
                    fun_option = list(options.items())[option][1]
                    fun_option()
                    return
            os.system('cls')
            print("Opción no válida")

    def main_menu(self):

        self.current_user = ""

        mm_options = {
            "1. Iniciar sesión": self.login,
            "2. Registrar usuario": self.register_user,
            "3. Salir": self.exit
        }

        mm_head = "Menú principal"
        self.show_menu(mm_options, mm_head)

    def login(self):

        os.system('cls')

        # Verifica que existan usuarios registrados
        if not len(self.user_data):
            print("No hay registros de ningun usuario")
            print("Debe registrar al menos a uno")
            self.main_menu()
            return

        l_head = "Inicio de sesión"
        self.print_head(l_head)

        user_name = input("Ingrese nombre de usuario: ")
        user_password = input("Ingrese su contraseña: ")

        if user_name not in self.user_data:
            os.system('cls')
            print("Usuario no registrado")
            self.main_menu()
            return

        if self.user_data[user_name] == user_password:
            self.current_user = user_name
            self.user_menu()
            return

        os.system('cls')
        print("Error al iniciar sesión")
        print("Inténtelo nuevamente")
        self.main_menu()

    def register_user(self):
        ru_head = "Registrando usuario"

        while True:
            os.system('cls')
            self.print_head(ru_head)
            user_name = input("Ingrese nombre de usuario a registrar:\n")
            user_password = input("Ingrese contraseña:\n")

            print("¿Está seguro que los datos son correctos?")
            print("-"*35)
            confirm = input(
                "Ingrese n para comenzar de nuevo, de lo contrario presione enter\n")
            if confirm != "n":
                self.user_data[user_name] = user_password
                break

        os.system('cls')
        print("Usuario registrado con éxito")
        self.main_menu()

    def exit(self):
        print("Cerrando sistema")
        input("presione enter para cerrar")
        os.system('exit')

    def user_menu(self):
        um_head = f"Bienvenido {self.current_user}"

        um_options = {
            "1. Realizar llamada": self.use_phone,
            "2. Enviar correo electrónico": self.send_email,
            "3. Cerrar sesión": self.logout
        }

        os.system('cls')
        self.show_menu(um_options, um_head)

    def use_phone(self):

        os.system('cls')
        self.print_head("Teléfono")

        phone_number = input("Ingrese el número al que desea llamar:\n")

        if phone_number.isdigit():
            if phone_number[0] == "9" and len(phone_number) == 9:
                print("Ha llamado al " + phone_number)
                input("Presione enter para continuar")
                self.user_menu()
                return

        print("Se ha producido un error al llamar")
        print("El número debe comenzar con 9 y tener 9 dígitos")
        input("Presione enter para continuar")
        self.user_menu()

    def send_email(self):
        os.system('cls')
        se_head = "Correo electrónico"
        self.print_head(se_head)

        correo = input("Ingrese el correo del destinatario:\n")

        if "@" not in correo:
            print("El correo debe tener al menos 1 @")
            print("Error al ingresar correo")
            input("Presione enter para continuar")
            self.user_menu()
            return

        mensaje = input("Ingrese el mensaje que desea enviar:\n")

        os.system('cls')
        self.print_head("Mensaje enviado")
        print(f"Destinatario: {correo}")
        print(f"Mensaje: {mensaje}")
        input("Presione enter para continuar")
        self.user_menu()

    def logout(self):
        os.system('cls')
        print("Se ha cerrado sesión con éxito")
        self.main_menu()

    def start(self):
        os.system('cls')
        self.main_menu()


my_users = {
    "samuel": "1111"
}

my_program = Sessions(my_users)
my_program.start()
