# las tuplas existentes no puedes modificarlas
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)
# la funcion tuple solo acepta iterables
punto = tuple(range(4))  # (0, 1, 2, 3)
punto2 = tuple("abcde")  # ('a', 'b', 'c', 'd', 'e')
punto3 = tuple([1, 2])  # (1, 2)

menos_numeros = numeros[:2]
print(menos_numeros)
primero, segundo, *otros = numeros
print(primero)
print(segundo)
print(otros)
# si quieres modificar una tupla
lista_numeros = list(numeros)
lista_numeros[0] = "happy"

print(lista_numeros)
# en conclusion solo modificas la lista no la tupla
