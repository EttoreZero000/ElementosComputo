# Elaborado por: Hector Lieva G.
# Fecha de creacion: 6/3/2024
# Ultima modificacion: 6/3/2024
# Version: 3.12.2 64-bit

# Bibliotecas
# pip install colorama

# Importar módulos necesarios
import math
from colorama import Fore, Style
x1=0.0
x2=0.0
y1=0.0
y2=0.0
# Función para entrada de Float y verificación
def entradaDeFloat(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorFloat = float(entrada)
            return valorFloat
        except ValueError:
            print(f"{Fore.RED}Error: Ingresa un número decimal válido.{Style.RESET_ALL}")

# Entrada de coordenadas como números flotantes
x1 = entradaDeFloat('Digite tu coordenada X en tu primer punto: ')
y1 = entradaDeFloat('Digite tu coordenada Y en tu primer punto: ')
x2 = entradaDeFloat('Digite tu coordenada X en tu segundo punto: ')
y2 = entradaDeFloat('Digite tu coordenada Y en tu segundo punto: ')

# Imprimir el resultado
print('La distancia de tus puntos es:', math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
