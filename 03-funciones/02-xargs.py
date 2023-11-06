def suma(*numeros):  # params iterables
    resultado = 0
    for num in numeros:
        resultado += num
    print(resultado)


suma(1, 2, 3, 4)
suma(9, 7, 2, 7, 2)
