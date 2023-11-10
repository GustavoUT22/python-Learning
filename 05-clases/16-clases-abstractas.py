from abc import ABC, abstractmethod


class Model(ABC):  # 1 para no generar instancias debe heredar de ABC
    @property  # 2
    @abstractmethod  # 3
    def tabla(self):
        pass

    # ya no es necesario el construcot cuando es abstracto
    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")

    @abstractmethod
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id: {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guaradando usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(12)
