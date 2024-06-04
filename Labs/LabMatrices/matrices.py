#Elaborado Hector Leiva y Mauricio Cortes
#Creado el 18-4-2024
#Modificado el 18-4-2024
#Veersion 3.12.2 64-bits Visual Studio Code
from funciones import *

def crearEdificioAux(fila, columnas):
    """
    Crea una matriz que representa un edificio con `fila` número de filas y `columnas` número de columnas.
    Entradas:
        fila (int): número de filas del edificio.
        columnas (int): número de columnas del edificio. 
    Salidas:
        list of list: Retorna la matriz que representa el edificio o `None` si `fila` o `columnas` son valores negativos.
    """
    if fila < 0 or columnas < 0:
        return None  # Retorna None si los valores son negativos
    else:
        # Retorna la matriz del edificio creada por `funcionCrearEdificio`
        return funcionCrearEdificio(fila, columnas)
def modificarRentaAux(fila, columna, precio, edificio):
    """
    Modifica la renta de un apartamento específico en el edificio.
    Entradas:
        fila (int): índice de la fila (piso) del apartamento.
        columna (int): índice de la columna del apartamento.
        precio (int): nuevo precio de la renta del apartamento.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna un mensaje indicando el resultado de la operación.
    """
    # Verifica los índices de fila y columna
    if fila < 0 or columna < 0 or fila >= len(edificio) or columna >= len(edificio[fila]):
        return "El piso o el apartamento no existe"
    if edificio[fila][columna]==0 or edificio[fila][columna]==precio:
        return "El espacio no esta habitado"
    return funcioModificarApartamento(fila,columna,precio,edificio)
def crearEdificio():
    """
    Solicita al usuario los valores necesarios para crear un edificio y lo crea llamando a la función `crearEdificioAux`.
    Entradas:
        No tiene entradas directas (recibe entradas de usuario). 
    Salidas:
        list of list: Retorna la matriz que representa el edificio o imprime un mensaje de error.
    """
    print("-------------\nCrear Edificio\n-------------")
    fila = int(input("Cuántas filas tiene tu edificio: "))
    columna = int(input("Cuántas columnas tiene tu edificio: "))
    edificio = crearEdificioAux(fila, columna)
    if edificio is None:
        print("Error: No se pudo crear el edificio.")
    else:
        print("Edificio creado!")
    return edificio
def modificarRenta(edificio):
    """
    Permite al usuario modificar la renta de un apartamento en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        print de "Modificacion con exito"
    """
    fila = int(input("Cuál apartamento quieres modificar la rentar: "))
    columna = int(input("Cuál es el número de apartamento: "))
    fila-=1
    columna-=1
    precio = int(input("Cuál sería el monto a cambiar: "))
    opcion=input("Estas seguro de los cambios [Si]/[No]: ")
    if opcion.lower()=="si":
        print(modificarRentaAux(fila, columna, precio, edificio))
    else:
        print("Los cambios no se realizaron")
def alquilerAux(fila, columna, precio, edificio):
    """
    Permite rentar un apartamento específico en el edificio.
    Entradas:
        fila (int): índice de la fila (piso) del apartamento.
        columna (int): índice de la columna del apartamento.
        precio (int): precio de la renta del apartamento.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna un mensaje indicando el resultado de la operación.
    """
    if fila < 0 or columna < 0 or fila >= len(edificio) or columna >= len(edificio[fila]):
        return "El apartamento ya esta ocupado"
    return funcioModificarApartamento(fila,columna,precio,edificio)
def alquiler(edificio):
    """
    Permite al usuario rentar un apartamento en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        print de "Modificacion con exito"
    """
    fila = int(input("Cuál apartamento quieres rentar: "))
    columna = int(input("Cuál es el número de apartamento: "))
    fila-=1
    columna-=1
    if 0 <= fila < len(edificio) and 0 <= columna < len(edificio[fila]):
        if edificio[fila][columna]==0:
            precio = int(input("Cuál sería el monto a cambiar: "))
            opcion=input("Estas seguro de los cambios [Si]/[No]: ")
            if opcion.lower()=="si":
                resultado = alquilerAux(fila, columna, precio, edificio)
                print(resultado)
            else:
                print("Los cambios no se realizaron")
        else:
            print("El apartamento ya se esta alquilando")
    else:
        print("El apartamento no existe")
def desalojarAux(fila, columna, precio, edificio):
    """
    Permite desalojar un apartamento específico en el edificio.
    Entradas:
        fila (int): índice de la fila (piso) del apartamento.
        columna (int): índice de la columna del apartamento.
        precio (int): nuevo precio de la renta (cero para desalojar).
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna un mensaje indicando el resultado de la operación.
    """
     # Verifica los índices de fila y columna
    if fila < 0 or columna < 0 or fila >= len(edificio) or columna >= len(edificio[fila]):
        return "El piso o el apartamento no existe"
    if edificio[fila][columna]==0:
        return "El espacio debe de ser habitado"
    return funcioModificarApartamento(fila,columna,precio,edificio)
def desalojar(edificio):
    """
    Permite al usuario desalojar un apartamento en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        print de "Modificacion con exito"
    """
    fila = int(input("Cuál apartamento quieres desalojar: "))
    columna = int(input("Cuál es el número de apartamento: "))
    fila-=1
    columna-=1
    opcion=input("Estas seguro de los cambios [Si]/[No]: ")
    if opcion.lower()=="si":
        print(modificarRentaAux(fila, columna, 0, edificio))
    else:
        print("Los cambios no se realizaron")
def apartamentoPrecioAux(fila,columna,edificio):
    """
    Obtiene el precio del alquiler de un apartamento específico en el edificio.
    Entradas:
        fila (int): índice de la fila (piso) del apartamento.
        columna (int): índice de la columna del apartamento.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        int: Retorna el precio del alquiler del apartamento o un mensaje de error.
    """
    if fila < 0 or columna < 0 or fila >= len(edificio) or columna >= len(edificio[fila]):
        return "El piso o el apartamento no existe"
    return edificio[fila][columna]
def apartamentoPrecio(edificio):
    """
    Permite al usuario obtener el precio del alquiler de un apartamento específico en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio.
    Salidas:
        None
    """
    fila = int(input("Cuál piso quieres rentar: "))
    columna = int(input("Cuál es el número de apartamento: "))
    print(f"El precio del alquiler es: ${apartamentoPrecioAux(fila-1,columna-1,edificio)} de apartamento {fila}-{columna}")
def mensualPisoAux(fila,edificio):
    """
    Calcula los ingresos por alquiler de un piso específico en el edificio.
    Entradas:
        fila (int): índice de la fila (piso).
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        int: Retorna los ingresos totales por alquiler del piso o un mensaje de error.
    """
    if fila-1<0 or fila-1>=len(edificio[0]):
        return "El piso no existe"
    return funcionMensualPiso(fila,edificio)
def mensualPiso(edificio):
    """
    Permite al usuario obtener los ingresos por alquiler de un piso específico en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        print de confirmacion de la modificacion
    """
    fila = int(input("Cuál piso quieres ver sus ingresos: "))
    print(mensualPisoAux(fila, edificio))
def mensualColumnaAux(columna,edificio):
    """
    Calcula los ingresos por alquiler de una columna específica en el edificio.
    Entradas:
        columna (int): índice de la columna.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        int: Retorna los ingresos totales por alquiler de la columna o un mensaje de error.
    """
    if columna-1<0 or columna-1>=len(edificio):
        return "La columna no existe"
    return funcionMensualColumna(columna,edificio)
def mensualColumna(edificio):
    """
    Permite al usuario obtener los ingresos por alquiler de una columna específica en el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio.
    Salidas:
        print de los ingresos de cada columna
    """
    columna = int(input("Cuál columna quieres ver sus ingresos: "))
    print(mensualColumnaAux(columna, edificio))
def mensualEdificio(edifcio):
    """
    Calcula los ingresos totales por alquiler de todo el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        int: Retorna los ingresos totales por alquiler de todo el edificio.
    """
    print(funcionEdificio(edifcio))
def reporteEdificio(edificio):
    """
    Genera un reporte del edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        print reporte del edificio completo
    """
    print(funcionReporteEdificio(edificio))
def menu(): 
    """
    Genera un menu para moverse
    Entradas: None
    Salida: None
    """
    edificio = None  # Inicialización de `edificio` con un valor predeterminado
    edificio = crearEdificio()
    while True:
        print("----\nMenu\n----")
        opcion = int(input("1-Ingresar nuevo inquilino \n2-Modificar renta\n3-Desalojar\n4-Indicar ingreso por alquiler:\n5-Reporte del edificio\n"
                           "6-Salida del programa\n:"))
        if opcion == 1:
            alquiler(edificio)
        elif opcion == 2:
            modificarRenta(edificio)
        elif opcion==3:
            desalojar(edificio)
        elif opcion==4:
            opcion = int(input("1-Por apartamento\n2-Por piso\n3-Por columna\n4-Por Edificio\n:"))
            if opcion==1:
                apartamentoPrecio(edificio)
            elif opcion==2:
                mensualPiso(edificio)
            elif opcion==3:
                mensualColumna(edificio)
            elif opcion==4:
                mensualEdificio(edificio)
            else:
                menu()
        elif opcion==5:
            reporteEdificio(edificio)
        elif opcion==6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            menu()
menu()
