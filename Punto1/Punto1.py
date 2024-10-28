frase = input("Escriba una palabra o frase: ").lower()


conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


for letra in frase:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

#
print("Conteo de vocales:")
for vocal, conteo in conteo_vocales.items():
    print(f"{vocal}: {conteo}")
