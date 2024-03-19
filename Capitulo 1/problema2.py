
#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit
#Bibliotecas
#pip install colorama

#programa principal
from colorama import Fore, Style
base=0.0
altura=0.0
#funcion para entrada y verficar su entrada de float
def entradaDeNumero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorNumerico=float(entrada)
            return valorNumerico
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")

base=entradaDeNumero('Digite la base del triangulo: ')
altura=entradaDeNumero('Digite la atura del triangulo: ')

print('La area del triangulo es de: ', (base*altura)/2)