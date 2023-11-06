# set significa grupo o conjunto con datos que no
# se pueden repetir y que no esta ordenado

primer = {1, 1, 2, 2, 3, 4}
# print(primer)   {1, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)
print(primer | segundo)  # apareceran unidos con datos unicos
print(primer & segundo)  # los que tengan en comun
# muestra los datos de la izquierda quitandoles los que estan en la drecha
print(primer - segundo)  # {1,2,3}^ {2,3,4} == {1,4}
