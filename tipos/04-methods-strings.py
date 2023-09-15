# métodos
animal = "  GatO feliz"
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.strip())  # espacios a la izquierda
print(animal.rstrip())  # "    " a la derecha
print(animal.strip().capitalize())
print(animal.find("t"))
print(animal.find("j"))  # -1 = not found
print(animal.replace("t", "m"))
print("eli" in animal)  # retorna booleano
print("eli" not in animal)
