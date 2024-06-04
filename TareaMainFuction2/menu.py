#Elaborador por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 2-4-2024
#Ultima modificacion 3-4-2024
#Version: 3.12.2 64-bit

#Librerias importadas
from funciones import *
#Funciones de verificacion
def verificacionNumeroSuerte(pentrada):
    
    if type(pentrada)!=str:
        return "Escriba una frase valida"
    elif len(pentrada)<=0:
        return "Escriba una frase mayor a 0 caracteres"
    else:
        return (f"Tu numero de la suerte es: {funcionNumeroSuerte(pentrada)}")

def verificacionLetraVocales(pentrada):
    if len(pentrada) <= 0:
        return "Escriba una frase mayor a 0 caracteres"
    else:
        # Llama a la función y almacena su salida en una variable
        funcionVocales_resultado = funcionVocales(pentrada)
        # Accede a los elementos de la variable resultante
        return (f"Cantidad de a: {funcionVocales_resultado[0]}\nCantidad de e: {funcionVocales_resultado[1]}\n"
                f"Cantidad de i: {funcionVocales_resultado[2]}\nCantidad de o: {funcionVocales_resultado[3]}\n"
                f"Cantidad de u: {funcionVocales_resultado[4]}\nCantidad de consonantes {funcionVocales_resultado[5]}")

def verificacionPalindroma(pentrada):
    if len(pentrada)<=2:
        return "Escibra una palabra que tenga 3 letras"
    else:
        return funcionPalindroma(pentrada.lower())
    
def verificacionEliminarVocales(pentrada):
    if len(pentrada)<0:
        return "Escriba una palabra o frase"
    else:
        return funcionEliminarVocales(pentrada)
def verificacionEspejo(pentrada):
    if len(pentrada)<0:
        return "Escriba una frase"
    else:
        return funcionPalabraEspejo(pentrada)
def verificacionPalabras(pentrada):
    if len(pentrada)<0:
        return "Escriba una frase!!"
    else:
        return funcionPalabras(pentrada)

#Funciones de entrada y salida
def determinarSuerte():
    print("----------------")
    print("Numero de Suerte")
    print("----------------")
    entrada=input("Escriba una frase: ")
    print(verificacionNumeroSuerte(entrada))

def determinarCantidadDeVocalesYConsonantes():
    print("-----------------------------------------------")
    print("Determinar la cantidad de Vocales y consonantes")
    print("-----------------------------------------------")
    entrada=input("Digite una frase para verla: ")
    print(verificacionLetraVocales(entrada))

def determinarPalidroma():
    print("------------------------------------")
    print("Determinar si una palabra palindroma")
    print("------------------------------------")
    entrada=input("Escriba una palabra que creas que sea palindroma: ")
    print(verificacionPalindroma(entrada))
def determinarVocales():
    print("---------------------------------------")
    print("Determinar el reconocimiento de vocales")
    print("---------------------------------------")
    entrada=input("Escriba una palabra para eliminar las vocales: ")
    print(verificacionEliminarVocales(entrada))
def determinarEspejo():
    print("---------------")
    print("Frase en espejo")
    print("---------------")
    entrada=input("Esccriba una frase: ")
    print(verificacionEspejo(entrada))
def determinarPalabras():
    print("--------------------------------")
    print("Cuantas palabras hay en un texto")
    print("--------------------------------")
    entrada=input("Escribra una frase: ")
    print(verificacionPalabras(entrada))
#FuncionMain
def main():
    try:
        print("----")
        print("Menu")
        print("----")
        print("1-Numero de Suerte \n2-Cantidad de vocales y consonantes\n3-La palabra es palíndroma\n"
              "4-Reconociendo las vocales\n5-Candena espejo\n6-Analizandor de texto")
        opcion=int(input("Escoja un opción: "))
        if opcion==1:
            determinarSuerte()
        elif opcion==2:
            determinarCantidadDeVocalesYConsonantes()
        elif opcion==3:
            determinarPalidroma()
        elif opcion==4:
            determinarVocales()
        elif opcion==5:
            determinarEspejo()
        elif opcion==6:
            determinarPalabras()
        else:
            print("Escoja una opción válida")
    except ValueError:
        print("Dijite un valor correcto")
        main()
main()