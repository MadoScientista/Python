"""
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.


 Cifrado Cesar: Es un tipo de cifrado por sustitución en el que una letra en 
 el texto original es reemplazada por otra letra que se encuentra un número fijo 
 de posiciones más adelante en el alfabeto. Por ejemplo, con un desplazamiento 
 de 3, la A sería sustituida por la D (situada 3 lugares a la derecha de la A), 
 la B sería reemplazada por la E, etc.
"""


class CesarCode():
    def __init__(self, base):
        self.alphabet = "abcdefghijklmnñopqrstuvwxyz"
        self.base = base
        self.text = ""
        self.encode_dict = self.encodeDict()
        self.decode_dict = self.decodeDict()

    def encodeDict(self):
        encode_dict = {}
        for index, char in enumerate(self.alphabet):
            encode_dict[char] = self.alphabet[self.base +
                                              index-len(self.alphabet)]

        return encode_dict

    def decodeDict(self):
        decode_dict = {}
        for index, char in enumerate(self.alphabet):
            decode_dict[char] = self.alphabet[index-self.base]

        return decode_dict

    def encode(self, text):
        encode_text = ""

        for char in text.lower():
            if char in self.alphabet:
                encode_text += self.encode_dict[char]
            else:
                encode_text += char

        return encode_text

    def decode(self, text):
        decode_text = ""

        for char in text.lower():
            if char in self.alphabet:
                decode_text += self.decode_dict[char]
            else:
                decode_text += char

        return decode_text


saludo = "---- Codificador Cesar ----"
print(saludo+"\n")

mode = int(input("¿Qué deseas hacer?\n" +
                 "\n(1) Codificar \n(2) Decdificar \n\nIngresa una opción (1 o 2): "))

base = int(input(
    "\nIngresa un número entero como base de desplazamiento (1, 2, 3, 4, etc) \nBase: "))


cesar = CesarCode(base)

if mode == 1:
    text = input("\nIngresa el texto a codificar: ")
    print("El texto codificado es:" + "\n" + cesar.encode(text) + "\n")
elif mode == 2:
    text = input("\nIngresa el texto a decodificar: ")
    print("El texto decodificado es:" + "\n" + cesar.decode(text) + "\n")
