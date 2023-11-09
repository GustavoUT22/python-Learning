
class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):  # hereda los metodos y propiedades de animal
    def pasear(self):
        print("pasenado")


class Canguro(Perro):  # hereda todo los metodos y propiedades del perro
    def saltar(self):
        print("saltando")


canguro = Canguro()
canguro.saltar()
canguro.pasear()
canguro.comer()

perro = Perro()
perro.pasear()
perro.comer()


animal = Animal()
animal.comer()
