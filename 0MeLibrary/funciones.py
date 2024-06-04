import matplotlib.pyplot as plt
import networkx as nx
def funcionCompararMatrices(matriz1,matriz2):
    if len(matriz1) != len(matriz2):
        return False
    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            return False
    return True
def sumarMatrices(matriz1, matriz2):
    """
    Función para sumar dos matrices de igual tamaño.
    Args:
    matriz1 (list): La primera matriz.
    matriz2 (list): La segunda matriz.
    Returns:
    list: La matriz resultante de la suma.
    """
    if not funcionCompararMatrices(matriz1,matriz2):
        return ("Las matrices tiene que ser igual tamaño")
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma_elemento)
        resultado.append(fila_resultado)
    return resultado
def restaMatrices(matriz1, matriz2):
    """
    Función para sumar dos matrices de igual tamaño.
    Args:
    matriz1 (list): La primera matriz.
    matriz2 (list): La segunda matriz.
    Returns:
    list: La matriz resultante de la suma.
    """
    if not funcionCompararMatrices(matriz1,matriz2):
        return ("Las matrices tiene que ser igual tamaño")
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            suma_elemento = matriz1[i][j] - matriz2[i][j]
            fila_resultado.append(suma_elemento)
        resultado.append(fila_resultado)
    return resultado
def esPalindromo(letra):
    """
    Verifica si una letra es igual en su posición original y en su posición invertida.
    Args:
    letra (str): La letra a verificar.
    Returns:
    bool: True si la letra es igual en su posición original y en su posición invertida, False en caso contrario.
    """
    letra=letra.lower()
    return letra == letra[::-1]
def cuantasPalabras(frace):
    palabras=0
    marcador=False
    for letra in frace:
        if letra != " ":
            if not marcador:
                palabras+=1
                marcador=True
        else:
            marcador=False
    return palabras
def imprimirFila(fila,matriz):
    fila-=1
    filaStr=""
    for elemento in range(len(matriz[fila])):
        if elemento==len(matriz[fila])-1:
            filaStr+=f"{matriz[fila][elemento]}"
        else:
            filaStr+=f"{matriz[fila][elemento]}, "
    return filaStr
def imprimirColumna(columna,matriz):
    columna-=1
    columnaStr=""
    for elemento in range(len(matriz)):
        if elemento==len(matriz)-1:
            columnaStr+=f"{matriz[elemento][columna]}"
        else:
            columnaStr+=f"{matriz[elemento][columna]}, "
    return columnaStr       
def crearMatrizVacia(fila,columnas):
    matriz=[]
    for i in range(fila):
        lista=[]
        for j in range(columnas):
            lista.append(None)
        matriz.append(lista)
    return matriz
def crearMatrizVaciaPro(fila, columnas):
    return [[None]*columnas for _ in range(fila)]
def llenarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=i+j
    return matriz
def rubrica(pentrada):
    """
    Analiza las notas de los estudiantes y clasifica los resultados en aprobados, reprobados, reposición y cuadro de honor.
    También calcula el promedio general de las notas y proporciona un comentario según el promedio.
    Entradas:
    pentrada: lista de valores, donde cada grupo de 5 elementos corresponde a la información de un estudiante:
              nombre, primer apellido, segundo apellido, nota y estado de adecuación curricular.
    Salidas:
    Retorna una tupla con:
    - La cantidad de estudiantes aprobados.
    - El porcentaje de estudiantes aprobados.
    - La cantidad de estudiantes en reposición.
    - El porcentaje de estudiantes en reposición.
    - La cantidad de estudiantes reprobados.
    - El porcentaje de estudiantes reprobados.
    - La cantidad de estudiantes en cuadro de honor.
    - Una lista con los nombres y notas de los estudiantes en cuadro de honor.
    - El promedio general del grupo.
    - Un comentario basado en el promedio del grupo.
    """
    apro = repo = repro = honor = promedio = promedioC = 0
    listaNotasHonor = []
    for i in range(0, len(pentrada), 5):
        if int(pentrada[i + 3]) <= 60:
            repro += 1
        elif 70 > int(pentrada[i + 3]) > 60:
            repo += 1
        elif int(pentrada[i + 3]) > 70:
            apro += 1
        if int(pentrada[i + 3]) >= 90:
            honor += 1
            listaNotasHonor.append(pentrada[i])
            listaNotasHonor.append(pentrada[i + 3])
        promedio += int(pentrada[i + 3])
    promedioC = repro + repo + apro
    if promedio / promedioC >= 70:
        comentario = "Usted tuvo buena promoción estudiantil"
    else:
        comentario = "Analice sus estrategias de enseñanza, mejore sus estrategias de enseñanza para tener una mejor promoción de calidad"
    return (apro, (apro / promedioC) * 100, repo, (repo / promedioC) * 100, repro, (repro / promedioC) * 100, honor, listaNotasHonor, promedio / promedioC, comentario)
def significativa(pentrada):
    """
    Clasifica los estudiantes según si tienen una adecuación curricular significativa o no significativa.
    Entradas:
    pentrada: lista de valores, donde cada grupo de 5 elementos corresponde a la información de un estudiante:
              nombre, primer apellido, segundo apellido, nota y estado de adecuación curricular
    Salidas:
    Retorna una tupla con dos listas:
    - La primera lista contiene los nombres de los estudiantes con "Adecuación curricular Significativa".
    - La segunda lista contiene los nombres de los estudiantes con "Adecuación curricular No Significativa".
    """
    adecuacionS = []  # Lista para almacenar entradas con "Adecuación curricular Significativa"
    adecuacionNS = []  # Lista para almacenar entradas con "Adecuación curricular No Significativa"
    # Itera a través de pentrada con un paso de 5
    for i in range(0, len(pentrada), 5):
        # Verifica la adecuación curricular en la entrada i + 4
        if pentrada[i + 4] == "Adecuación curricular No Significativa":
            adecuacionNS.append(pentrada[i])  # Agrega a la lista adecuacionNS
        elif pentrada[i + 4] == "Adecuación curricular Significativa":
            adecuacionS.append(pentrada[i])  # Agrega a la lista adecuacionS
    # Devuelve ambas listas
    return adecuacionS, adecuacionNS
def funcionNotasFinalesString(pentrada):
    """
    Toma una cadena de texto con la información de los estudiantes, la decodifica en una lista de valores, y luego llama a rubrica y significativa para analizar los datos de los estudiantes.
    Entradas:
    pentrada: una cadena de texto que contiene información sobre los estudiantes, separada por caracteres especiales.
    Salidas:
    Retorna una tupla con tres elementos:
    - Una lista de datos sobre los estudiantes (nombres, apellidos, notas y adecuación curricular).
    - Los resultados de la función rubrica aplicada a la lista de datos sobre los estudiantes.
    - Los resultados de la función significativa aplicada a la lista de datos sobre los estudiantes.
    """
    pentrada += " "
    palabraDeAyuda = ""
    listaDeAyuda = []
    enPalabra = False
    for letra in pentrada:
        if letra.isalpha():
            palabraDeAyuda += letra
            enPalabra = True
        elif letra.isdigit():
            palabraDeAyuda += letra
            enPalabra = True
        else:
            if palabraDeAyuda == "":
                listaDeAyuda.append("No tiene Adecuación")
            else:
                listaDeAyuda.append(palabraDeAyuda)
            palabraDeAyuda = ""
            enPalabra = False
    if enPalabra:
        listaDeAyuda.append(palabraDeAyuda)
    for i in range(0, len(listaDeAyuda), 5):
        if listaDeAyuda[i + 4].upper() == "ANS":
            listaDeAyuda[i + 4] = "Adecuación curricular No Significativa"
        elif listaDeAyuda[i + 4].upper() == "AS":
            listaDeAyuda[i + 4] = "Adecuación curricular Significativa"
    return (listaDeAyuda, rubrica(listaDeAyuda), significativa(listaDeAyuda))
def esPrimoSegundo2(numero, divisor):
    """
    Función para determinar si un número es primo.
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    if divisor * divisor > numero:
        return True
    if numero % divisor == 0:
        return False
    return esPrimoSegundo(numero, divisor + 2)
def esPrimo1(numero):
    """
    Funcion par saber si es primo
    """
    if numero==2:
        return True
    elif numero%2==0:
        return "No es primo"
    else:
        divisor=3
        return esPrimoSegundo2(numero,divisor)
def esPrimo(numero):
    """
    Función para verificar si un número es primo.
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for divisor in range(3, int(numero ** 0.5) + 1, 2):
        if numero % divisor == 0:
            return False
    return True
def esPar(numero):
    if numero%2==0:
        return True
    else:
        return False
def sacarCuatroNumeros(numero):
    if int(numero[:4])==2018:
        return True
    