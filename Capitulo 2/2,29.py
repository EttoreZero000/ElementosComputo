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

def ordenarDescendente(a, b, c):
    """
    Función para ordenar tres números de forma descendente.

    Parametros:
    a (int): Primer número.
    b (int): Segundo número.
    c (int): Tercer número.

    Returns:
    tuple: Tupla con los números ordenados de forma descendente.
    """
    if a > b:
        if a > c:
            if b > c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    elif b > c:
        if a > c:
            return b, a, c
        else:
            return b, c, a
    else:
        return c, b, a

def main():
    """
    Función principal que utiliza las funciones anteriores para ejecutar el programa.
    """
    print("Sistema de ordenamiento descendente, solo funciona con números enteros!!")

    # Entrada de datos como números enteros
    a = entradaDeEntero('Digite tu primer número: ')
    b = entradaDeEntero('Digite tu segundo número: ')
    c = entradaDeEntero('Digite tu tercer número: ')

    # Ordenar y mostrar el resultado
    print("Orden:", ordenarDescendente(a, b, c))

# Llamada a la función principal
main()
