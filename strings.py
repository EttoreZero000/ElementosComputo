#Elaborado por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 10-4-2024
#Fecha de ultima modificación 11-4-2024
#Version 3.12.2 64-bits
#Importacion de librerias
from funciones import esBisiesto, calcularAnnosDeNacimiento, determinarEdadMayorMenor
#Funcion para mostrar los palindromos de una lista
def buscarPalindromos(pentrada):
    palindromos = []
    for a in pentrada:
        if a == a[::-1]:
            palindromos.append(a)
    return palindromos
print(buscarPalindromos(["ana", "comida", "somos", "hola", "radar", "oro", "mundo"]))
# Función para solicitar al usuario cuántas edades desea ingresar
def solicitarNumeroEdades():
    numEdades = int(input("\n¿Cuántas edades desea ingresar?: "))
    return numEdades
# Función para ingresar las edades una por una en una lista
def ingresarEdades(numEdades):
    edades = []
    for i in range(1, numEdades + 1):
        edad = int(input(f"Ingrese la edad {i}: "))
        edades.append(edad)
    return edades
# Función para mostrar la información
def mostrarInformacion(edadMayor, edadMenor, annosNacimiento, esBisiestoLista, edades):
    print(f"El menor nació en el año {annosNacimiento[edades.index(edadMenor)]}, por ende tiene {edadMenor} años.")
    print(f"El mayor nació en el año {annosNacimiento[edades.index(edadMayor)]}, por ende tiene {edadMayor} años, esta persona nació en {'año bisiesto' if esBisiestoLista[edades.index(edadMayor)] else 'año no bisiesto'}.")
    print(f"Entre ellos hay {edadMayor - edadMenor} años de diferencia y entre este rango entonces se encuentran las edades:")
    for i, edad in enumerate(sorted(edades), 1):
        print(f"Edad {i}: {edad}")
# Función principal que coordina todo el proceso
def main():
    numEdades = solicitarNumeroEdades()
    edades = ingresarEdades(numEdades)
    edadMayor, edadMenor = determinarEdadMayorMenor(edades)
    annosNacimiento, esBisiestoLista = calcularAnnosDeNacimiento(edades)
    mostrarInformacion(edadMayor, edadMenor, annosNacimiento, esBisiestoLista, edades)
# Llamar a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
