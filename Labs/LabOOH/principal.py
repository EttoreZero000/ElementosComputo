#Elaborado por Hector Leiva y Mauricio Cortes
#Fecha creacion 25/5/2025
#Fecha modificacion 25/5/2025
#Version 3.12.2 64-bits Visual Studio Code

#Importaciones
from funciones import *
import archivos
#Funciones
def registrarArmaAux(danno,velocidad,metal,color,inventario):
    if danno not in (7,8,9):
        print("El daño está fuera del rango permitido (debe ser 7, 8 o 9)")
    elif velocidad not in (0.1,0.3):
        print("La velocidad esta fuera del rango permitido (0.1,0.3)")
    elif color not in (1,2,3):
        print("La color esta fuera del rango permitido (1,2,3)")
    elif metal not in (1,2,3):
        print("El metal esta fuera del rango permitido (1,2,3)")
    else:
        return fRegistrarArma(danno,velocidad,metal,color,inventario)
def registrarArmaduraAux(defensa, metal, color, inventario):
    if int(defensa) not in (4, 5, 6):
        print("La defensa está fuera del rango permitido (debe ser 4, 5 o 6)")
    elif int(metal) not in (1, 2, 3):
        print("El metal está fuera del rango permitido (debe ser 1, 2 o 3)")
    elif int(color) not in (1, 2, 3):
        print("El color está fuera del rango permitido (debe ser 1, 2 o 3)")
    else:
        return fRegistrarArmadura(int(defensa), int(metal), int(color), inventario)
def registrarArma(inventario):
    danno = int(input("Daño del arma (7,8,9): "))
    velocidad = float(input("Velocidad del arma (0.1,0.3): "))
    metal = int(input("Metal del arma (1-oro, 2-diamante, 3-hierro): "))
    color = int(input("Color del arma (1-azul, 2-amarillo, 3-gris): "))
    return registrarArmaAux(danno, velocidad, metal, color, inventario)
def registrarArmadura(inventario):
    defensa=input("Defensa de la armadura (4,5,6): ")
    metal=input("Metal del arma (1-oro, 2-diamante, 3-hierro): ")
    color=input("Color del arma (1-zaul, 2-amarillo, 3-gris): ")
    return registrarArmaduraAux(defensa,metal,color,inventario)
def desgastarArma(inventario):
    id = int(input("Dime una ID para utilizar el arma: "))
    inventario = fDesgastarArma(id, inventario)
    return inventario
def eliminarEquipo(inventario):
    id=int(input("Dime una ID para eliminar equipo: "))
    return fEliminarEquipo(id,inventario)
def mostrarArmasPorMetal(inventario):
    metal=int(input("Metal del arma (1-oro, 2-diamante, 3-hierro): "))
    return fMostrarArmasPorMetal(metal,inventario)
def menu():
        while True:
            inventario = archivos.lee("inventario.pkl")
            if inventario is None:
                inventario = []
            opcion = input("1-Registrar un arma\n2-Registrar una armadura\n3-Desgastar un arma\n4-Eliminar equipo\n5-Mostrar todas las herramientas\n6-Mostrar todas las armas por metal\n7-Mostrar herramienta gastada\n8-Salir\n")
            if opcion == '1':
                inventario=registrarArma(inventario)
            elif opcion == '2':
                inventario=registrarArmadura(inventario)
            elif opcion == '3':
                inventario=desgastarArma(inventario)
            elif opcion == '4':
                inventario=eliminarEquipo(inventario)
            elif opcion == '5':
                fMostrarHerramientas(inventario)
            elif opcion == '6':
                mostrarArmasPorMetal(inventario)
            elif opcion == '7':
                fMostrarHerramientasGastadas(inventario)
            elif opcion == '8':
                archivos.graba("inventario.pkl", inventario)
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida, por favor intente de nuevo.")
            archivos.graba("inventario.pkl", inventario)
#Programa principal            
menu()