palabra = "Hola"
palabraNueva = ""

for i in range(-1, -(len(palabra)+1), -1):  # Empieza en -1 y termina en el negativo de la longitud de la palabra (no inclusivo), decreciendo en -1
    palabraNueva += palabra[i]

print(palabraNueva)
