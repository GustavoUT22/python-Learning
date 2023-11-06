usuarios = [
    ["chanchito", 3],
    ["felipe", 1],
    ["pedro", 5],
]

# nombres = []
# for user in usuarios:
#     nombres.append(user[0])

# print(nombres)
# TRANSFORMAR LA LISTA
nombres = [user[0] for user in usuarios]
# esto devuelve ['chanchito', 'felipe', 'pedro']
# FILTRAR
numeros = [user for user in usuarios if user[1] > 2]
# TRANSFORMAR LA LISTA Y FILTRAR
numeros2 = [user[0] for user in usuarios if user[1] > 2]
