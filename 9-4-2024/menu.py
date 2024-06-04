#Elaborado por Hector Lieva, Mauricio Cortes
#Fecha de creacion 9-4-2024
#Fecha de ultima modificación 10-4-2024
#Version 3.12.2 64-bits, Visual Studio Code
#Importacion de librerias
from funciones import *
#Importacion de funciones salidas, entradas y verificaciónes
def mutiplicarImparesLAuxiliar(pentrada):
    """
    Multiplica los números impares en una lista de entrada (`pentrada`).
    Entradas:
        pentrada (list[int]): Lista de números enteros.
    Retorna:
        str: Retorna un mensaje de error si alguno de los elementos no es un número entero
        o si la lista contiene números mayores o iguales a 100.
        Si la lista es válida, retorna un mensaje con la lista de entrada y el
        resultado de multiplicar los números impares de la lista.
    """
    for numero in pentrada:
        if not isinstance(numero, int):
            return "Todos los elementos tienen que ser números enteros."
        if numero >= 100:
            return "La lista contiene números mayores o iguales a 100."
    resultado = funcionMultiplicarImparesL(pentrada)
    return f"Lista de entrada: {pentrada}\nResultado de multiplicar impares: {resultado}"
def notasImaginariasAuxiliar(pentrada):
    """
    Analiza una lista de notas, categorizándolas en aprobados, reprobados, o en reposición, y calcula el promedio.
    Entradas:
        pentrada (list): Lista de notas (enteros o cadenas de caracteres que pueden convertirse en enteros).
    Retorna:
        str: Retorna un mensaje de error si algún elemento no es un número o si está fuera del rango de 0 a 100.
        Si la lista es válida, retorna un resumen del número de aprobados, reprobados, y de reposición,
        junto con el promedio del grupo.
    """
    for nota in pentrada:
        try:
            nota = int(nota)
            if nota < 0 or nota > 100:
                return "Las notas deben estar entre 0 y 100."
        except ValueError:
            return f"\"{nota}\" no es un número válido."
    
    lista = funcionNotasImaginarias(pentrada)
    return (f"Cantidad de aprobados: {lista[0][0]}\n"
            f"Cantidad de reposición: {lista[0][1]}\n"
            f"Cantidad de reprobados: {lista[0][2]}\n"
            f"Promedio del grupo: {lista[1]}")
def palidromoEnListaAuxiliar(pentrada):
    """
    Verifica si las palabras de una lista (`pentrada`) son palíndromos.
    Entradas:
        pentrada (list[str]): Lista de cadenas de caracteres (palabras).
    Retorna:
        str: Retorna un mensaje con la lista de entrada y el resultado del análisis de si las palabras son palíndromos o no.
    """
    resultados = funcionPalindromaLista(pentrada)
    return f"Entrada: {pentrada}\nResultado del análisis de palíndromos: {resultados}\n"
def multiplicarImpares():
    """
    Función de prueba que ejecuta `mutiplicarImparesLAuxiliar` con algunas listas de prueba.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime los resultados de la multiplicación de números impares de las listas de prueba.
    """
    print("--------------------------------------")
    print("Multiplicación de una lista de números")
    print("--------------------------------------")
    print(mutiplicarImparesLAuxiliar([8, 0, 6, 5, 0, 3]))
    print(mutiplicarImparesLAuxiliar([8, 2, 6, 8, 4]))
    print(mutiplicarImparesLAuxiliar([2, 3, 4, 5, 7]))
    menu()
def notasImaginarias():
    """
    Solicita al usuario notas para 10 estudiantes, luego ejecuta `notasImaginariasAuxiliar` con las notas.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime el resumen de las notas ingresadas (aprobados, reprobados, en reposición, y promedio).
    """
    listaNotas = []
    print("-----------------\nNotas imaginarias\n-----------------")
    for i in range(1, 11):
        nota = input(f"Nota del estudiante {i}:")
        if nota == "":
            nota = 0
        listaNotas.append(nota)
    print(notasImaginariasAuxiliar(listaNotas))
    menu()
def palindromaEnLista():
    """
    Función de prueba que ejecuta `palidromoEnListaAuxiliar` con algunas listas de prueba.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime los resultados del análisis de palíndromos de las listas de prueba.
    """
    print("--------------------")
    print("Lista de palíndromos")
    print("--------------------")
    print(palidromoEnListaAuxiliar(["ana", "comida", "somos", "hola"]))
    print(palidromoEnListaAuxiliar(["ana", "comida", "somos", "hola", "radar", "oro", "mundo"]))
    print(palidromoEnListaAuxiliar([]))
    print(palidromoEnListaAuxiliar(["pato", "mora", "zapato", "cartera"]))
    menu()
def palindromaEnListaPersonal():
    """
    Solicita al usuario ingresar palabras para verificar si son palíndromos.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime los resultados del análisis de palíndromos de las palabras ingresadas por el usuario.
    """
    print("--------------------")
    print("Lista de palíndromos")
    print("--------------------")
    listaNueva = []
    print("Escriba una palabra para saber si es palíndroma")
    while True:
        entrada = input()
        if entrada == "":
            break
        listaNueva.append(entrada)
    print(palidromoEnListaAuxiliar(listaNueva))
    menu()
def mutiplicarImparesListaPersonal():
    """
    Solicita al usuario ingresar números para multiplicar los impares.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime los resultados de la multiplicación de números impares ingresados por el usuario.
    """
    print("---------------------------------------")
    print("Multiplicación de impares personalizado")
    print("---------------------------------------")
    listaNueva = []
    print("Digite números para multiplicar los números impares")
    while True:
        try:
            entrada = int(input())
            if entrada == 0:
                break
            listaNueva.append(entrada)
        except ValueError:
            print("Dato incorrecto")
            menu()
    print(mutiplicarImparesLAuxiliar(listaNueva))
    menu()
def solicitarNumeroEdades():
    """
    Solicita al usuario cuántas edades desea ingresar.
    Entradas:
        Ninguna.
    Retorna:
        int: Devuelve la cantidad de edades que el usuario desea ingresar.
    """
    numEdades = int(input("\n¿Cuántas edades desea ingresar?: "))
    return numEdades
def ingresarEdades(numEdades):
    """
    Ingresa las edades una por una en una lista.
    Entradas:
        numEdades (int): Cantidad de edades que se ingresarán.
    Retorna:
        list[int]: Devuelve una lista con las edades ingresadas.
    """
    edades = []
    for i in range(1, numEdades + 1):
        edad = int(input(f"Ingrese la edad {i}: "))
        edades.append(edad)
    return edades
def mostrarInformacion(edadMayor, edadMenor, annosNacimiento, esBisiestoLista, edades):
    """
    Muestra información sobre las edades ingresadas y realiza análisis sobre ellas.
    Entradas:
        edadMayor (int): La edad mayor encontrada en la lista.
        edadMenor (int): La edad menor encontrada en la lista.
        annosNacimiento (list[int]): Lista de años de nacimiento calculados para cada edad.
        esBisiestoLista (list[bool]): Lista que indica si el año de nacimiento de cada persona es bisiesto.
        edades (list[int]): Lista de edades ingresadas.
    Retorna:
        Ninguna.
    Efecto secundario:
        Imprime información sobre las edades, incluyendo los años de nacimiento, si el año es bisiesto o no, y el rango de edades.
    """
    print(f"El menor nació en el año {annosNacimiento[edades.index(edadMenor)]}, por ende tiene {edadMenor} años.")
    print(f"El mayor nació en el año {annosNacimiento[edades.index(edadMayor)]}, por ende tiene {edadMayor} años. "
      f"Esta persona nació en {'año bisiesto' if esBisiestoLista[edades.index(edadMayor)] else 'año no bisiesto'}.")
    print(f"Entre ellos hay {edadMayor - edadMenor} años de diferencia y entre este rango entonces se encuentran las edades:")
    for i, edad in enumerate(sorted(edades), 1):
        print(f"Edad {i}: {edad}")
def unirEdades():
    """
    Ejecuta el flujo de solicitud de edades, cálculo de datos y muestra de información para las edades ingresadas.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    """
    numEdades = solicitarNumeroEdades()
    edades = ingresarEdades(numEdades)
    edadMayor, edadMenor = determinarEdadMayorMenor(edades)
    annosNacimiento, esBisiestoLista = calcularAnnosDeNacimiento(edades)
    mostrarInformacion(edadMayor, edadMenor, annosNacimiento, esBisiestoLista, edades)
def menu():
    """
    Muestra el menú al usuario y permite elegir una opción para ejecutar una función.
    Entradas:
        Ninguna.
    Retorna:
        Ninguna.
    """
    print("----\nMenú\n----")
    print("1 - Multiplicación de números impares de una lista, tú creas")
    print("2 - Palabras en una lista palíndromas que tú creas")
    print("3 - Notas imaginarias")
    print("4 - La edad de mis conocidos")
    print("5 - Multiplicar impares prueba del folleto")
    print("6 - Palabras palíndromas prueba del folleto")
    opcion = int(input("¿Cuál opción eliges?: "))
    if opcion == 1:
        mutiplicarImparesListaPersonal()
    elif opcion == 2:
        palindromaEnListaPersonal()
    elif opcion == 3:
        notasImaginarias()
    elif opcion == 4:
        unirEdades()
    elif opcion == 5:
        multiplicarImpares()
    elif opcion == 6:
        palindromaEnLista()


# Programa principal
menu()
