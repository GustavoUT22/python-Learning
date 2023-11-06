# and, or, not
gas = True
encendido = True
apagado = False
edad = 18

if gas and encendido:
    print("Puedes avanzar")


if encendido or apagado:
    print("puedes seguir")

if not encendido or apagado:
    print("uno es verdadero")
else:
    print("es falso")


if gas and (encendido or edad > 17):
    print("puedes avanzar")

# operaciones de corto circuito= significa que se corta la evaluación
