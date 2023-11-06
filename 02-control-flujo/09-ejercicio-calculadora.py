print("Bienvenidos a la calculadora")
print("Para salir escribir salir")
print("Las operaciones son suma, multi, div y resta")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese el número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese el operador: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break
    print(f"el resultado es {resultado}")
