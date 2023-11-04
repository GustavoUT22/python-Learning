from pprint import pprint

string = "hellow my friend"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def count_caracters(lista):
    chars_dic = {}
    for char in lista:
        if char in chars_dic:
            chars_dic[char] += 1
        else:
            chars_dic[char] = 1

    return chars_dic


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccioanrio):
    mensaje = "Los qque mas se respiten son: \n"
    for key, valor in diccioanrio.items():
        mensaje += f"- {key} con {valor} repeticones \n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = count_caracters(sin_espacios)
ordenanados = ordena(contados)
mayores = mayores_tuplas(ordenanados)
mensaje = crea_mensaje(mayores)
print(mensaje)
