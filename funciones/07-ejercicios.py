# FORMA CORTA
# def es_palindormo(text):
#     text = text.strip()
#     return text == text[::-1]


# print(es_palindormo("ala"))

# FORMA LARGA
def no_space(text):
    nuevo_texto = ""
    for char in text:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def voltear_string(texto):
    nuevo_texto = ""
    for char in texto:
        nuevo_texto = char + nuevo_texto
    return nuevo_texto


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = voltear_string(texto)
    return texto.lower() == texto_al_reves.lower()


d = es_palindromo("reconocer")
e = es_palindromo("amo la paloma")
f = es_palindromo("comida")

print(d, e, f)
