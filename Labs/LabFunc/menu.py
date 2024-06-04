#Elaborador por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 14-3-2024
#Ultima modificacion 15-3-2024
#Version: 3.12.2 64-bit

#Librerias importadas
from funciones import *
#Funcion para verificar datos del señor del carro
def ingresoDelCarroAux(pingreso):
    """
    Función para verificar los datos entrantes que sean enteros

    Parámetros:
    pingreso (int): Es el ingreso del señor del carrito

    Returns:
    f-string: Es una cadena de texto que forma una tabla que indica:
    Cantidad de ventas y cantidad de dinero dependiendo de la cantidad de,
    500 o menor,
    entre 500 y 800 y
    1.000 o mayor

    Función que se llama dentro:
    calcularDelCarro()
    """
    if type(pingreso) != int:
        return "¡Debe indicar un valor entero!"
    elif pingreso < 0:
        return "¡Debe indicar un valor positivo!"
    elif pingreso == 0:
        listaVentas = calcularDelCarro(pingreso)
        return f"""
            |{'Tipo de venta':^25}|{'Cantidad de ventas':^20}|{'Cantidad de dinero':^20}|
            |{'500 o menor':^25}|{listaVentas[0]:^20}|{listaVentas[3]:^20}|
            |{'Entre 500 y 800':^25}|{listaVentas[1]:^20}|{listaVentas[4]:^20}|
            |{'1.000 o mayor':^25}|{listaVentas[2]:^20}|{listaVentas[5]:^20}|
            """

    else:
        calcularDelCarro(pingreso)
        return "Valor ingresado con éxito"
#Funcion para la entrada de datos del señor del carro
def ingresoDelCarro():
    """
    Función para pedir los datos al señor del carrito e imprimir datos

    Parámetros:
    Ninguno
    Returns:
    Salida: Una tabla con los datos ordenados
    """
    print(f"{'------------------':^25}")
    print(f"{'El señor del carro':^25}")
    print(f"{'------------------':^25}")

    while True:  # Bucle infinito hasta que se ingrese un valor válido
        try:
            ingreso = int(input("Ingrese la cantidad de venta actual, si terminó el día, digite 0: "))
            print(ingresoDelCarroAux(ingreso))
            if ingreso == 0:
                break  # Sale del bucle si se ingresa 0
        except ValueError:
            print("Debe ingresar un número entero válido.")
#Funcion para verificar datos de JUDUCA
def ingresoJuducaAux(pingreso, pedad, ppais, pmedallas):
    """
    Función para verificar los datos entrantes que sean enteros

    Parámetros:
    pingreso (int): 1.Hombre 2.Mujer
    pedad (int): La edad del participante
    ppais (int): El país del participante
    pmedallas (int): Medallas del participante
    Returns:
    f-string: Es una cadena de texto que forma una tabla que indica:
    Cantidad de hombres, mujeres, Mujeres con medalla con oro,
    Hombres con oro menores a 25 y estudiantes de Costa Rica

    Función que se llama dentro:
    calcularJuduca()
    """
    if type(pingreso) != int or type(pedad) != int or type(ppais) != int or type(pmedallas) != int:
        return "Debe indicar un valor entero!"
    elif pingreso < 0 or pedad < 0 or ppais < 0 or pmedallas < 0:
        return "Debe indicar un valor positivo"
    elif pingreso == 0:
        result = calcularJuduca(pingreso, pedad, ppais, pmedallas)
        return (f"|{'Hombres':^25}|{'Mujeres':^25}|{'Mujeres con oro':^25}|{'Hombres con oro':^25}|{'Estudiantes Costa Rica':^25}|\n"
                f"|{result[0]:^25}|{result[1]:^25}|{result[2]:^25}|{result[3]:^25}|{result[4]:^25}|")
    else:
        calcularJuduca(pingreso, pedad, ppais, pmedallas)
        return "Datos ingresados correctamente"
#Funcion para la entrada de datos de JUDUCA
def ingresoJuduca():
    """
    Función para pedir los datos de los participantes y enviar los datos a otras funciones

    Parámetros:
    Returns:
    Salida: Una tabla con los datos ordenados
    Función que se llama dentro:
    ingresoJuducaAux()
    """
    print(f"{'------':^25}")
    print(f"{'JUDUCA':^25}")
    print(f"{'------':^25}")
    try:
        print("¿Eres hombre o mujer?")
        ingreso = int(input("1. Hombre \n2. Mujer\n0. Terminar\n"))
        if ingreso == 0:
            print(ingresoJuducaAux(ingreso, 0, 0, 0))
            main()
        edad = int(input("¿Cuántos años tienes?: "))
        pais = int(input("¿Qué país participa?\n1.Guatemala\n2.El Salvador\n3.Panamá\n4.Costa Rica\n5.Honduras\n6.Belice\n7.República Dominicana\n8.Nicaragua\n"))
        medallas = int(input("¿Cuántas medallas has ganado?: "))
        print(ingresoJuducaAux(ingreso, edad, pais, medallas))
        ingresoJuduca()
    except ValueError:
        print("Debe ingresar un número entero válido")
        ingresoJuduca()
#Funcion para verificar datos Fotocopiadora
def ingresoImprecioAux(pingreso, pcantidad, pdato, pcolor):
    """
    Función para verificar los datos entrantes que sean enteros o un string

    Parámetros:
    pingreso (int): 1.Impresión 2.Escáner
    pcantidad (int): Cantidad de imprimir o escanear
    pdato (int) o (str): Dependiendo del ingreso, verificará como debe
    pcolor (int): 1.Blanco o negro, 2.Color
    Returns:
    f-string: Es una cadena de texto que forma una tabla que indica:
    Impresión:
    |Tipo de papel|Calidad|Cantidad|Costo|
    Escanear:
    |Cantidad de papel|Costo|Correo|

    Función que se llama dentro:
    calcularEscaneoOImprimir()
    """
    if type(pingreso) != int or type(pcantidad) != int or type(pdato) != int or type(pcolor) != int:
        if type(pdato) != str:
            return "Debe indicar un valor válido!!"
        elif pingreso < 0 or pcantidad < 0 or pcolor < 0:
            return "Debe indicar valores mayores a 0!!"
        else:
            result = calcularEscaneoOImprimir(pingreso, pcantidad, pdato, pcolor)
            return (f"|{'Cantidad de papel':^20}|{'Costo':^20}|{'Correo':^40}|\n"
                    f"|{result[0]:^20}|{result[1]:^20}|{result[2]:^40}|")
    elif pingreso < 0 or pcantidad < 0 or pdato < 0 or pcolor < 0:
        return "Debe indicar valores mayor a 0!!"
    elif pdato == 2 and pcolor == 1:
        return "Papel Couché a blanco y negro no existe"
    elif pdato > 3 or pcolor > 2:
        return "Debe indicar un valor válido!!"
    else:
        result = calcularEscaneoOImprimir(pingreso, pcantidad, pdato, pcolor)
        return (f"|{'Tipo de papel':^20}|{'Calidad':^20}|{'Cantidad':^20}|{'Costo':^20}|\n"
                f"|{result[0]:^20}|{result[1]:^20}|{result[2]:^20}|{result[3]:^20}|")
#Funcion para la entrada de datos Fotocopiadora
def ingresoImprecion():
    """
    Función para la entrada de datos y la impresión de estos en una tabla

    Parámetros:
    Returns:
    Salida: Una tabla con los datos ordenados

    Función que se llama dentro:
    ingresoImprecioAux()
    """
    print(f"{'-----------------------------------------------------------------':^25}")
    print(f"{'Ganancias al cierre diario del Centro de Impresiones por Registro':^25}")
    print(f"{'-----------------------------------------------------------------':^25}")
    try:
        ingreso = int(input(("¿Quieres hacer una:\n1.Impresión\n2.Escaneo\n")))
        if ingreso == 2:
            cantidad = int(input("¿Cuántas páginas vas a escanear?: "))
            tipo = input("¿Cuál es tu correo electrónico?: ")
            print(ingresoImprecioAux(ingreso, cantidad, tipo, 1))
        elif ingreso == 1:
            tipo = int(input("¿Cuál es tu tipo de impresión?:\n1.Papel tradicional.\n2.Papel Couché.\n3.Papel autoadhesivo.\n"))
            cantidad = int(input("¿Cantidad de hojas para imprimir?\n"))
            color = int(input("¿Lo quieres a \n1.Blanco y negro\n2.Color\n"))
            print(ingresoImprecioAux(ingreso, cantidad, tipo, color))
    except ValueError:
        print("Debe ingresar un número entero válido!!")
        ingresoImprecion()
#Funcion principal y menu
def main():
    print("-----------------------------")
    print("Menu de Laboratorio Funciones")
    print("-----------------------------")
    print("1. El señor del carrito. \n2. JUDUCA \n3. Ganancia a cierre del Centro Impresiones")
    opcion = int(input("Escoja una opción: "))
    if 0 < opcion < 4:
        if opcion == 1:
            ingresoDelCarro()
        elif opcion == 2:
            ingresoJuduca()
        elif opcion == 3:
            ingresoImprecion()
        else:
            return
    else:
        print("Opción inválida, indique una de las siguientes opciones.")
    main()
#Inicia el programa
main()
