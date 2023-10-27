#           parametros
def saludo(nombre, apellido="torres"):
    print("Hola mundo!")
    print(f"Bienvenido {nombre.title()} {apellido.title()}")


#          argumentos
saludo("gustavo", "ugarte")
saludo("enma")
saludo(apellido="torres", nombre="lenin")
