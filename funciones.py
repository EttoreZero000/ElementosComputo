# Función para determinar si un año es bisiesto
def esBisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

# Función para calcular los años de nacimiento correspondientes y si son bisiestos o no
def calcularAnnosDeNacimiento(edades):
    annoActual = 2024
    annosNacimiento = [annoActual - edad for edad in edades]
    esBisiestoLista = [esBisiesto(anno) for anno in annosNacimiento]
    return annosNacimiento, esBisiestoLista

# Función para determinar la edad mayor y la edad menor
def determinarEdadMayorMenor(edades):
    edadMayor = max(edades)
    edadMenor = min(edades)
    return edadMayor, edadMenor
