# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800

import os


class Delivery():
    def __init__(self):
        self.bill_amount = 0
        self.bill_amount_discount = 0
        self.n_rolls = 0
        self.rolls_select = {}
        self.discount_code_user = ""
        self.in_order = True
        self.width_head = 46
        self.rolls = {
            "Pikachu Roll": 4500,
            "Otaku Roll": 5000,
            "Pulpo Venenoso Roll": 5200,
            "Anguila Eléctrica": 4800,
            "Profe roll": 2000,
            "Sam Roll": 3600
        }
        self.discount_codes = {
            "soyotaku": 10,
            "programación": 20,
        }

    def print_head(self, text_head: str):
        """Imprime el encabezado de cada menú"""

        print("┌" + "─" * (self.width_head-2) + "┐")
        print("│"+text_head.center(self.width_head-2)+"│")
        print("└" + "─" * (self.width_head-2) + "┘")

    def show_menu(self, menu_display: list, menu_comand: dict, head):
        "Imprime opciones del menú"

        while True:
            self.print_head(head)

            for menu_options in menu_display:
                print(menu_options)

            print("─"*self.width_head)
            option = input("Ingrese la opción que desea\n")

            if option in menu_comand:
                fun_option = menu_comand[option]
                fun_option()
                break
            os.system('cls')
            print("Opción no válida")

    def show_sushi_options(self):
        os.system('cls')
        self.in_order = True

        options_display = []
        option_command = {}
        for i, (name, price) in enumerate(self.rolls.items()):
            options_display.append(f'{i+1}. {name} ${price}')
            option_command[str(
                i+1)] = lambda n=name, p=price: self.add_sushi(n, p)

        options_display.append("Ingresa x para terminar el pedido")
        option_command['x'] = self.finish_order

        so_head = "Menú sushi"
        while self.in_order:
            self.show_menu(options_display, option_command, so_head)
            os.system('cls')
            print(
                f"Acualmente lleva {self.n_rolls} rolls. Total: {self.bill_amount}")

    def add_sushi(self, name, price):

        self.bill_amount += price
        self.n_rolls += 1

        if name not in self.rolls_select:
            self.rolls_select[name] = 1
        else:
            self.rolls_select[name] += 1

    def finish_order(self):
        self.in_order = False
        self.discount()

    def discount(self):
        os.system('cls')

        d_options = [
            "1. Si tengo código de descuento",
            "2. No tengo código de descuento",
            "3. Seguir comprando"
        ]
        d_command = {
            "1": self.check_code,
            "2": self.bill,
            "x": self.show_sushi_options
        }
        d_head = "¿Código de descuento?"
        self.show_menu(d_options, d_command, d_head)

    def check_code(self):

        while True:
            discount_code = input(
                "Ingrese su código de descuento (Ingresa x para seguir comprando): ")

            if discount_code in self.discount_codes:
                self.discount_code_user = discount_code
                self.bill_amount_discount = self.bill_amount * \
                    self.discount_codes[self.discount_code_user]/100
                return
            if discount_code == "x":
                self.in_order = True
                self.show_sushi_options()
                return

            os.system('cls')
            print("Código no válido")

    def bill(self):

        os.system('cls')
        b_head = "Boleta Sam Sushi"
        self.print_head(b_head)

        print(f"Total productos: {self.n_rolls}")

        for y, x in self.rolls_select.items():
            print(f"{x} {y}")

        print("─"*self.width_head)
        print(f"Subtotal a pagar: ${self.bill_amount}")
        print(
            f"Descuento por código: {self.discount_codes.get(self.discount_code_user, 0)} %")
        print(f"Monto descuento: ${self.bill_amount_discount}")
        print("─"*self.width_head)
        print(f"TOTAL: {self.bill_amount-self.bill_amount_discount}")
        print("─"*self.width_head)

    def reset_order(self):
        self.bill_amount = 0
        self.bill_amount_discount = 0
        self.n_rolls = 0
        self.rolls_select = {}
        self.discount_code_user = ""
        self.in_order = True

    def start_delivery(self):
        os.system('cls')
        self.show_sushi_options()
        self.bill()

        restart = input(
            "Si desea realizar otro pedido ingrese 1\nIngrese cualquier otro valor para terminar\n")
        if restart == "1":
            self.reset_order()
            self.start_delivery()
            return

        print("Gracias por comprar en Sushi Sam")


my_delivery = Delivery()
my_delivery.start_delivery()
