# la variable numero toma los valores del 0 al 5
for ele in ["a", "b", "c"]:
    print(ele)

for ele in range(5):
    print(ele * "#")

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontré el nunero buscado")


for char in "Ultimate Python":
    print(char)
