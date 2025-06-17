# 1. Agregar artículo
# 2. Listar artículos
# 3. Actualizar precio
# 4. Borrar productos
# 5. Salir

import os

productos = [
    {"nombre": "Lápiz","precio": 400},
    {"nombre": "Goma", "precio": 200},
    {"nombre": "Estuche", "precio": 1600}
]

# for i, producto in enumerate(productos):
#     print(f'{i+1}.- {producto["nombre"]} ${producto["precio"]}')


class GestorArticulos():
    def __init__(self, products: list):
        self.products = products

    def print_head(self, text_head, width=44):
        """Imprime el encabezado de cada menú"""

        left = int((width-len(text_head))/2)
        right = width - 2 - len(text_head) - left
        print("┌" + "─" * (width-2) + "┐")
        print("│" + " " * left + text_head + " " * right + "│")
        print("└" + "─" * (width-2) + "┘")

    def show_menu_option_number(self, options: dict, head=None, width=44):
        """Muestra menú interactivo con opciones numpéricas"""

        option_list = list(options.items())  # Lista las opciones disponibles
        while True: 

            # Imprime el encabezado en caso de que esté definido
            if head:
                self.print_head(head)

            # Imprime las opciones disponibles
            for index, info in enumerate(option_list):
                print(f"{index+1}.- {info[0]}")
            print("─"*width)

            # Intenta capturar el número de la opción seleccionada
            try:
                option = int(
                    input("Ingrese el número de la opción que desea: ")) - 1
                os.system('cls')

                # Si la opción es válida ejecuta la función asociada
                if option in range(len(option_list)):
                    option_list[option][1]()
                    break

                print("Opcioón no válida. Inténtelo nuevamente")

            except ValueError:
                os.system('cls')
                print("Ingrese solo números enteros")

        
    def show_main_menu(self, head = None):

        smm_options = {
            "Agregar Artículo": self.add_product,
            "Listar Artículos": lambda x = True: self.show_products(x),
            "Actualizar Precio": self.update_price,
            "Borrar Artículo": self.del_product
        }

        if head:
            smm_head = "Gestor de Artículos"
            self.show_menu_option_number(smm_options, smm_head)
        else:
            self.show_menu_option_number(smm_options)


    def add_product(self):
        
        adding = True

        while adding:
            self.print_head("Agregando Productos")

            name = input("Ingrese el nombre del producto: ")
            try:
                price = int(input("Ingrese el precio del producto: "))
                os.system('cls')

                new_product = {
                    "nombre": name,
                    "precio": price
                }
                
                print(f'¿Está seguro que desea agregar {name} a un valor de {price}?')
                print("─"*44)
                print("1. Para volver a intentarlo")
                print("2. Para volver al menú principal")
                print("Para confirmar solo presione enter")

                confirm = input()
                os.system('cls')

                match confirm:
                    case "1":
                        continue
                    case "2":
                        self.show_main_menu()
                        adding = False
                        return
                    case _:
                        self.products.append(new_product)
                        print(f"Se ha agreado {name} con éxito")
                        self.show_main_menu("Gestor de Artículos")
                        return

            except ValueError:
                os.system('cls')
                print("El precio debe ser solo números enteros")

    def show_products(self, head=True):

        if head:
            self.print_head("Lista de productos")

        for i, product in enumerate(self.products):
            print(f'{i+1}.- {product["nombre"]} ${product["precio"]}')

        print("─"*44)
        print("¿Qué desea hacer?")
        self.show_main_menu()


    def update_price(self):
        updating = True
        os.system('cls')
        while updating:
            self.print_head("Actualizando Precios")
            try:
                self.show_products()
                n = int(input("Ingrese el número del producto que desea actualizar: ")) -1

                if n in range(len(self.products)):
                    price = int(input("Ingrese el nuevo precio: "))

                    print("─"*44)
                    print("1. Para volver a intentarlo")
                    print("2. Para volver al menú principal")
                    print("Para confirmar solo presione enter")
                    confirm = input(f'¿Está seguro que quiere actualizar {self.products[n]["nombre"]} a {self.products[n]["precio"]}?')
                    

                    match confirm:
                        case "1":
                            continue
                        case "2":
                            self.show_main_menu()
                            updating = False
                            return
                        case _:
                            self.products[n]["price"] = price
                            print(f'Se ha actualizado el valor de {self.products[n]["nombre"]} con éxito)')
                            self.show_main_menu("Gestor de Artículos")
                            return
                else:
                    print(f"El producto {n} no se encuentra dentro de la lista")

            except ValueError:
                print("Ingrese solo números enteros")


    def del_product(self):
        erasing = True
        os.system('cls')
        while erasing:
            self.print_head("Eliminando Productos")
            try:
                self.show_products()
                n = int(input("Ingrese el número del producto que desea borrar: ")) - 1
                name = self.products[n]["nombre"].copy()

                if n in range(len(self.products)):
                    
                    print("─"*44)
                    print("1. Para volver a intentarlo")
                    print("2. Para volver al menú principal")
                    print("Para confirmar solo presione enter")
                    confirm = input(f'¿Está seguro que quiere eliminar {self.products[n]["nombre"]}?')
                    
                    match confirm:
                        case "1":
                            continue
                        case "2":
                            self.show_main_menu()
                            erasing = False
                            return
                        case _:
                            self.products.pop(n)
                            print(f'Se ha eliminado el valor de {name} con éxito)')
                            self.show_main_menu("Gestor de Artículos")
                            return
                else:
                    print(f"El producto {n} no se encuentra dentro de la lista")

            except ValueError:
                print("Ingrese solo números enteros")



    def start(self):
        self.show_main_menu("Gestor de Artículos")


mi_gestor = GestorArticulos(productos)

mi_gestor.start()