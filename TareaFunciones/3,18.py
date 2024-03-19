# Elaborado por: Hector Lieva G.
# Fecha de creacion: 11/3/2024
# Ultima modificacion: 11/3/2024
# Version: 3.12.2 64-bit

def entradaDeInt(mensaje):
    """
    Función para ingresar un número entero y verificar la entrada.

    Parametros:
    mensaje (str): Mensaje que se muestra para solicitar la entrada.

    Returns:
    int: Valor entero ingresado correctamente.
    """
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Error: Ingresa un número ENTERO válido")

def contarVotos():
    """
    Función que realiza la lógica de contar los votos de los candidatos.

    Returns:
    tuple: Tupla con la cantidad de votos para cada candidato.
    """
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    candidato4 = 0

    while True:
        voto = entradaDeInt("Ingrese su voto (1, 2, 3, 4). Ingrese 0 para salir: ")

        if voto != 0:
            if 1 <= voto <= 4:
                if voto == 1:
                    candidato1 += 1
                elif voto == 2:
                    candidato2 += 1
                elif voto == 3:
                    candidato3 += 1
                elif voto == 4:
                    candidato4 += 1
            else:
                print("Error: Ingrese un número válido (1, 2, 3, 4).")
        else:
            break

    return candidato1, candidato2, candidato3, candidato4

def calcularPorcentajeVotos(candidato_votos, suma_votos):
    """
    Función para calcular el porcentaje de votos para cada candidato.

    Parametros:
    candidato_votos (tuple): Tupla con la cantidad de votos para cada candidato.
    suma_votos (int): Suma total de votos.

    Returns:
    tuple: Tupla con el porcentaje de votos para cada candidato.
    """
    porcentaje_candidato1 = round((candidato_votos[0] / suma_votos) * 100, 2)
    porcentaje_candidato2 = round((candidato_votos[1] / suma_votos) * 100, 2)
    porcentaje_candidato3 = round((candidato_votos[2] / suma_votos) * 100, 2)
    porcentaje_candidato4 = round((candidato_votos[3] / suma_votos) * 100, 2)

    return porcentaje_candidato1, porcentaje_candidato2, porcentaje_candidato3, porcentaje_candidato4

def main():
    """
    Función principal que utiliza las funciones anteriores para ejecutar el programa.
    """
    print("Sistema de votos solo números enteros!!")

    # Contar los votos, se guarda en una lista del 0 al 3
    candidato_votos = contarVotos()

    # Calcular la suma total de votos
    suma_votos = sum(candidato_votos)

    # Calcular y mostrar el porcentaje de votos para cada candidato
    porcentajes = calcularPorcentajeVotos(candidato_votos, suma_votos)
    print("Votos de candidato 1:", candidato_votos[0], ", porcentaje de:", porcentajes[0])
    print("Votos de candidato 2:", candidato_votos[1], ", porcentaje de:", porcentajes[1])
    print("Votos de candidato 3:", candidato_votos[2], ", porcentaje de:", porcentajes[2])
    print("Votos de candidato 4:", candidato_votos[3], ", porcentaje de:", porcentajes[3])

# Llamada a la función principal
main()
