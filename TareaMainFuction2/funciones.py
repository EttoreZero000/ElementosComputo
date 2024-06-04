def funcionNumeroSuerte(entrada):
    salida = 0
    for caracter in entrada:
        if caracter.isdigit():
            salida += int(caracter)
    return salida

def funcionVocales(entrada):
    cantidadA = cantidadE = cantidadI = cantidadO = cantidadU = cantidadC = 0
    for letra in entrada:
        if letra.lower() == "a":
            cantidadA += 1
        elif letra.lower() == "e":
            cantidadE += 1
        elif letra.lower() == "i":
            cantidadI += 1
        elif letra.lower() == "o":
            cantidadO += 1
        elif letra.lower() == "u":
            cantidadU += 1
        else:
            cantidadC += 1
    return [cantidadA, cantidadE, cantidadI, cantidadO, cantidadU, cantidadC]

def funcionPalindroma(entrada):
    palabraNueva = ""
    for letra in reversed(entrada):  # Recorremos la palabra en reversa
        palabraNueva += letra

    if palabraNueva == entrada:
        return f"La palabra '{entrada}' es una palabra palíndroma."
    else:
        return f"La palabra '{entrada}' no es una palabra palíndroma"

def funcionEliminarVocales(entrada):
    palabraNueva = ""
    vocales = ['a', 'e', 'i', 'o', 'u']
    # Recorremos la palabra letra por letra
    for letra in entrada:
        # Si la letra no es una vocal, la agregamos a la nueva palabra
        if letra.lower() not in vocales:
            palabraNueva += letra
    return palabraNueva

def funcionPalabraEspejo(entrada):
    palabraNueva=""
    for i in range(-1, -(len(entrada)+1), -1):  # Empieza en -1 y termina en el negativo de la longitud de la palabra (no inclusivo), decreciendo en -1
        palabraNueva += entrada[i]
    return palabraNueva

def funcionPalabras(entrada):
    numeroPalabras=numeroLetras=0
    enPalabra= False
    for caracter in entrada:
        numeroLetras+=1
        if caracter == " ":
            if enPalabra:
                numeroPalabras+=1
                enPalabra=False
        else:
            enPalabra=True
    if enPalabra:
        numeroPalabras+=1
    return (f"Numero de palabras es de {numeroPalabras}\nNumero de letras es de {numeroLetras}")
