#Elaborado por Hector Leiva y Mauricio Cortes
#Fehca de creacion 18/5/2024
#Fehca de ultima version 18/5/2024
#Version 3.12.2 64-bit
#Importaciones
from clase import *
from funciones import *
from archivos import *
# Lista para almacenar los personajes
listaPersonajes = []
def registrarPersonajeAux(nombre, tipo, listaHabilidades, danno):
    """
    Registra un nuevo personaje en la lista de personajes.

    Parámetros:
    - nombre (str): Nombre del personaje.
    - tipo (int): Tipo del personaje (1 para Tanque, 2 para Daño, 3 para Cura o Soporte).
    - listaHabilidades (list): Lista de habilidades del personaje.
    - danno (int): Daño principal del personaje.
    Retorna:
    - tuple: Una tupla que contiene un mensaje indicando si el personaje se ha creado correctamente
             y la lista actualizada de personajes.
    """
    if nombre == "":
        return "Nuestro personaje no tiene nombre"
    elif tipo not in [1, 2, 3]:
        return "Nuestro personaje tiene que tener un tipo, 1, 2 o 3"
    elif listaHabilidades == []:
        return "Nuestro personaje no tiene habilidades"
    elif danno <= 0:
        return "El personaje tiene daño inferior o igual a 0"
    else:
        personaje = Personaje(nombre, tipo, listaHabilidades, danno)
        listaPersonajes.append(personaje)
        return "Personaje creado correctamente", listaPersonajes
def registrarPersonaje():
    """
    Registra un nuevo personaje solicitando los datos necesarios al usuario.
    Retorna:
    - list: La lista actualizada de personajes.
    """
    try:
        nombre = input("Nombre de tu personaje: ")
        tipo = input("1-Tanque\n2-Daño\n3-Cura o Soporte\nEl tipo de personaje: ")
        danno = input("Cual es el daño de tu personaje: ")
        listaHabilidades = cicloHabilidades()
        mensaje = registrarPersonajeAux(nombre, int(tipo), listaHabilidades, int(danno))
        print(mensaje)
        return listaPersonajes
    except ValueError:
        print("Hubo un error al indicar datos de tu personaje")
def mostrarPersonaje(listaPersonajes):
    """
    Muestra todos los personajes registrados.
    Parámetros:
    - listaPersonajes (list): Lista de personajes.
    """
    for index, personaje in enumerate(listaPersonajes):
        print(f"Índice: {index}")
        print("Datos del personaje:")
        print(personaje.imprimirDatos())
def dispararPersonaje(listaPersonajes):
    """
    Realiza disparos entre los personajes.
    Parámetros:
    - listaPersonajes (list): Lista de personajes.
    """
    disparar(listaPersonajes)

def mostrarPersonajesMuertos(listaPersonajes):
    """
    Muestra los personajes que han muerto (estado=False) en la lista de personajes.
    Parámetros:
    - listaPersonajes (list): Lista de personajes.
    """
    muertos = [personaje for personaje in listaPersonajes if not personaje.estado]
    if muertos:
        print("Personajes muertos:")
        for index, personaje in enumerate(muertos):
            print(f"Índice: {index}")
            print("Datos del personaje:")
            print(personaje.imprimirDatos())
    else:
        print("No hay personajes muertos.")
def menu():
    """
    Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
    """
    global listaPersonajes  # Indicar que se va a modificar la variable global
    listaPersonajes = lee("Overwatch")
    while True:
        try:
            opcion = int(input("1-Registrar un personaje\n2-Disparar\n3-Mostrar todos los personajes\n4-Mostrar todos los caídos\n5-Salir\nOpción: "))
            if opcion == 1:
                listaPersonajes = registrarPersonaje()
            elif opcion == 2:
                dispararPersonaje(listaPersonajes)
            elif opcion == 3:
                mostrarPersonaje(listaPersonajes)
            elif opcion==4:
                mostrarPersonajesMuertos(listaPersonajes)
            elif opcion == 5:
                graba("Overwatch", listaPersonajes)
                print("Saliendo del programa...")
                break
        except ValueError:
            print("Opción inválida")
        graba("Overwatch", listaPersonajes)
print("Bienvenido a Overwatch")
menu()