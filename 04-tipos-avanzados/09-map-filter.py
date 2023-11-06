usuarios = [
    ["chanchito", 3],
    ["felipe", 1],
    ["pedro", 5],
]

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)  # ['chanchito', 'felipe', 'pedro']

menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menos_usuarios)
