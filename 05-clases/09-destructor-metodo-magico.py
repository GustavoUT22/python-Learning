# son metodos que se van a ejecutar cuando nosotros
# no lo estemos llamando directamente
# ejemplo el constructor
# __algo__ esas son su estructura
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self):
        print(f"chao perro {self.nombre}")

    def habla(self):
        print(f"{self.nombre} dice: Guau")


perro = Perro("ares", 6)
del perro
