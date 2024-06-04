#Elaborado por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 4-42024
#Fecha de ultima modificación 6-4-2024
#Version 3.12.2 64-bits
#Importacion de librerias
from funciones import *
#Importacion de funciones salidas, entradas y verificaciónes
def auxiliarTarjeta(pentrada):
    """
    Función auxiliar para validar los símbolos de la tarjeta.
    Parámetros:
        pentrada: Cadena de entrada que contiene los símbolos de la tarjeta.
    Return: 
        Un mensaje que muestra la información de la tarjeta si la entrada es válida, de lo contrario, muestra un mensaje de error.
    Salidas:
        Prints con la información de la tarjeta o mensajes de error.
    """
    if len(pentrada) == 0:
        print("Debe ingresar un texto para poder decodificar.")
        definirTarjeta()
    elif pentrada == "micro":
        return 'El texto brindado no es posible de decodificar.'
    else:
        listaCaracteristicas = funcionTarjeta(pentrada)
        return (f"Usted está usando:\n"
                f"{listaCaracteristicas[0]}\n{listaCaracteristicas[1]}\n{listaCaracteristicas[2]}\n"
                f"{listaCaracteristicas[3]}")
def auxiliarVarilla(pentrada):
    """
    Función auxiliar para validar la nomenclatura de la varilla.
    Parámetros:
        pentrada: Cadena de entrada que contiene la nomenclatura de la varilla.
    Return:
        Un mensaje que muestra la información de la varilla si la entrada es válida, de lo contrario, muestra un mensaje de error.
    Salidas:
        Prints con la información de la varilla o mensajes de error.
    """
    if len(pentrada) != 6:
        return("El texto debe tener exactamente 6 caracteres.")
    if not pentrada[:2].isupper():
        return("Los dos primeros caracteres no son mayúsculas.")
    if pentrada[2] not in ['3', '4', '5', '6', '8']:
        return("El diámetro de entrada no es un valor permitido.")
    if pentrada[3] not in ['S', 'W']:
        return("El proceso de fabricación no es un valor permitido.")
    if pentrada[4:] not in ['40', '60', '70']:
        return("El grado de entrada no es un valor permitido.")   
    listaVarilla = funcionVarilla(pentrada)
    return (f"{COLOR_RED}{listaVarilla[0]}\n{COLOR_BLUE}{listaVarilla[1]}\n{COLOR_YELLOW}{listaVarilla[2]}\n{COLOR_GREEN}{listaVarilla[3]}{COLOR_RESET}")
def auxiliarLeonisa(pentrada):
    """
    Función auxiliar para validar el código de Leonisa.
    Parámetros: mi2
        pentrada: Cadena de entrada que contiene el código de Leonisa.
    Return:
        Mensaje de error si hay problemas con el código, o llamada a la función funcionLeonisaMenu si el código es válido.
    Salidas:
        String
    """
    if len(pentrada) != 10:
        return("El código debe ser de 10 caracteres.\n")
    if not pentrada[:5].isdigit():
        return("El código debe empezar con 5 números.\n")
    if not pentrada[5:7].isalpha() or pentrada[5:7] != pentrada[5:7].upper():
        return("El color debe estar en mayúsculas.\n")
    if pentrada[5:7].upper() not in ['BL', 'WH', 'BG', 'RD', 'BE']:
        return("El color no es un valor permitido.\n")
    if pentrada[7:9] not in ['32', '34', '36', '38', '40', '42', '44']:
        return("La talla no es un valor permitido.\n")
    if not pentrada[9].isupper() or pentrada[9] not in ['A', 'B', 'C', 'D', 'E']:
        return("La copa no es un valor permitido.\n")
    if funcionLeonisaMenu(pentrada):
        definirLeonisa()
    else:
        menu()
def definirTarjeta():
    """
    Función que solicita al usuario los símbolos de la tarjeta y muestra información sobre la tarjeta.
    Parámetros: No tiene.
    Return: No tiene.
    Salidas: Prints con la información de la tarjeta o mensajes de error.
    """
    print("-------------------")
    print("Simbolos de tarjeta")
    print("-------------------")
    print("Dame los símbolos de la tarjeta, como se muestra en su tarjeta SD")
    entrada = input("Escíbalo aquí: ")
    print(auxiliarTarjeta(entrada))
    menu()
def definiVarilla():
    """
    Función que solicita al usuario la nomenclatura de la varilla y muestra información sobre la varilla.
    Parámetros: No tiene.
    Return: No tiene.
    Salidas: Prints con la información de la varilla o mensajes de error.
    """
    nomenclaturaVarilla = input("Ingrese la nomenclatura de la varilla: ")
    print(auxiliarVarilla(nomenclaturaVarilla))
    menu()
def definirLeonisa():
    """
    Función que solicita al usuario el código a descifrar y muestra información sobre el código de Leonisa.
    Parámetros: No tiene.
    Return: No tiene.
    Salidas: Prints con información sobre el código de Leonisa o mensajes de error.
    """
    entrada = input("Ingrese el código a descifrar: ")
    print(auxiliarLeonisa(entrada))
    menu()
def menu():
    """
    Función que muestra un menú de opciones y realiza diferentes acciones dependiendo de la opción seleccionada por el usuario.
    Parámetros: No tiene.
    Return: No tiene.
    Salidas: Prints con el menú y mensajes de error.
    """
    print("--------------------")
    print("Menu de Labs-Strings")
    print("--------------------")
    print("1-Nomenclatura de varilla de construcción\n2-Símbolos de tarjeta\n3-Leonisa")
    opcion = input("Opción: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            definiVarilla()
        elif opcion == 2:
            definirTarjeta()
        elif opcion == 3:
            definirLeonisa()
        else:
            print("Es una opción inválida")
            menu()
    else:
        print("La opción ingresada no es un número entero.")
        menu()
#Programa principal
menu()