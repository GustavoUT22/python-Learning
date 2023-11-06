mascotas = ["Wolfgang", "Pelusa", "Pulga", "Felipe", "Pulga", "Feliz"]

# agregando
mascotas.insert(1, "Firulais")  # add element in posicion
mascotas.append("Lazy")  # add at the last of list


# eliminando
mascotas.remove("Pulga")  # the first element founded
mascotas.pop()  # the last element
mascotas.pop(1)  # with index
del mascotas[0]  # with index
mascotas.clear()  # delete all
print(mascotas)
