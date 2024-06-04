# Elaborado por Hector Leiva y Mauricio Cortes
# Creación del archivo 10-5-2024
# Última modificación 11-5-2024
# Versión 3.12.2 64-bits

# Funciones importadas

# Funciones

def esPar(numero):
    """
    Entra un numero y retorna True si es par
    Entrada: numero int
    Salida: True o False
    """
    if numero % 2 == 0:
        return True
    else:
        return False
def contarParesImpares(*arg):
    """
    Cuenta la cantidad de números pares e impares de 4 dígitos.
    Entrada: *arg (int) - números enteros
    Salida: (int, int) - cantidad de pares e impares respectivamente
    """
    print(f"Entrada: {arg}")
    contadorPares = contadorImpares = 0
    for numeros in arg:
        if len(str(numeros)) == 4:
            if esPar(numeros):
                contadorPares += 1
            else:
                contadorImpares += 1
        else:
            return "Debe ser un número natural de 4 dígitos."
    return (contadorPares, contadorImpares)
def separarParesImpares(*args):
    """
    Separa los números pares e impares de 4 dígitos.
    Entrada: *args (int) - números enteros
    Salida: ([int], [int]) - listas de números pares e impares respectivamente
    """
    print(f"Entrada: {args}")
    listaPares = []
    listaImpares = []
    for numero in args:
        if len(str(numero)) == 4:
            if esPar(numero):
                listaPares.append(numero)
            else:
                listaImpares.append(numero)
        else:
            return "Debe ser un número natural de 4 dígitos."
    return (listaPares, listaImpares)
def desglozar(dinero):
    """
    Desglosa una cantidad de dinero en billetes de diferentes denominaciones.
    Entrada: dinero (int) - cantidad de dinero
    Salida: (int, int, int, int, int, int) - cantidad de billetes de 100, 50, 20, 10, 5, 1 respectivamente
    """
    print(f"Entrada: {dinero}")
    billete100 = billete50 = billete20 = billete10 = billete5 = billete1 = 0
    while dinero > 0:
        if dinero >= 100:
            billete100 += 1
            dinero -= 100
        elif dinero >= 50:
            billete50 += 1
            dinero -= 50
        elif dinero >= 20:
            billete20 += 1
            dinero -= 20
        elif dinero >= 10:
            billete10 += 1
            dinero -= 10
        elif dinero >= 5:
            billete5 += 1
            dinero -= 5
        elif dinero >= 1:
            billete1 += 1
            dinero -= 1
    return (billete100, billete50, billete20, billete10, billete5, billete1)
def contarPalabras(palabrasAContar, tuplaDeTextos):
    """
    Cuenta la cantidad de ocurrencias de palabras en una tupla de textos.
    Entrada: palabrasAContar (tuple) - palabras a contar
             tuplaDeTextos (tuple) - tupla de textos
    Salida: dict - diccionario con las palabras contadas y su cantidad de ocurrencias
    """
    biblioteca = {palabra: 0 for palabra in palabrasAContar}  # Inicializa todas las palabras a contar con un valor de 0
    for texto in tuplaDeTextos:
        palabras = texto.split()  # Divide el texto en palabras
        for palabra in palabras:
            palabra = palabra.lower()  # Convierte la palabra a minúsculas para considerar la misma palabra en diferentes formas
            if palabra in palabrasAContar:
                biblioteca[palabra] += 1
    return biblioteca
def contarPalabrasAux(palabrasAContar, tuplaDeTextos):
    """
    Hace la funcion contarPalabra y lo ordena para que se vea bonito
    Entrada: palabrasAContar (tuple) - palabras a contar
             tuplaDeTextos (tuple) - tupla de textos
    Salida: Print ordenado
    """
    diccionario=contarPalabras(palabrasAContar, tuplaDeTextos)
    for clave,valor in diccionario.items():
        print(f"{clave}: {valor}")
    return None
def esParAmigable(tuplaNumero):
    """
    Comprueba si dos números son amigables.
    Entrada: tuplaNumero (tuple) - tupla con dos números enteros
    Salida: bool - True si los números son amigables, False de lo contrario
    """
    numero1 = numero2 = 0
    print(f"Entrada: {tuplaNumero}")
    if tuplaNumero[0] == tuplaNumero[1]:
        return False
    elif tuplaNumero[0] <= 0 or tuplaNumero[1] <= 0:
        return False
    for numero in sacarDivisores(tuplaNumero[0]):
        numero1 += numero
    for numero in sacarDivisores(tuplaNumero[1]):
        numero2 += numero
    if numero1 == tuplaNumero[1] and numero2 == tuplaNumero[0]:
        return True
    else:
        return False
def sacarDivisores(numero):
    """
    Obtiene los divisores de un número.
    Entrada: numero (int) - número entero
    Salida: list - lista de divisores
    """
    divisores = []
    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
def mostrarCercano(tuplaNumero):
    """
    Encuentra el número más cercano al primer elemento de la tupla.
    Entrada: tuplaNumero (tuple) - tupla de números enteros
    Salida: int - número más cercano
    """
    primer_elemento = tuplaNumero[0]
    distanciaMin = float('inf')
    numeroBajo = None  # Inicializamos el número más bajo como None
    for elemento in tuplaNumero[1:]:
        distancia = abs(elemento - primer_elemento)
        if 0 < distancia < distanciaMin:
            numeroBajo = elemento
            distanciaMin = distancia
        elif distancia == distanciaMin:
            numeroBajo = min(numeroBajo, elemento)  # Escogemos el más pequeño si hay empate
    return numeroBajo
def mostrarCercanoAux(tuplaNumero):
    """
    Función auxiliar para mostrar el número más cercano.
    Entrada: tuplaNumero (tuple) - tupla de números enteros
    Salida: int - número más cercano
    """
    print(f"Entrada: {tuplaNumero}")
    numeroVisto = set()
    if type(tuplaNumero) != tuple:
        return "Debe de ingresar una tupla"
    elif len(tuplaNumero) != 5:
        return "Deben de ser exactamente 5 valores enteros"
    for numero in tuplaNumero:
        if type(numero) == str:
            return "Las entradas debe de ser enteros"
        elif numero < 0:
            return "Las entradas deben ser mayores a cero"
        if numero in numeroVisto:
            return "No se puede ingresar numeros repetidos"
        else:
            numeroVisto.add(numero)
    return mostrarCercano(tuplaNumero)
# Programa principal
print("-----------------------------------")
print("Cuantos números hay pares e impares:")
print(contarParesImpares(1235, 1742, 1111, 2321))
print(contarParesImpares(2426, 1224, 1542, 1000))
print(contarParesImpares(3557, 1237, 1243, 4561))
print(contarParesImpares(219999))
print("-----------------------------------")
print("Separar números pares e impares:")
print(separarParesImpares(1235, 1742, 1111, 2321))
print(separarParesImpares(2426, 1224, 1542, 1000))
print(separarParesImpares(3557, 1237, 1243, 4561))
print(separarParesImpares(3557))
print(separarParesImpares(219999))
print("-----------------------------------")
print("Devolución de dinero:")
print(desglozar(1427))
print("-----------------------------------")
print("Contar palabras:")
contarPalabrasAux(("calor", "ayer", "el", "mañana"), ("ayer hizo bastante calor", "en el laboratorio hace calor"))
print("-----------------------------------")
print("Es par amigable:")
print(esParAmigable((220, 284)))
print(esParAmigable((15, 18)))
print(esParAmigable((1210, 1184)))
print(esParAmigable((890, 890)))
print("-----------------------------------")
print("Mostrar cercano:")
print(mostrarCercanoAux((8, 11, 4, 10, 100)))
print(mostrarCercanoAux((8, 11, 10, 4, 6)))
print(mostrarCercanoAux([8, 11, 4, 8, 10]))
print(mostrarCercanoAux((8, 11, 4, 10)))
print(mostrarCercanoAux((8, 11, "4", -10, 6)))
print(mostrarCercanoAux((8, 11, 4, -10, 6)))
print(mostrarCercanoAux((8, 11, 4, 10, 4)))