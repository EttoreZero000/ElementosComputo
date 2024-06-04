#Elaborado por Hector Leiva y Mauricio Cortes
#Fecha de creacion 16/4/2024
#Fecha de modicacion 17/4/2024
#Version 3.12.2 64-bit Visual Studio Code

#Funciones
def imprimirFila(pentrada):
    """
    Imprime una fila de la matriz especificada por el usuario.
    Parámetros:
    - pentrada: lista de listas, representa una matriz.
    Entradas:
    - Solicita al usuario un número entero que corresponde a la fila que quiere imprimir (basado en uno).
    Retornos:
    - Si el número de fila es válido, devuelve una cadena con los elementos de la fila especificada separados por espacios.
    - Si el número de fila no es válido, devuelve una cadena que indica que la fila no existe.
    """
    stringNuevo = ""
    # Iterar a través de cada fila en la matriz
    for fila in pentrada:
        # Iterar a través de cada elemento en la fila
        for elemento in fila:
            # Agregar cada elemento a la cadena stringNuevo, seguido de un espacio
            stringNuevo += str(elemento) + " "
        # Agregar un salto de línea al final de cada fila
        stringNuevo += "\n"
    # Devolver la cadena que contiene todas las filas de la matriz
    return stringNuevo
def imprimirColumna(pentrada):
    """
    Imprime una columna de la matriz especificada por el usuario.
    Parámetros:
    - pentrada: lista de listas, representa una matriz.
    Entradas:
    - Solicita al usuario un número entero que corresponde a la columna que quiere imprimir (basado en uno).
    Retornos:
    - Si el número de columna es válido, devuelve una cadena con los elementos de la columna especificada separados por espacios.
    - Si el número de columna no es válido, devuelve una cadena que indica que la columna no existe.
    """
    stringNuevo = ""
    for i in range(len(pentrada[0])):
        for fila in pentrada:
            stringNuevo += str(fila[i]) + " "
        stringNuevo+="\n"
    return stringNuevo
def RellenarMatriz(nFila, nColumna):
    """
    Crea una matriz de nFila x nColumna y la rellena con valores basados en la suma de los índices de fila y columna.
    Parámetros:
    - nFila: int, el número de filas de la matriz.
    - nColumna: int, el número de columnas de la matriz.
    Retornos:
    - Una matriz (lista de listas) de tamaño nFila x nColumna con valores basados en la suma de los índices de fila y columna.
    """
    matriz = []
    for i in range(nFila):
        fila = []
        for j in range(nColumna):
            valor = i + j
            fila.append(valor)
        matriz.append(fila)
    return matriz
def imprimirMatrizCuadrada():
    """
    Solicita al usuario ingresar el tamaño de una matriz cuadrada y luego la imprime con valores basados en la suma de los índices de fila y columna.
    Entradas:
    - Solicita al usuario que ingrese un número entero para la cantidad de filas y columnas de la matriz.
    Retornos:
    - Devuelve una cadena que representa la matriz con valores basados en la suma de los índices de fila y columna, cada fila separada por una nueva línea.
    """
    stringNuevo = ""
    nFila = int(input("Ingrese la cantidad de filas: "))
    nColumna = int(input("Ingrese la cantidad de columnas: "))
    matriz = RellenarMatriz(nFila, nColumna)
    for fila in matriz:
        for columna in range(len(fila)):
            stringNuevo += str(fila[columna]) + " "
        stringNuevo += "\n"
    return stringNuevo
def nulaMatriz():
    """
    Verifica si la matriz ingresada por el usuario es una matriz nula (matriz donde todos los elementos son cero).
    Entradas:
    - Solicita al usuario que ingrese una matriz.
    Retornos:
    - Retorna True si la matriz es nula (todos los elementos son cero), de lo contrario retorna False.
    """
    lista=[]
    matriz = convertirEntradaAMatriz()
    for i in matriz:
        if i !=0:
            lista.append(False)
        else:
            lista.append(True)
    return lista
def sumarMatriz(matriz):
    """
    Calcula la suma de todos los elementos de una matriz.
    Parámetros:
    - matriz: lista de listas, representa una matriz.
    Retornos:
    - Retorna la suma total de todos los elementos de la matriz.
    """
    suma_total = 0
    for fila in matriz:
        for elemento in fila:
            suma_total += elemento
    return suma_total
def convertirEntradaAMatriz():
    """
    Convierte una entrada de cadena que representa una matriz a una lista de listas.
    Entradas:
    - Solicita al usuario que ingrese una matriz como una lista de listas.
    Retornos:
    - Devuelve la matriz convertida de la entrada del usuario (lista de listas).
    - Si la conversión tiene éxito, devuelve la matriz.
    - Llama a la función `sumarMatriz(matriz)` para calcular la suma total de los elementos de la matriz.
    """
    entradas = [
        "[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]",
        "[[67, 87, 98, 25], [56, 45, 5, 54], [23, 56, 46, 5], [56, 23, 2, 45]]",
        "[[0, 1, 0], [1, 1, 0], [0, 1, 0]]"
    ]
    # Lista para almacenar las sumas de cada matriz
    sumasTotales = []
    # Procesa cada entrada (cadena que representa una matriz)
    for entrada in entradas:
        # Eliminar corchetes exteriores y dividir en filas
        filas = entrada.strip('[]').split('],[')
        matriz = []
        # Convertir cada fila a una lista de números
        for fila in filas:
            # Eliminar corchetes interiores y dividir por comas
            fila = fila.replace('[', '').replace(']', '').replace(' ', '').split(',')
            # Convertir cada elemento a entero
            filaNumeros = [int(numero) for numero in fila]
            matriz.append(filaNumeros)
        # Calcular la suma de la matriz convertida
        sumaTotal = sumarMatriz(matriz)
        sumasTotales.append(sumaTotal)

    # Retorna la lista de sumas totales de cada matriz
    return sumasTotales

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
entradas = [
    "[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]",
    "[[67, 87, 98, 25], [56, 45, 5, 54], [23, 56, 46, 5], [56, 23, 2, 45]]",
    "[[0, 1, 0], [1, 1, 0], [0, 1, 0]]"
    ]
def menu():
    try:
        print("Imprimir filas")
        print(imprimirFila(matriz))
        print("Imprimir columnas")
        print(imprimirColumna(matriz))
        print("Rellenar Matriz")
        print(imprimirMatrizCuadrada())
        print("Nula la Matriz")
        lista=nulaMatriz()
        for i in range(len(lista)):
            print(entradas[i])
            if lista[i]:
                print("La matriz es nula\n")
            else:
                print('La matriz no es nula\n')
        print("Suma de matrices")
        lista=convertirEntradaAMatriz()
        for i in range(len(lista)):
            print(entradas[i])
            print(lista[i])
    except ValueError:
        print("Hubo un error")
#Prrograma principal
menu()
