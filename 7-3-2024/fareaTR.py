#Elaborado por: Hector Leiva Ganboa
#Fecha de creacion: 7-3-2024
#Ultima modificacion 7-3-2024
#Version: 3.12.2 64-bit

#defenir variaables
base=0.0
altura=0.0
#definir funciones
def calcularAreaTR(pbase,paltura):
    '''
    Funcionamiento: Calcula la área de una triángulo
    Entrada:
    -pbase(int): tamaño de la base del triangulo rectángulo
    -paltura(int): tamaño de la altura del triangulo rectángulo
    Salida:
    -area(float): área del triángulo rectángulo
    '''
    return pbase*paltura/2
#programa principal
base=int(input("Ingrese el valor de la base: "))
altura=int(input("Ingrese el valor de la base: "))
print("El area de Triangulo rectangulo es:", calcularAreaTR(base,altura))