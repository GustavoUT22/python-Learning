class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(f"{self.nombre} tiene {self.edad} años")


mi_perro = Perro("Ares", 6)
print(mi_perro.nombre)
mi_perro.info()
