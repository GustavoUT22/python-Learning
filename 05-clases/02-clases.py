class Perro:
    def habla(self):
        print("Guau")


mi_perro = Perro()
print(type(mi_perro))  # <class '__main__.Perro'>
mi_perro.habla()
#                 objeto    clase
print(isinstance(mi_perro, Perro))
