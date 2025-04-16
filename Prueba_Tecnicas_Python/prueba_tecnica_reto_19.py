"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 """


text = "Este es un texto de prueba, por lo que usare distintos signos de puntuacion. Por ahora no usare tildes. Agregrare mas palabras, por si las moscas."

text = "hola hola, hola hola. hola."
n_words = 0
total_char = 0
average_len_words = 0
n_sentences = 0
longest_word = ""
current_word = ""

for char in text:

    if char in [" "]:
        n_words += 1

    elif char in [".", "?", "!"]:
        n_sentences += 1

    elif char != ",":
        total_char += 1
        current_word += char

        if len(current_word) > len(longest_word):
            longest_word = current_word


if text[len(text)-1] != ".":
    n_sentences += 1
    n_words += 1


average_len_words = round(total_char/n_words)

print(n_words)
print(total_char)
print(average_len_words)
print(n_sentences)
print(longest_word)
