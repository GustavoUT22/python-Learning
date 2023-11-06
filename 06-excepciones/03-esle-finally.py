try:
    n1 = int(input("ingresa primer numero"))
except Exception as e:
    print("Ocurrió un error ")
else:
    print("no ocurrió nada")
finally:
    print("se ejecuta siemrpe")
