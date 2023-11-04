pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
print(pila)
ultimoElmento = pila.pop()
print(ultimoElmento)
print(pila)
print(pila[-1])

pila.pop()
pila.pop()

pila.pop()

if not pila:
    print("pila vacia")
