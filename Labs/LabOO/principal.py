from clase import *
from funciones import *
diccionario={}
def registrarPersonajeAux(nombre,tipo,listaHabilidades):
    if nombre=="":
        return "Nuestro personaje no tiene nombre"
    elif tipo not in [1,2,3]:
        return "Nuestro personaje tiene que tener un tipo, 1, 2 o 3"
    elif listaHabilidades==[]:
        return "Nuestro personaje no tiene habilidades"
    else:
        personaje = Personaje(nombre, tipo, listaHabilidades)
        diccionario[personaje.id] = personaje
        return "Personaje creado correctamente"
def registrarPersonaje():
    nombre=input("Nombre de tu personaje: ")
    tipo=int(input("1-Tanque\n2-Daño\n3-Cura o Soporte\nEl tipo de personaje: "))
    listaHabilidades=cicloHabilidades()
    registrarPersonajeAux(nombre,tipo,listaHabilidades)
def mostrarPersonaje():
    for personaje_id, personaje in diccionario.items():
        print(f"ID: {personaje_id}")
        print("Datos del personaje:")
        print(personaje.imprimirDatos())
def dispararPersonaje():
    disparar(diccionario)
def menu():
    opcion=int(input("1-Registrar un personaje\n2-Disparar\n3-Mostrar todos los personajes\n4-Mostrar todos los caidos\n5-Salir\nOpcion: "))
    if opcion==1:
        print(registrarPersonaje())
    elif opcion==2:
        print(dispararPersonaje())
    elif opcion==3:
        mostrarPersonaje()
    elif opcion==5:
        return None  
    menu()
menu()
len(diccionario)