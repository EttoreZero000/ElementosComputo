#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit

#Bibliotecas
#pip install colorama

#programa principal
import math
from colorama import Fore, Style
radio=0.0
altura=0.0
#funcion para entrada de Float y verificacion
def entradaDeFloat(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorFloat=float(entrada)
            return valorFloat
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")

altura=entradaDeFloat('Cual es la altura de tu cilindro?: ')
radio=entradaDeFloat('Cual es el radio de tu cilindro: ')

print('El area de tu cilindro es de:', math.pi*radio**2*altura)