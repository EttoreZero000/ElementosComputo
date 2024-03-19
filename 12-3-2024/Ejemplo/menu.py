from funciones import *

def esBisiestoAux(panno):
    if type(panno)!=int:
        return "Debe indicar un valor entero para el año a analizar."
    elif panno<0 or panno>10000:
        return "Debe ser un año después de Cristo y antes del 10.000"
    else:
        if esBisiesto(panno)==True:
            return "El año de estudio es bisiesto."
        else:
            return "El año de estudio NO es bisiesto."

def opcionBisiesto():
    print ("-----------------------------")
    print ("Prueba del año bisiesto")
    print ("-----------------------------")
    try:
        anno = int(input("Ingrese un año positivo: "))
        print(esBisiestoAux(anno))
        print()
        return ""
    except ValueError:
        print("El año deber ser un valor entero.")
        opcionBisiesto()

def calcularAreaTAux(pbase,paltura):
    if type(pbase)!=int:
        return "Debe indicar un valor entero para la base del triángulo"
    elif type(paltura)!=int:
        return "Debe indicar un valor entero para la altura del triángulo"
    elif pbase<0 or paltura<0:
        return "La base y la altura deben ser mayores a cero"
    else:
        return "El área del triángulo rectángulo es: "+str(calcularAreaT(pbase,paltura))

def opcionAreaT():
    print ("-----------------------------")
    print ("Prueba del área del Triángulo")
    print ("-----------------------------")
    try:
        base=int(input("Indique la medida de la base del triángulo rectángulo: "))
        altura=int(input("Indique la medida de la altura del triángulo rectángulo: "))
        print(calcularAreaTAux(base,altura))
        print()
        return ""
    except ValueError:
        print("Debe indicar únicamente valores enteros.")
        opcionAreaT()

def calcularOrdenNumeroAux(pn1,pn2,pn3):
    if type(pn1)!=int or type(pn2)!=int or type(pn3)!=int:
        return "Digite un numero entero"
    else:
        return "El orden de los numeros es:"+str(calcularOrdenNumero(pn1,pn2,pn3))
    
def opcionOrdenarN():
    print("-----------------------------")
    print("Prueba ordenar numeros")
    print("-----------------------------")
    try:
        n1=int(input("Digite el primer numero: "))
        n2=int(input("Digite el segundo numero: "))
        n3=int(input("Digite el tercer numero: "))
        print(calcularOrdenNumeroAux(n1,n2,n3))
        print()
    except ValueError:
        print("Digite un numero enteros")
        opcionOrdenarN()

def opcionMasCercanos():
    print ("-----------------------------")
    print ("Prueba de la recta numérica")
    print ("-----------------------------")
    n1 = int(input("Ingrese n1 : "))
    n2 = int(input("Ingrese n2 : "))
    n3 = int(input("Ingrese n3 : "))
    n4 = int(input("Ingrese n4 : "))
    print(masCercanos(n1, n2, n3, n4))
    print()
    return ""


def opcionPrimo():  
    print ("-----------------------------")
    print ("Prueba del número primo")
    print ("-----------------------------")
    n = int(input("Ingrese n : "))
    print(str(n) + " es primo? " + str(esPrimo(n)))
    print()
    return ""

def opcionPotencia():
    print ("-----------------------------")
    print ("Prueba de la potencia")
    print ("-----------------------------")
    a = int(input("Ingrese base : "))
    b = int(input("Ingrese exponente : "))
    print (str(a) + " elevando a la " +str(b) + " es " + str(potencia(a,b)))
    print()
    return ""

def menu():
    print ("-----------------------------")
    print ("Práctica de Funciones")
    print ("-----------------------------")
    print ("1. Año Bisiesto")
    print ("2. Recta Numérica")
    print ("3. Área del Triángulo Rectángulo")
    print ("4. Ordenar numeros")
    print ("5. Diferencia de Horas")
    print ("6. Número Primo")
    print ("7. Potencia")
    print ("0. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=7:   #ojo
        if opcion == 1:
            opcionBisiesto()
        elif opcion == 2 :
            opcionMasCercanos()
        elif opcion == 3:
            opcionAreaT()
        elif opcion == 4:
            opcionOrdenarN()
        elif opcion == 5:
            print ("en construcción Horas")
        elif opcion == 6:   #ojo
            opcionPrimo()    
        elif opcion == 7:   #ojo 
            opcionPotencia()
        else:
            return
    else:
        print ("Opción inválida, indique una de las siguientes opciones.")
    menu()


#Programa Principal
menu()



