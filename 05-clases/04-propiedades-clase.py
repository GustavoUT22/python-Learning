# veremos diferencia entre las propiedades de
# clase y de las propiedades de las instancias

class Perro:
    patas = "cinco"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(f"{self.nombre} tiene {self.edad} años")


mi_perro = Perro("Ares", 6)
mi_perro.info()
Perro.patas = "cuatro"  # modifica el valor parala clase
mi_perro.patas = "tres"  # modifica el valor para la instancia
print(mi_perro.patas)
print(Perro.patas)
