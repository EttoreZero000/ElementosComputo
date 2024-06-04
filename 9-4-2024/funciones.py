def funcionMultiplicarImparesL(pentrada):
    producto=1
    impar=False
    for a in pentrada:
        if not funcionEsPar(a):
            producto*=a
            impar=True
    if impar:
        return producto
    else:
        return 0
def funcionEsPar(pentrada):
    if pentrada%2==0:
        return True
    else:
        return False  
def funcionPalindroma(pentrada):
    pentrada=pentrada.lower()
    palabraNueva = ""
    for i in range(len(pentrada) - 1, -1, -1):
        palabraNueva += pentrada[i]

    if palabraNueva == pentrada:
        return True
    else:
        return False
def funcionPalindromaLista(pentrada):
    listaPalindroma=[]
    for palabra in pentrada:
        if funcionPalindroma(palabra):
            listaPalindroma.append(palabra)
    return listaPalindroma
def funcionNotasImaginarias(pentrada):
    conteos = [0, 0, 0]  # Inicializamos una lista para almacenar los conteos
    notasSumadas = 0
    for nota in pentrada:
        nota = int(nota)
        if nota > 70:
            conteos[0] += 1
        elif 70 >= nota >= 60:
            conteos[1] += 1
        else:
            conteos[2] += 1
        notasSumadas += nota
    return conteos, notasSumadas / len(pentrada)
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
