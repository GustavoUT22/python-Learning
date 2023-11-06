# el key solo puede ser un string
punto = {"x": 35, "y": 50}
print(punto['x'])
print(punto['y'])

# agregamos un elemento
punto['z'] = 45
# punto['lala'] = 55
if 'lala' in punto:
    print("encontre lala", punto['lala'])

print(punto.get('x'))
print(punto.get("lala", 95))

del punto['x']
del (punto['y'])
print(punto)
print("===================")
punto['x'] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for k, v in punto.items():
    print(k, v)

usuarios = [
    {'id': 1, 'nombre': 'skips'},
    {'id': 2, 'nombre': 'tomas'},
    {'id': 3, 'nombre': 'mordecai'},
    {'id': 4, 'nombre': 'benson'},
    {'id': 5, 'nombre': 'rigby3'},
]

for usuario in usuarios:
    print(usuario['nombre'])
