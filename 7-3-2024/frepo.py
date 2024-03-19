#Elaborado por: Hector Leiva Ganboa
#Fecha de creacion: 7-3-2024
#Ultima modificacion 7-3-2024
#Version: 3.12.2 64-bit

#Librerias utilizadas
from colorama import Fore, Style
#defenir variables
nota=0
#definir funciones
def obtenerEstado(pnota):
    '''
    Funcionamiento: calcula si el estudiante se quedo si o no
    Entrada:
    -pnota(int): la nota del estudiante
    Salida:
    -resultado(String): imprime si se quedo, si tiene que hacer repo o pasa de año
    '''
    if (pnota>=70):
        print(f'{Fore.GREEN}Aprobo de año{Style.RESET_ALL}')
    elif (70>pnota>=60):
        print(f'{Fore.YELLOW}Tienes que ir a repo{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Te quedastes el año{Style.RESET_ALL}')
    return 
#programa principal
while True:
    nota=int(input("Ingrese el valor de la nota: "))
    obtenerEstado(nota)