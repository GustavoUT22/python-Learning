class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} guau")

    @classmethod
    def factory(cls):
        return cls("happy", 4)


perro1 = Perro.factory()
# print(perro1.__nombre) no se puede acceder
# solo podemos acceder a las propiedades privadas
# a traves de los metodos
print(perro1.get_nombre())
print(perro1.__dict__)  # aqui accedemos a todo
print(perro1._Perro__nombre)  # manera forzada
