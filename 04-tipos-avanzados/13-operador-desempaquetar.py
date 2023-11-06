lista = [1, 2, 3, 4]
print(*lista)  # 1 2 3 4
lista2 = [5, 6]
combinada = [*lista, *lista2]
print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hi", **punto2, "z": "mundo"}
print(nuevoPunto)
