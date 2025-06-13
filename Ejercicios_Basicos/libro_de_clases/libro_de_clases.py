import os
import json


class ClassRegister():
    """Libro de clases"""

    def __init__(self, book):
        self.book = book        # Ruta del json con datos del libro de clases
        self.open = True        # Indica si el libro está en uso
        self.class_info = {}    # Almacena la información del json del libro de clases

    def load_class_info(self):
        """Carga datos de json estudiantes"""

        with open(self.book, "r", encoding="utf-8") as data:
            self.class_info = json.load(data)

    def save_class_info(self):
        """Actualiza datos de json con class_info"""

        with open(self.book, "w", encoding="utf-8") as data:
            json.dump(self.class_info, data, ensure_ascii=False, indent=4)

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

    def open_book(self):
        """Carga datos del Json y book y muestra menú principal del libro de clases"""

        os.system('cls')
        self.load_class_info()

        self.show_main_menu()

    def close_book(self):
        """Guarda progreso y cierra programa"""

        self.save_class_info()
        print("Cerrando libro de clases")
        input("Presione enter para cerrar")
        os.system('exit')

    def show_main_menu(self):
        """Muestra menú principal"""

        # Establece opciones disponibles para el menú principal
        book_option = {
            "Asignaturas": lambda x=True: self.show_subjects_menu(head=x),
            "Estudiantes": lambda x=True: self.show_student_menu(head=x),
            "Cerrar libro de clases": self.close_book
        }  

        # Establece el encabezado e imprime el menú principal
        bo_head = f'Libro de clases {self.class_info["curso"]}'
        self.show_menu_option_number(book_option, bo_head)

    def show_subjects_menu(self, width=44, head=False):
        """Muestra menú de asignaturas"""
        
        # Decide si mostrar o no el encabezado
        if head:
            head = "Asignaturas"
        else:
            head = None
            print("─"*width)

        # Establece las opciones disponibles e imprime el menú de asignaturas
        ssm_options = {
            "Lista de asignaturas": self.show_subjecs,
            "Agregar Asignatura": self.add_subjects,
            "Eliminar Asignatura": self.del_subjects,
            "Volver al menú principal": self.show_main_menu,
        }

        self.show_menu_option_number(ssm_options, head)

    def show_subjecs(self):
        """Muestra asignaturas del libro de clases y menú de asignaturas"""

        # Imprime el encabezado
        self.print_head("Asignaturas")

        # Verifica si hay asignaturas inscritas
        if len(self.class_info["asignaturas"]):

            subject_list = []
            # Imprime las asignaturas inscritas
            for idx, subject in enumerate(self.class_info["asignaturas"].keys()):
                subject_list.append(subject)
                print(f'{idx+1}. {subject}')

            print("─"*44)
            print("Para ver información de una asignatura ingrese su número: ")
            print("─"*44)

            n_subject = input("Para volver al menú principal solo presione enter: ")
            os.system('cls')

            try:
                n_subject = int(n_subject)-1

                # Si la opción es válida muestra la información de la asignatura seleccionada
                if n_subject in range(len(subject_list)):
                    self.show_subject_info(subject_list[n_subject])
                    return

                print("Número de asignatura inválido")

            except ValueError:
                print("Entrada no válida")
        else:
            print("No hay asignaturas en el libro de clases")

        self.show_subjects_menu()

    def show_subject_info(self, subject_name: str):
        """Muestra información de la asignatura"""

        # Imprime encabezado
        self.print_head(subject_name)
        print("N° Apellido Nombre | Notas")
        print("─"*44)

        # Imprime el listado de estudiantes y sus notas en la asignatura
        for student in self.class_info["asignaturas"][subject_name]:
            notas = ""
            for nota in student["notas"]:
                notas += "|" + str(nota)
            print(
                f'{student["id"]}.- {student["apellido"]} {student["nombre"]} {notas}')

        # Verifica si el usuario quiere realizar una acción con algún estudiante
        print("─"*44)
        print("1. Agregar nota a estudiante")
        print("2. Borrar nota a estudiante")
        print("─"*44)
        confirm = input("Para volver al menú principal solo presione enter: ")

        match confirm:
            case "1":
                self.add_score(subject_name)
            case "2":
                self.del_score(subject_name)
            case _:
                os.system('cls')
                self.show_main_menu()

    def add_subjects(self):
        """Agrega asignaturas a libro de clases"""

        self.load_class_info()
        adding = True
        while adding:
            self.print_head("Agregando nueva asignatura")
            subject_name = input("Ingrese el nombre de la asignatura: ")
            os.system('cls')

            if subject_name in self.class_info["asignaturas"]:
                print(f"{subject_name} ya existe")
                self.show_subjects_menu()
                return
            if subject_name == "":
                print("El nombre de la asignatura no puede estar vacío")
                self.show_subjects_menu()
                return

            self.print_head("Agregando nueva asignatura")
            print(f"¿Desea agregar {subject_name} como una nueva asignatura?")
            print("1. Volver a ingresar nombre")
            print("2. Volver al menú principal")
            print("─"*44)
            confirm = input("Para confirmar solo presione enter: ")
            os.system('cls')

            if confirm == "1":
                continue

            if confirm == "2":
                adding = False
                self.show_main_menu()

            else:
                self.add_student_list(subject_name)
                self.save_class_info()
                self.print_head("Asignatura")
                print(f"Se ha agregado {subject_name} al libro de clases")
                self.show_subjects_menu()
                return

    def del_subjects(self):
        """Muestra lista de asignatura y permite borrar una según número de lista"""

        if len(self.class_info["asignaturas"]) == 0:
            self.print_head("Asignaturas")
            print("No hay asignaturas en el libro de clases")
            self.show_subjects_menu()
            return

        while True:
            self.print_head("Eliminando asignatura")

            i = 1
            for asignatura in self.class_info["asignaturas"]:
                print(f"{i}.- {asignatura}")
                i += 1
            print("─"*44)

            try:
                n = int(input("Ingrese el número de la asignatura a eliminar: "))-1
                os.system('cls')

                if n in range(len(self.class_info["asignaturas"])):
                    subject_name = list(
                        list(self.class_info["asignaturas"].keys()))[n]
                    print(
                        f'¿Está seguro que deseas eliminar {subject_name}?')

                    print("─"*44)
                    print("1. Modificar número de estudiante")
                    print("2. Volver al menú principal")
                    print("─"*44)
                    ans = input("Para eliminar solo presione enter: ")
                    os.system('cls')

                    if ans == "1":
                        continue

                    if ans == "2":
                        break

                    del self.class_info["asignaturas"][subject_name]
                    self.save_class_info()
                    print(f"Se ha eliminado {subject_name} exitosamente")
                    break

                print("Opción no válida")

            except ValueError:
                os.system('cls')
                print("Ingrese solo números enteros")

        self.show_main_menu()

    def add_student_list(self, subject):
        """Actualiza lista de estudiantes en la asignatura"""

        lista_estudiantes = []
        for estudiante in self.class_info["lista"]:
            lista_estudiantes.append(
                {"id": estudiante["id"],
                 "nombre": estudiante["nombre"],
                 "apellido": estudiante["apellido"],
                 "notas": []}
            )

        self.class_info["asignaturas"][subject] = lista_estudiantes
        self.save_class_info()

    def show_student_menu(self, head=None):
        """Muestra menú de estudiantes"""

        if head:
            self.print_head("Estudiantes")
        else:
            print("─"*44)

        ssm_option = {
            "Mostrar lista de estudiantes": self.show_student_list,
            "Mostrar información de estudiante": self.show_student_info,
            "Agregar estudiante": self.add_student,
            "Eliminar estudiante": self.del_student,
            "Volver al menú principal": self.show_main_menu
        }

        self.show_menu_option_number(ssm_option)

    def show_student_list(self):
        """Muestra lista de estudiantes"""

        ssl_head = f'Lista de estudiantes {self.class_info["curso"]}'
        self.print_head(ssl_head)

        print("N° Apellido Nombre")
        for student in self.class_info["lista"]:
            print(
                f'{student["id"]}.- {student["apellido"]} {student["nombre"]}')

        print("─"*44)
        print("¿Qué desea hacer?")
        self.show_student_menu()

    def add_student(self):
        """Agrega a un nuevo estudiante a la lista general y de todas las asignaturas"""

        while True:
            self.print_head("Agregando estudiante")
            name = input("Ingrese el nombre del estudiante: ")
            last_name = input("Ingrese el apellido del estudiante: ")

            new_id = 0

            # Busca si el estudiante ya se encuentra en la lista
            for student in self.class_info["lista"]:
                if student["nombre"] == name and student["apellido"] == last_name:
                    os.system('cls')
                    print(f"{name} {last_name} ya se encuentra en la lista")
                    self.show_student_menu()
                    return

                if new_id <= student["id"]:
                    new_id = student["id"] + 1

            # Crea diccionario con información del estudiante
            new_student = {
                "id": new_id,
                "nombre": name,
                "apellido": last_name
            }

            # Solicita confirmación
            print(f"¿Está seguro que desea agregar a {name} {last_name}?")
            print("1. Volver a escribir nombre o apellido")
            print("2. Volver al menú principal")
            print("─"*44)
            confirm = input("Para confirmar solo presione enter: ")
            os.system('cls')

            if confirm == "1":
                continue
            if confirm == "2":
                self.show_main_menu()
                return

            self.class_info["lista"].append(new_student)

            for subject_name in self.class_info["asignaturas"]:
                self.class_info["asignaturas"][subject_name].append(
                    {"id": new_id, "notas": []})

            self.save_class_info()
            print(f"Ahora {name} {last_name} es {new_id}° de la lista")

            self.show_student_menu()
            return

    def del_student(self):
        """Elimina a un estudiante de la lista por nombre y apellido"""

        erasing = True
        while erasing:
            self.print_head("Quitando estudiante de la lista")
            name = input("Ingrese el nombre del estudiante: ")
            last_name = input("Ingrese el apellido del estudiante: ")
            os.system('cls')

            student_id = None

            for student in self.class_info["lista"]:
                if student["nombre"] == name and student["apellido"] == last_name:
                    os.system('cls')
                    student_id = student["id"]

                    print(
                        f"¿Está seguro que desea quitar a {name} {last_name} de la lista?")
                    print("1. Quiero volver a escribir nombre o apellido")
                    print("2. Quiero volver al menú de estudiantes")
                    print("─"*44)
                    confirm = input("Para eliminar solo presione enter: ")
                    os.system('cls')

                    if confirm == "1":
                        os.system('cls')
                        continue

                    if confirm == "2":
                        erasing = False
                        self.show_student_menu()
                        return

            if student_id is None:
                print(f"{name} {last_name} no se encuentra en la lista")
                erasing = False
                self.show_student_menu()
                return

            # Elimina al estudiante de la lista del curso
            for idx, student in enumerate(self.class_info["lista"]):
                if student_id == student["id"]:
                    self.class_info["lista"].pop(idx)

            # Elimina al estudiante de la lista de las asignaturas
            for subject_name, students in self.class_info["asignaturas"].items():
                for idx, student in enumerate(students):

                    if student_id == student["id"]:
                        self.class_info["asignaturas"][subject_name].pop(idx)
                        self.save_class_info()
                        print(
                            f"Se ha eliminado a {name} {last_name} de la lista")
                        break

            self.show_student_menu()
            return

    def show_student_info(self):
        pass

    def add_score(self, subject_name):
        """Permite agregar notas a un estudiante"""

        self.print_head("Agregando calificaciones")
        print("INGRESE EL NÚMERO DE LA LISTA DEL ESTUDIANTE")
        print("─"*44)
        confirm = input("Para volver atrás solo presione enter\n")
        os.system('cls')

        try:
            n_student = int(confirm)
        except ValueError:
            print("Solo ingrese números")
            self.show_subject_info(subject_name)
            return

        find_student = False
        name = None
        relative_possition = None
        for idx, student in enumerate(self.class_info["asignaturas"][subject_name]):
            if student["id"] == n_student:
                name = student["nombre"] + " " + student["apellido"]
                relative_possition = idx
                find_student = True

        if not find_student:
            print(f"No se ha encontrado al estudiante n° {n_student}")

        while find_student:
            self.print_head(f'Notas de {name} en {subject_name}', width=50)
            print("Ingrese la nota sin punto decimal")
            print("Ejemplo: Para un 6,5 ingrese 65")
            print("─"*50)

            try:
                nota = int(input("Ingrese nota: "))
                os.system('cls')

                if 10 <= nota <= 70:
                    self.class_info["asignaturas"][subject_name][relative_possition]["notas"].append(
                        nota/10)
                    print(f"Se ha agregado {nota/10} en las notas de {name}")
                    self.save_class_info()

                else:
                    print("La nota debe estar entre 10 y 70")

                print("─"*44)
                print("1. Para volver a la asignatura")
                print("2. Para volver al menú principal")
                print("─"*44)
                confirm = input(
                    'Para ingresar otra nota solo presione enter: ')
                os.system('cls')

                if confirm == "1":
                    self.show_subject_info(subject_name)
                    return
                if confirm == "2":
                    self.show_main_menu()
                    return

            except ValueError:
                os.system('cls')
                print("Error al ingersar nota")
                print("Ingrese solo números entre 10 y 70")
                print("─"*44)
                print("Presione enter para continuar o ingrese x para volver atrás")
                confirm = input()
                if confirm == "x":
                    self.show_subject_info(subject_name)
                    return
                os.system('cls')

    def del_score(self, subject_name):
        """Permite eliminar notas a un estudiante en particular"""

        self.print_head("Borrando calificaciones")
        print("INGRESE EL NÚMERO DE LA LISTA DEL ESTUDIANTE")
        print("─"*44)
        confirm = input("Para volver atrás solo presione enter\n")
        os.system('cls')

        try:
            n_student = int(confirm)
        except ValueError:
            print("Solo ingrese números")
            self.show_subject_info(subject_name)
            return

        find_student = False
        name = None
        relative_possition = None
        for idx, student in enumerate(self.class_info["asignaturas"][subject_name]):
            if student["id"] == n_student:
                name = student["nombre"] + " " + student["apellido"]
                relative_possition = idx
                find_student = True

        if not find_student:
            print(f"No se ha encontrado al estudiante n° {n_student}")

        cantidad_notas = len(self.class_info["asignaturas"][subject_name][n_student])
        if len(self.class_info["asignaturas"][subject_name][n_student]) == 0:
            print(f"{name} no tiene calificaciones")
            self.show_subject_info(subject_name)
            return
        
        for idx, nota in enumerate(self.class_info["asignaturas"][subject_name][relative_possition]["notas"]):
            print(f"{idx+1}.- {nota}")
        print("─"*44)

        print("Ingrese el número de la nota que desea eliminar")
        confirm = input("Para volver atrás solo presione enter: ")
        os.system('cls')

        try:
            n_nota = int(confirm) - 1
            if n_nota in range(cantidad_notas):
                self.class_info["asignaturas"][subject_name][relative_possition]["notas"].pop(n_nota)
                self.save_class_info()
                print("Se ha eliminado la nota con éxito")
            else:
                print(f"No se ha encontrado la nota {n_nota}")
            
            self.show_subject_info(subject_name)

        except ValueError:
            self.print_head(subject_name)
            self.show_subject_info(subject_name)
            return

            
ruta_libro = "ruta"
mi_libro = ClassRegister(ruta_libro)
mi_libro.open_book()
