# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800

import os 
from copy import copy

class Delivery():
    def __init__(self):
        self.bill_amount = 0
        self.bill_amount_discount = 0
        self.n_rolls = 0
        self.rolls_select = {}
        self.discount_code_user = ""
        self.rolls ={
            "Pikachu Roll": 4500,
            "Otaku Roll": 5000,
            "Pulpo Venoso Roll": 5200,
            "Anguila Eléctrica": 4800,
            "Profe roll": 2000,
            "Sam Roll": 3600
        }
        self.order = True
        self.discount_codes = {
            "soyotaku": 10
        }

    def print_head(self, text_head):
        """Imprime el encabezado de cada menú"""

        left = int((44-len(text_head))/2)
        right = 42 - len(text_head) - left
        print("┌" + "─" * 42 + "┐")
        print("│" + " " * left + text_head + " " * right + "│")
        print("└" + "─" * 42 + "┘")

    def show_menu(self, menu:dict, head):
        "Imprime opciones del menú"


        while True:
            self.print_head(head)

            for option_menu in menu.items():
                print(option_menu[0])

            try:
                option = int(input("Ingrese el número del roll que desea agergar\n"))
                option -= 1

                if 0 <= option < len(menu):
                    fun_option = list(menu.items())[option][1]
                    fun_option()
                    break

            except ValueError:
                os.system('cls')
                print("Opción no válida")
                
            print(f"Ingrese solo números entre 1 y {len(menu)}")

    def sushi_options(self):
        rolls = list(self.rolls.items())

        so_options = {}

        for i, option in enumerate(rolls):
    
            so_options[f'{i+1}. {option[0]} ${option[1]}'] = lambda name = option[0], price = option[1]: self.add_sushi(name, price)
            #print(so_options)

        so_options[f'{len(self.rolls)+1}. Salir'] = self.finish_order

        so_head = "Menú sushi"
        while self.order:
            self.show_menu(so_options, so_head)
            os.system('cls')
            print(f"Acualmete lleva {self.n_rolls} rolls")
            print(f"Total: {self.bill_amount}")

    def add_sushi(self, name, price):
        # print(name,price)
        self.bill_amount += price
        self.n_rolls += 1

        if name not in self.rolls_select:
            self.rolls_select[name] = 1
        else:
            self.rolls_select[name] += 1

    def finish_order(self):
        self.order = False

    def discount(self):
        os.system('cls')
        while True:
            discount_code = input("¿Tiene código de descuento?\n" \
            "1. Si tengo\n" \
            "2. No tengo\n")

            if discount_code.isdigit():
                discount_code = int(discount_code)
                if discount_code == 1:
                    discount_code = input("Ingrese su código de descuento: ") 

                    if discount_code in self.discount_codes:
                        self.bill_amount_discount = self.bill_amount*(100 - self.discount_codes[discount_code])/100
                        self.discount_code_user = discount_code
                        return True
                        # break
                elif discount_code == 2:
                    return False
                    # break

            print("Opción no válida")


    def bill(self):
        #os.system('cls')
        b_head = f"Total de productos {self.n_rolls}"
        self.print_head(b_head)
        print(f"Lleva {self.n_rolls} rolls")
        
        for y,x in self.rolls_select.items():
            print(f"{x} {y}")

        print("─"*42)
        print(f"El valor a pagar es {self.bill_amount}")
        print(f"El valor con descuento es {self.bill_amount_discount}")

    def start_delivery(self):
        os.system('cls')
        self.sushi_options()
        if self.discount():
            os.system('cls')
            print(f"Se ha aplicado descuento con el código {self.discount_code_user}")
            print(f"El descuento es de {self.discount_codes[self.discount_code_user]} %")
        self.bill()


my_delivery = Delivery()
my_delivery.start_delivery()
