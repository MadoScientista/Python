import os


class DeliverySushi():
    def __init__(self):
        self.rolls_menu = {
            "1": {
                "name": "Pikachu Roll",
                "price": 4500
            },
            "2": {
                "name": "Otaku Roll",
                "price": 5000
            },
            "3": {
                "name": "Pulpo Venenoso Roll",
                "price":  5200
            },
            "4": {
                "name": "Anguila Eléctrica Roll",
                "price": 4800},
        }
        self.discount_codes = {
            "soyotaku": 10,
        }
        self.is_gone = False
        self.in_order = True

        self.rolls_in_order = {}
        self.sub_total = 0
        self.discount = 0

    def print_head(self, text_head: str):
        print("*"*42)
        print(text_head.center(42))
        print("*"*42)

    def show_sushi_options(self):
        for option, info in self.rolls_menu.items():
            print(f'{option}. {info["name"]} ${info["price"]}')

    def take_sushi_order(self):
        self.print_head("¿Qué roll desea agregar?")
        self.show_sushi_options()

        finish_order = str(len(self.rolls_menu) + 1)
        print(f"{finish_order}. Ir a pagar")

        print("*"*42)
        n = input("Ingrese la opción que desea: ")
        os.system('cls')

        if n == finish_order:
            self.in_order = False

        if n in self.rolls_menu:
            name_roll = self.rolls_menu[n]["name"]
            price_roll = self.rolls_menu[n]["price"]

            if name_roll in self.rolls_in_order:
                self.rolls_in_order[name_roll] += 1
            else:
                self.rolls_in_order[name_roll] = 1

            self.sub_total += price_roll
            print(f"Ha agregado {name_roll}")
            print(f"total a pagar: {self.sub_total}")

    def apply_discount(self):
        while True:
            self.print_head("¿Tiene código de descuento?")
            print("1. Si tengo")
            print("2. No tengo")

            print("*"*42)
            ad_option = input()
            os.system('cls')

            match ad_option:
                case "1":
                    print("*"*42)
                    code = input("Ingrese código: ")
                    os.system('cls')

                    if code in self.discount_codes:
                        self.discount = self.sub_total * \
                            self.discount_codes[code]/100
                        return True

                    print("Código no válido")
                    print("*"*42)
                    print("Para seguir comprando ingrese x")
                    print("De lo contrario presione enter")
                    re_order = input()
                    os.system('cls')

                    if re_order == "x":
                        self.in_order = True
                        return False

                case "2":
                    return True
                case _:
                    print("Opción no válida, intente nuevamente")

    def bill(self):
        total_products = 0
        for name, number in self.rolls_in_order.items():
            total_products += number

        self.print_head(f"Total productos: {total_products}")

        for name, number in self.rolls_in_order.items():
            print(f"{name}: {number}")

        print("*"*42)
        print(f"Sub total a pagar: {self.sub_total}")
        print(f"Descuento por código: {self.discount}")
        print(f"TOTAL: {self.sub_total - self.discount}")
        print("*"*42)

    def reset_order(self):
        self.is_gone = False
        self.in_order = True

        self.rolls_in_order = {}
        self.sub_total = 0
        self.discount = 0

    def in_local(self):
        while True:
            print("¿Desea realizar otra compra?")
            print("1. Si")
            print("2. No")

            ans = input()
            os.system('cls')

            match ans:
                case "1":
                    self.reset_order()
                    break
                case "2":
                    self.is_gone = True
                    os.system('cls')
                    print("Muchas gracias por su compra")
                    print("*"*42)
                    input("Presione enter para terminar")
                    os.system('exit')
                    break
                case _:
                    print("Opción no válida, intente nuevamente")

    def start(self):
        os.system('cls')
        while not self.is_gone:

            while self.in_order:
                self.take_sushi_order()

            if self.apply_discount():
                self.bill()
                input("Presione enter para continuar")
                os.system('cls')
                self.in_local()


my_sushi = DeliverySushi()
my_sushi.start()
