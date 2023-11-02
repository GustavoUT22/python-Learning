numeros = [2, 45, -13, 18, 93, 4, 1]
# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)  # devuelve una nueva lista
print(numeros)
print(numeros2)

usuarios = [
    ["chanchito", 3],
    ["felipe", 1],
    ["pedro", 5],
    ["Gustavo", -2]
]

# manera 1
# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)

# manera 2
usuarios.sort(key=lambda el: el[1])
print(usuarios)
