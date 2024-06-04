#Elaborador por Hector Leiva y Mauricio Cortes
#Fecha 30/4/2024
#Fecha de ultima modificacion 30/4/2024
#Version 3.12.2 64bits


#Funciones
def esPrimoSegundo(numero,divisor):
    """
    Funcion par saber si es primo
    """
    if divisor <numero//2:
        if numero%divisor==0:
            return "No es primo"
        else:
            return esPrimoSegundo(numero,divisor+2)
    else:
        return True
def esPrimo(numero):
    """
    Funcion par saber si es primo
    """
    if numero==2:
        return True
    elif numero%2==0:
        return "No es primo"
    else:
        divisor=3
        return esPrimoSegundo(numero,divisor)
def validarMatriz(matriz):
    """
    Validar si es una matriz
    """
    for indiceLista in range(len(matriz)):
        if len(matriz[0])!=len(matriz[indiceLista]):
            return "No es matriz"
    return True
def validarEntradas(matriz,fila,columna):
    """
    Validar entradas
    """
    if str(fila).isdigit() and str(columna).isdigit():
        if len(matriz)>=fila or 0>=len(matriz):
            if 0<=columna<len(matriz[fila]):
                numero = len(matriz[fila])
                for filas in matriz:
                    if numero != len(filas):
                        return "La matriz es incorrecta"
                    try:
                        valorGuardado=matriz[fila][0]
                        matriz[fila][0]=0
                        matriz[fila][0]=valorGuardado
                    except:
                        return "Hay una tupla"
                return True
            else:
                return "La entrada de columna esta incorrecta"
        else:
            return "La entrada de fila esta mal"
    else:
        return "Los parametros tiene que ser enteros no flotantes"
def sacarPrimosMatriz(matriz,fila,columna):
        """
        Funcion para sacar los primos de la funcion
        """
        fila-=1
        columna-=1
        flag=validarEntradas(matriz,fila,columna)
        if type(flag)==str:
            return flag
        if validarEntradas(matriz,fila,columna):
            listaAyuda=[]
            for i in range(fila, len(matriz)):
                for j in range(columna, len(matriz[fila])):
                    if esPrimo(matriz[i][j]):
                        listaAyuda.append(matriz[i][j])
            return listaAyuda
#Programa principal
print(sacarPrimosMatriz([[23,20],[25,37,1],[50,24,58],[79,61,14]], 2, 1))  # El valor de entrada no es una matriz.
print(sacarPrimosMatriz([[23,20,17],(25,37,1),[50,24,58],[79,61,14]], 2, 1))  # Todos los elementos de la matriz deben ser listas.
print(validarEntradas([[23,20,17],[25,37,1],[50,24,58],[79,61,14]], "a", 1))  # Los datos para la fila y la columna deben ser enteros únicamente.
print(validarEntradas([[23,20,17],[25,37,1],[50,24,58],[79,61,14]], 5, 1))  # El número de fila solicitado excede la cantidad de filas de la matriz ingresada.
print(validarEntradas([[23,20,17],[25,37,1],[50,24,58],[79,61,14]], 1, 5))  # El número de columna solicitada excede la cantidad de columnas de la matriz ingresada.
print(sacarPrimosMatriz([[23,20,17],[25,37,1],[50,24,58],[79,61,14]], 2, 1))  # [37,79,61]
print(sacarPrimosMatriz([[15,97],[53,89],[43,10]], 1, 1))  # [97,53,89,43]
print(sacarPrimosMatriz([[37,1],[24,58],[61,14]], 2, 2))  # [37,61]
print(sacarPrimosMatriz([[7,6,12],[55,39,17]], 2, 3))  # [17]
print(sacarPrimosMatriz([[50,6],[55,39]], 1, 1))  # []