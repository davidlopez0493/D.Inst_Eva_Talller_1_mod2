nombres = input("Escriba una lista de nombres separados por comas: ").split(',')


nombres = [nombre.strip() for nombre in nombres]


nombres_ordenados = sorted(nombres)


print("nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)
