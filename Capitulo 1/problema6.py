#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit

#Bibliotecas
#pip install colorama

#programa principal
from colorama import Fore, Style
dias=0
#funcion para entrada de Int y verificacion
def entradaDeInt(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorInt=int(entrada)
            return valorInt
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")

dias=entradaDeInt('Cantidad de dias que quieres saber sus sengudos: ')
print('A pasado:',dias*24*60*60,'segundos')