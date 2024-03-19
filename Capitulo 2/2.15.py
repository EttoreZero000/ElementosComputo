# Elaborado por: Hector Lieva G.
# Fecha de creacion: 11/3/2024
# Ultima modificacion: 11/3/2024
# Version: 3.12.2 64-bit

def entradaDeEntero(mensaje):
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
            valorEntero = int(entrada)
            return valorEntero
        except ValueError:
            print("Error: Ingresa un número ENTERO válido")

def calcularCostoTotal(tipoEnfermedad, edad, dias):
    """
    Función para calcular el costo total de la hospitalización.

    Parametros:
    tipoEnfermedad (int): Tipo de enfermedad del paciente (1, 2, 3, 4).
    edad (int): Edad del paciente.
    dias (int): Días totales de hospitalización.

    Returns:
    float: Costo total calculado.
    """
    if tipoEnfermedad == 1:
        costoTotal = dias * 25
    elif tipoEnfermedad == 2:
        costoTotal = dias * 16
    elif tipoEnfermedad == 3:
        costoTotal = dias * 20
    elif tipoEnfermedad == 4:
        costoTotal = dias * 32
    else:
        print("Enfermedad no registrada")
        return 0  # Se devuelve 0 en caso de enfermedad no registrada.

    if 14 <= edad <= 22:
        costoTotal *= 1.10  # Incremento del 10% para edades entre 14 y 22.
    print("Costo total:", costoTotal)
    return

def main():
    """
    Función principal que utiliza las funciones anteriores para ejecutar el programa.
    """
    print("Sistema de hospital, costo total!!")

    # Entrada de datos como números enteros
    tipoEnfermedad = entradaDeEntero('Tipo de enfermedad del paciente, 1, 2, 3, 4: ')
    edad = entradaDeEntero('Digite la edad del paciente: ')
    dias = entradaDeEntero('Digite los días totales del paciente: ')

    # Cálculo y presentación del costo total
    calcularCostoTotal(tipoEnfermedad, edad, dias)

# Llamada a la función principal
main()
