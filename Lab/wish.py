#Elaborado por Hector leiva y Mauricio Cortes
#Fecha de creaccion 25/04/2024
#Fecha de modificion 8/05/2024
#Version 3.12.2 64-bits

#Funciones importadas
from funciones import *
import pickle
from archivos import *
#funciones
def insertarPaqueteAux(numeroPaquete, numeroTelefonico, sucursal):
    """
    Inserta un nuevo paquete en el sistema.
    Parámetros:
    - numeroPaquete (int): El número del paquete.
    - numeroTelefonico (int): El número de teléfono asociado al paquete.
    - sucursal (str): El nombre de la sucursal asociada al paquete.
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    if numeroPaquete < 1:
        return "El numero de paquete debe de ser mayor a 0"
    elif len(str(numeroTelefonico)) != 8:
        return "El numero de telefono debe de ser 8 numeros enteros"
    elif len(sucursal) < 6:
        return "La sucursal debe de tener mas de 5 caracteres"
    elif str(validarPaquete(numeroPaquete)) in "123":
        print("El paquete ya existe")
        return
    else:
        return funcionInsertarPaquete(numeroPaquete, numeroTelefonico, sucursal, 10, 1)
def actualizarPaqueteAux(opcion, opcion2, numeroPaquete):
    """
    Actualiza el estado de un paquete en el sistema.
    Parámetros:
    - opcion (int): La opción de actualización (1, 2 o 3).
    - opcion2 (int): La confirmación de la actualización (1 o 2).
    - numeroPaquete (int): El número del paquete a actualizar.
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    if str(opcion) in "123":
        if opcion2 == 2:
            return "Los cambios no se realizaron"
        elif opcion2 == 1:
            return funcionactualizarPaquete(opcion, numeroPaquete)
def eliminarPaqueteAux(numeroPaquete, opcion):
    """
    Elimina un paquete del sistema.
    Parámetros:
    - numeroPaquete (int): El número del paquete a eliminar.
    - opcion (int): La opción de confirmación (1 o 2).
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    if opcion == 1:
        return funcionEliminarPaquete(numeroPaquete)
    elif opcion == 2:
        return "No se realizaron cambios"
    else:
        return f"{opcion} este no es un valor valido"
def paquetesTotalesTelefonoAux(telefono,archivo):
    """
    Obtiene el total de paquetes asociados a un número de teléfono.
    Parámetros:
    - telefono (int): El número de teléfono.
    Retorna:
    - str: Un mensaje indicando el total de paquetes asociados al número de teléfono.
    """
    if len(str(telefono)) != 8:
        return "El numero debe de ser igual a 8 digitos"
    else:
        return funcionPaquetesTotalesTelefono(telefono,archivo)
def paquetesTotalesAux(archivo):
    """
    Obtiene el total de paquetes en el sistema.
    Retorna:
    - int: El total de paquetes.
    """
    return funcionPaquetesTotales(archivo)
def insertarPaquete():
    """
    Solicita al usuario información para insertar un nuevo paquete en el sistema.
    Retorna:
    - None
    """
    numeroPaquete = int(input("Numero de paquete: "))
    numeroTelefonico = int(input("Numero telefonico: "))
    sucursal = input("Sucursal: ")
    print(insertarPaqueteAux(numeroPaquete, numeroTelefonico, sucursal))
def actualizarPaquete():
    """
    Solicita al usuario información para actualizar el estado de un paquete en el sistema.
    Retorna:
    - None
    """
    numeroPaquete = int(input("Numero de paquete: "))
    if str(validarPaquete(numeroPaquete)) in "123":
        print(f"Estado actual del paquete es: {validarPaquete(numeroPaquete)}\n1-Por entregar, cambia a 5 dias\n2-Entregado, cambia a 0 dias"
                f"\n3-Devuelto cambia a 0 dias")
        opcion = int(input("Opcion: "))
        print("Estas seguro de cambiar el estado del paquete, 1-Si, 2-No")
        opcion2 = int(input(":"))
        print(actualizarPaqueteAux(opcion, opcion2, numeroPaquete))
    else:
        print("El paquete no se encontro")
def eliminarPaquete():
    """
    Solicita al usuario información para eliminar un paquete del sistema.
    Retorna:
    - None
    """
    numeroPaquete = int(input("Numero de paquete: "))
    if str(validarPaquete(numeroPaquete)) in "123":
        opcion = int(input("Estas seguro de eliminar el paquete 1-Si, 2-No\nOpcion: "))
        print(eliminarPaqueteAux(numeroPaquete, opcion))
    else:
        print("El paquete no existe")
def paquetesTotales(archivo):
    """
    Muestra el total de paquetes en el sistema.
    Retorna:
    - None
    """
    print(f"Total de paquetes: {paquetesTotalesAux(archivo)}")
def paquetesTotalesTelefono(archivo):
    """
    Solicita al usuario un número de teléfono y muestra la cantidad de paquetes asociados a ese número.
    Retorna:
    - None
    """
    telefono = int(input("Cual telefono quieres ver sus paquetes: "))
    print(f"La cantidad de paquetes son: {paquetesTotalesTelefonoAux(telefono,archivo)}")
def menu():
    archivo=lee("inventario")
    """
    Presenta al usuario un menú de opciones y ejecuta la opción seleccionada.
    Retorna:
    - None
    """
    print("---------------------")
    print("1-Insertar paquetes\n2-Actualizar paquetes\n3-Eliminar paquete\n4-Paquetes totales\n5-Paquetes totales en un numero telefonico\n6-Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        insertarPaquete()
    elif opcion == 2:
        actualizarPaquete()
    elif opcion == 3:
        eliminarPaquete()
    elif opcion == 4:
        paquetesTotales(archivo)
    elif opcion == 5:
        paquetesTotalesTelefono(archivo)
    elif opcion == 6:
        return
    menu()
menu()