#Elaborado por Héctor Leiva, Mauricio Cortes
#Fecha de creacion: 11-4-2024
#Fecha de modificacion: 13-4-2024 10pm
#Vercion: 3.12.2 64-bits Visual Studio Code
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
def notasFinalesString(pentrada):
    """
    Llama a funcionNotasFinalesString con una cadena de texto específica y luego imprime los resultados de las funciones rubrica y significativa, junto con los datos sobre los estudiantes.
    Entradas:
    No toma entradas directas; llama a funcionNotasFinalesString con una cadena de texto específica.
    Salidas:
    Imprime información sobre los estudiantes y los resultados de las funciones rubrica y significativa.
    """
    listaNotas = funcionNotasFinalesString(pentrada)
    for i in range(0, len(listaNotas[0]), 5):
        print(f"Nombre: {listaNotas[0][i]}")
        print(f"Primer apellido: {listaNotas[0][i + 1]}")
        print(f"Segundo apellido: {listaNotas[0][i + 2]}")
        print(f"Nota: {listaNotas[0][i + 3]}")
        print(f"Estado: {listaNotas[0][i + 4]}\n")
    print(f"Cantidad y porcentaje de aprobado: {listaNotas[1][0]} {listaNotas[1][1]}%")
    print(f"Cantidad y porcentaje de reposición: {listaNotas[1][2]} {listaNotas[1][3]}%")
    print(f"Cantidad y porcentaje de reprobados: {listaNotas[1][4]} {listaNotas[1][5]}%")
    print(f"Lista de alumnos de cuadro de honor (superiores e iguales a 90) y su nota: {listaNotas[1][7]}")
    print(f"Lista de alumnos de Adecuación curricular Significativa (AS): {listaNotas[2][0]}")
    print(f"Lista de alumnos de Adecuación curricular No Significativa (ANS): {listaNotas[2][1]}")
    print(f"Promedio del grupo: {listaNotas[1][8]}")
    print(listaNotas[1][9])
def decodificarMurcielago(cadena):
    """
    Decodifica una cadena de texto basada en un código específico, donde los números del 0 al 9 se corresponden con las letras de la palabra "murciélago".
    Entradas:
    cadena: una cadena de texto que contiene los números a decodificar.
    Salidas:
    Retorna la cadena de texto decodificada, con las letras convertidas de acuerdo al código y en mayúsculas si la cadena original contiene letras mayúsculas.
    """
    textoDecodificado = ''
    for caracter in cadena:
        if caracter == '0':
            textoDecodificado += 'm'
        elif caracter == '1':
            textoDecodificado += 'u'
        elif caracter == '2':
            textoDecodificado += 'r'
        elif caracter == '3':
            textoDecodificado += 'c'
        elif caracter == '4':
            textoDecodificado += 'i'
        elif caracter == '5':
            textoDecodificado += 'e'
        elif caracter == '6':
            textoDecodificado += 'l'
        elif caracter == '7':
            textoDecodificado += 'a'
        elif caracter == '8':
            textoDecodificado += 'g'
        elif caracter == '9':
            textoDecodificado += 'o'
        else:
            textoDecodificado += caracter

    if any(letra.isupper() for letra in cadena):
        return textoDecodificado.upper()
    else:
        return textoDecodificado.lower()

notasFinalesString("Ana$Fuentes°Castro^95¬AS;Mario°Araya[Rodríguez^60¬ANS;Sergio°Poveda°Martínez^65¬;Amanda°Delgado°Trejos^40¬;Leticia°Pacheco°Fuentes^50¬AS")
print(decodificarMurcielago("67S, P767B27S, 07G437S, S9N, T1, Y, Y9, S909S, D5, 67, 04S07, S7NG25"))
