#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit

#Bibliotecas
#pip install colorama

#programa principal
import math
from colorama import Fore, Style
lado1=0.0
lado2=0.0
lado3=0.0
#funcion para entrada de Float y verificacion
def entradaDeFloat(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorFloat=float(entrada)
            return valorFloat
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")
lado1=entradaDeFloat('Digite el primer lado de tu triangulo: ')
lado2=entradaDeFloat('Digite el segundo lado de tu triangulo: ')
lado3=entradaDeFloat('Digite el tercero lado de tu triangulo: ')
S=(lado1+lado2+lado3)/2
print('El area del triangulo es:',math.sqrt(S*(S-lado1)*(S-lado2)*(S-lado3)))