#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit
#Bibliotecas
#pip install colorama

#programa principal
from colorama import Fore, Style
nombreDino=""
pesoDino=0.0
longitudPies=0.0
#funcion para entrada de Float y verificacion
def entradaDeFloat(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorFloat=float(entrada)
            return valorFloat
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")
#funcion para entrada de String y verificacion
def entradaDeString(mensaje):

    while True:
        entrada = input(mensaje)
        try:
            valorStr=str(entrada)
            return valorStr
        except ValueError:
            print(f"{Fore.RED}Este texto es rojo{Style.RESET_ALL}")

nombreDino=entradaDeString('Cual es el nombre del Dinosaurio?: ')
pesoDino=entradaDeFloat('Cual es el peso del Dinosaurio en toneladas?: ')
longitudPies=entradaDeFloat('Cual es la longitud del Dinosaurio en pies?: ')

print('El nombre de tu Dinosaurio es: '+nombreDino)
print('El peso de tu Dinosaurio en kilogramos es:', pesoDino*1000)
print('La longitud de tu Dinosaurio en metros es:', longitudPies*0.3047)