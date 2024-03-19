#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit
#Bibliotecas
#pip install colorama

#programa principal
from colorama import Fore, Style
Galon=0.0
#funcion para entrada de Float y verificacion
def entradaDeFloat(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorFloat=float(entrada)
            return valorFloat
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")

Galon=entradaDeFloat('Cuantos galones quiere?: ')

print('Total a pagar: $', Galon*3.785*8.20)