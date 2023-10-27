saludo = "hola global"
# utilizar variables globales es mala practica


def saludar():
    saludo = "hola mundno"
    print(saludo)


def saludar_gente():
    saludo = "hola gente"
    print(saludo)


saludar()
saludar_gente()
print(saludo)
