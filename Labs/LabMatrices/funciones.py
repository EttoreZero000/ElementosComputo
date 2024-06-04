def funcionCrearEdificio(fila, columnas):
    """
    Crea una matriz que representa un edificio con `fila` número de filas y `columnas` número de columnas.
    Inicializa todos los elementos de la matriz a 0.
    Entradas:
        fila (int): número de filas del edificio.
        columnas (int): número de columnas del edificio. 
    Salidas:
        list of list: Retorna una matriz bidimensional donde cada elemento es 0.
    """
    matriz=[]
    for i in range(fila):
        fila=[]
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return (matriz)
def funcioModificarApartamento(piso,apartamento,precio,edificio):
    """
    Modifica el precio de la renta de un apartamento específico en el edificio.
    Entradas:
        piso (int): índice del piso donde se encuentra el apartamento.
        apartamento (int): índice del apartamento que se va a modificar.
        precio (int): nuevo precio de la renta.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna un mensaje indicando el éxito de la operación.
    """
    # Modifica el precio de la renta
    edificio[piso][apartamento] = precio
    return "Cambios modificacion con exito"
def funcionMensualPiso(fila,edificio):
    """
    Calcula y muestra los ingresos por alquiler de un piso específico en el edificio.
    Entradas:
        fila (int): índice del piso que se va a consultar.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna el total de ingresos por alquiler de ese piso, incluyendo detalles de cada apartamento.
    """
    sumaPiso=0
    i=1
    for apartamento in edificio[fila-1]:
        sumaPiso+=int(apartamento)
        print(f"Piso: {fila}\nApartamento: {i}\nMonto de alquiler: {int(apartamento)}")
        i+=1
    return (f"Para un total de ingreso del {fila} de ${sumaPiso}")
def funcionMensualColumna(columna, edificio):
    """
    Calcula y muestra los ingresos por alquiler de una columna específica en el edificio.
    Entradas:
        columna (int): índice de la columna que se va a consultar.
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna el total de ingresos por alquiler de esa columna, incluyendo detalles de cada piso.
    """
    sumaColumna = 0
    piso = 1  # Inicializa el contador de pisos (empezando desde el primer piso)
    # Itera sobre cada fila en el edificio
    for fila in edificio:
        # Verifica si la columna existe en la fila actual
        if columna < len(fila):
            # Obtiene el monto de alquiler en la columna especificada
            monto_alquiler = fila[columna-1]
            # Suma el monto de alquiler al total de la columna
            sumaColumna += int(monto_alquiler)
            # Imprime la información del piso y el monto de alquiler en la columna
            print(f"Piso: {piso}\nApartamento: {columna}\nMonto de alquiler: {monto_alquiler}")
        piso += 1  # Incrementa el contador de pisos
    # Retorna la suma total de ingresos de la columna especificada
    return f"Para un total de ingreso de la columna {columna} es de ${sumaColumna}"
def funcionEdificio(edificio):
    """
    Calcula y muestra los ingresos totales por alquiler de todo el edificio.
    Entradas:
        edificio (list of list): matriz que representa el edificio. 
    Salidas:
        str: Retorna el total de ingresos por alquiler de todo el edificio, incluyendo detalles de cada piso y apartamento.
    """
    sumaEdificio=0
    piso=apartamento=1
    for i in edificio:
        apartamento=1
        for j in i:
            print(f"Piso: {piso}\nApartamento: {apartamento}\nMonto de alquiler: {j}")
            
            apartamento+=1
            sumaEdificio+=j
        piso+=1
    return f"Para un total de ganancia de ${sumaEdificio}"
def funcionReporteEdificio(edificio):
    """
    Genera un reporte del edificio mostrando los apartamentos alquilados y no alquilados.
    Entradas:
        edificio (list of list): matriz que representa el edificio.
    Salidas:
        str: Retorna un reporte con el número de apartamentos alquilados, no alquilados y sus porcentajes.
    """
    sumaApartado=sumaNoApartado=total=0
    for i in edificio:
        for j in i:
            if j == 0:
                sumaNoApartado+=1
            else:
                sumaApartado+=1
            total+=1
    return (f"Total de apartamentos alquilados: {sumaApartado}, para un porcentaje de: {(sumaApartado/total)*100}%\n"
            f"Total de apartamentos no alquilados: {sumaNoApartado}, para un porcentaje de: {(sumaNoApartado/total)*100}%")