class Perro:
    patas = "cinco"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau")

    # factory method
    @classmethod
    def factory(cls):
        return cls("happy", 4)

    def info(self):
        print(f"{self.nombre} tiene {self.edad} años")


Perro.habla()
perro1 = Perro("Ares", 6)
perro2 = Perro.factory()
print(perro2.edad, perro2.nombre)
