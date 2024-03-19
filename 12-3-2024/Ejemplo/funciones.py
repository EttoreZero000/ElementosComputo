import sys
sys.setrecursionlimit(5000)

def calcularAreaT(pbase,paltura):
    return (pbase*paltura)/2
    
def esBisiesto(a):
    """
    Funcionalidad:
    Determina si un año es bisiesto o no
    Entrada:
    - a(int):Recibe un número entero mayor que cero
    Salida:
    - Devuelve True/False si corresponde a un año bisiesto o no
    """
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def masCercanos(n1, n2, n3, n4):
    """
    Funcionalidad:
    Determina el número más cercano al cero
    Entrada:
    - nX(int): Recibe 4 numeros enteros al usuario y se determina cuales son los mas
    cercanos al cero
    Salida:
    - hilera(string): Devuelve una hilera con lo números más cercanos al cero
    """
    dn1 = abs(n1)
    dn2 = abs(n2)
    dn3 = abs(n3)
    dn4 = abs(n4)
    distanciaMenor = min(dn1,dn2,dn3,dn4)
    hilera = "Numeros mas cercanos al cero: \n"      # \ : alt+92
    if distanciaMenor == dn1:
        hilera += str(n1)
    if distanciaMenor == dn2:
        hilera += " " + str(n2)
    if distanciaMenor == dn3:
        hilera += " " + str(n3)
    if distanciaMenor == dn4:
        hilera += " " + str(n4)
    return hilera

def calcularOrdenNumero(a,b,c):
    if a > b:
        if a > c:
            if b > c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    elif b > c:
        if a > c:
            return b, a, c
        else:
            return b, c, a
    else:
        return c, b, a

def potencia(a,b):
    """
    Funcionalidad:
    Obtiene la potencia de los números indicados
    Entrada:
    - a(int):Número base para obtener la potencia
    - b(int):Número exponente para obtener la potencia
    Salida:
    - valor de la potencia solicitada. 
    """
    if a==0 and b==0:
        return "Error"
    elif a==0:
        return a
    elif b==0:
        return 1
    elif b <0:
        return 1 / potencia(a, -b)
    else:
        return a * potencia (a, b-1)

def esPrimoAux(n, divisor):
    if divisor < n//2:
        if n%divisor ==0:
            return False
        else:
            return esPrimoAux(n, divisor+2)
    else:
        return True

def esPrimo(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        divisor=3
        return esPrimoAux(n, divisor)

def primosEntre(desde, hasta):
    """
    Funcionalidad:
    Obtiene los valores primos entre el rango solicitado por el usuario 
    Entrada:
    -desde(int):valor inicial del rango para obtener los primos
    -hasta(int): valor final del rango para obtener los primos
    Salida:
    - Devolver los números primos contenidos en ese rango
    """
    if desde ==  2:
        return str(desde) + " " + primosEntre(desde+1, hasta)
    elif desde %2==0:
        return primosEntre(desde+1, hasta)
    else:
        if desde <= hasta:
            if esPrimo(desde) == True:
                return str(desde) + " " + primosEntre(desde+2, hasta)
            else:
                return primosEntre(desde+2, hasta)
        else:
            return ""
