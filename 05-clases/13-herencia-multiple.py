class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro(Caminador, Nadador):
    def programar(self):
        print("programando")


class Pato(Caminador, Nadador, Volador):
    def cuack(self):
        print("hacer bulla")
