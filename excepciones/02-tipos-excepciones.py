try:
    n1 = int(input("ingresa primer numero"))
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrió un error ")
# except Exception as e:
#     print(type(e))
