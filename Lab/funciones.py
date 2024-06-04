from archivos import *
diccionario={}
def funcionInsertarPaquete(numeroPaquete, numeroTelefonico, sucursal, dias, estado):
    """
    Inserta un nuevo paquete en el sistema.
    Parámetros:
    - numeroPaquete (int): El número del paquete.
    - numeroTelefonico (int): El número de teléfono asociado al paquete.
    - sucursal (str): El nombre de la sucursal asociada al paquete.
    - dias (int): La cantidad de días hábiles asociados al paquete.
    - estado (int): El estado del paquete (1, 2 o 3).
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    numeroTelefonico = int(numeroTelefonico)
    datosPersona = [numeroTelefonico, sucursal, dias, estado]
    diccionario[numeroPaquete] = datosPersona
    graba("inventario",diccionario)
    return "Datos ingresados correctamente"
def validarPaquete(numeroPaquete):
    """
    Valida la existencia de un paquete en el sistema.
    Parámetros:
    - numeroPaquete (int): El número del paquete a validar.
    Retorna:
    - int o str: El estado del paquete (1, 2 o 3) si se encuentra, de lo contrario, un mensaje de error.
    """
    try:
        datosPaquete = diccionario[numeroPaquete]
        return datosPaquete[3]
    except KeyError:
        return "No se encontró un paquete"
def funcionactualizarPaquete(opcion, numeroPaquete):
    """
    Actualiza el estado de un paquete en el sistema.
    Parámetros:
    - opcion (int): La opción de actualización (1, 2 o 3).
    - numeroPaquete (int): El número del paquete a actualizar.
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    datosPaquete = diccionario[numeroPaquete]
    datosPaquete[3] = opcion
    if opcion == 1:
        datosPaquete[2] = 5
    elif opcion == 2 or opcion == 3:
        datosPaquete[2] = 0
    diccionario[numeroPaquete] = datosPaquete
    graba("inventario",diccionario)
    return "Los cambios se realizaron"
def funcionEliminarPaquete(numeroPaquete):
    """
    Elimina un paquete del sistema.
    Parámetros:
    - numeroPaquete (int): El número del paquete a eliminar.
    Retorna:
    - str: Un mensaje indicando el resultado de la operación.
    """
    del diccionario[numeroPaquete]
    graba("inventario",diccionario)
    return f"Se ha eliminado el paquete {numeroPaquete}"
def funcionPaquetesTotales(archivo):
    """
    Muestra todos los paquetes en el sistema y su información.
    Retorna:
    - int: El total de paquetes en el sistema.
    """
    paquetes = 0
    for clave, lista in archivo.items():
        paquetes += 1
        if lista[3] == 1:
            Estado = "Por entregar"
        elif lista[3] == 2:
            Estado = "Entregado"
        elif lista[3] == 3:
            Estado = "Devuelto"
        print("------------------")
        print(f"Numero de paquete: {clave}\nNumero de telefono {lista[0]}\nSucursal {lista[1]}\nCantidad de dias habiles {lista[2]}\nEstado {Estado}")
        print("------------------")
    return paquetes 
def funcionPaquetesTotalesTelefono(telefono,archivo):
    """
    Muestra la información de los paquetes asociados a un número de teléfono específico.
    Parámetros:
    - telefono (int): El número de teléfono a consultar.
    Retorna:
    - int: El total de paquetes asociados al número de teléfono especificado.
    """
    paquetes = 0
    for clave, lista in archivo.items():
        # Verificar si el número telefónico está en la lista
        if telefono in lista:
            paquetes += 1
            if lista[3] == 1:
                Estado = "Por entregar"
            elif lista[3] == 2:
                Estado = "Entregado"
            elif lista[3] == 3:
                Estado = "Devuelto"
            print("----------------------")
            print(f"Numero de telefono {lista[0]}\nNumero de paquete: {clave}\nSucursal {lista[1]}\nCantidad de dias habiles {lista[2]}\nEstado {Estado}")
            print("----------------------")
    return paquetes