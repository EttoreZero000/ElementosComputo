#Elaborador por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 14-3-2024
#Ultima modificacion 15-3-2024
#Version: 3.12.2 64-bit

#Librarias importadas
import sys
sys.setrecursionlimit(5000)
#Variables globales del señor del carro
nIngresoMenor = 0
nIngresoMedio = 0
nIngresoMayor = 0
ingresoMenor = 0
ingresoMedio = 0
ingresoMayor = 0
#Variables globales de JUDUCA
cantidadHombres = 0
cantidadMujeres = 0
cantidadMujeresOro = 0
cantidadHombresOro = 0
cantidadEstudiantesCR = 0

def calcularDelCarro(ingreso):
    """
    Función para procesar los datos del señor del carro

    Parámetros:
    ingresp (int): Cantidad de ingresos de activos ingresa al carro
    Returns:
    result (lista): Es una lista de numeros que son:
    nIngresoMenor, nIngresoMedio, nIngresoMayor, ingresoMenor, ingresoMedio, ingresoMayor

    Salida: Una lista ordenada
    """
    global nIngresoMenor, nIngresoMedio, nIngresoMayor, ingresoMenor, ingresoMedio, ingresoMayor

    if ingreso == 0:
        result = [nIngresoMenor, nIngresoMedio, nIngresoMayor, ingresoMenor, ingresoMedio, ingresoMayor]
        # Resetear todas las variables a 0
        nIngresoMenor = 0
        nIngresoMedio = 0
        nIngresoMayor = 0
        ingresoMenor = 0
        ingresoMedio = 0
        ingresoMayor = 0
        return result
    elif ingreso <= 500:
        nIngresoMenor += 1
        ingresoMenor += ingreso
    elif 500 < ingreso < 800:
        nIngresoMedio += 1
        ingresoMedio += ingreso
    elif ingreso >= 800:
        nIngresoMayor += 1
        ingresoMayor += ingreso

def calcularJuduca(ingreso, edad, pais, medallas):
    """
    Función para procesar los datos de la competencia de JUDUCA

    Parámetros:
    ingreso (int): 1.Hombre 2.Mujer
    edad (int): La edad de los participantes
    pais (int): Numero de pais de los participantes
    medallas (int): Numero de medallas de los participantes
    Returns:
    result (lista): Es una lista de numeros que son:
    cantidadHombres, cantidadMujeres, cantidadMujeresOro, cantidadHombresOro, cantidadEstudiantesCR

    Salida: Una lista ordenada
    """
    global cantidadHombres, cantidadMujeres, cantidadMujeresOro, cantidadHombresOro, cantidadEstudiantesCR
    if pais == 4:
        cantidadEstudiantesCR += 1
    if ingreso == 0:
        result = [cantidadHombres, cantidadMujeres, cantidadMujeresOro, cantidadHombresOro, cantidadEstudiantesCR]
        cantidadEstudiantesCR=0
        cantidadHombres=0
        cantidadHombresOro=0
        cantidadMujeres=0
        cantidadMujeresOro=0
        return result
    elif ingreso == 2:
        cantidadMujeres += 1
        if medallas >= 1:
            cantidadMujeresOro += 1
    elif ingreso == 1:
        cantidadHombres += 1
        if medallas >= 2 and edad<25:
            cantidadHombresOro += 1
#b=correo y b=tipo de imprecion
def calcularEscaneoOImprimir(ingreso,cantidad,b,color):
    """
    Función para procesar los datos de la Fotocopiadora

    Parámetros:
    ingreso (int): Tipo de servicio 1.Imprimir 2.Escanear
    cantidad (int): cantida de hojas sacadas o escaneadas
    b (int o string): Dependiendo del servicio se comporta como string o un integer
    color (int): 1.Blanco y negro 2.A color
    Returns:
    1. Cantidad, costo, correo
    2. Tipo de papel, color, cantidad de papel, costo
    Salida: Una lista ordenada
    """
    if ingreso==2:
        return [cantidad,cantidad*20,b]
    if ingreso==1:
        if b==1:
            if color==1:
                return "Papel tradicional","Blanco y negro",cantidad,cantidad*15
            elif color==2:
                return "Papel tradicional","Color",cantidad,cantidad*25
        elif b==2:
            if color==2:
                return "Papel Couché","Color",cantidad,cantidad*250
        elif b==3:
            if color==1:
                return "Papel autoadhesivo","Blanco y negro",cantidad,cantidad*250
            elif color==2:
                return "Paple autoadhesivo","Color",cantidad,cantidad*300