#Elaborado por Hector Leiva y Mauricio Cortes
#Fehca de creacion 18/5/2024
#Fehca de ultima version 18/5/2024
#Version 3.12.2 64-bit
import random
def cicloHabilidades():
    """
    Solicita al usuario que ingrese las habilidades de un personaje de Overwatch.
    Returns:
        list: Una lista que contiene las habilidades ingresadas por el usuario.
    """
    listaHabilidades=[]
    while True:
        listaAyuda=input("Habilidad de tu personaje: ")
        if listaAyuda=="":
            return listaHabilidades
        else:
            listaHabilidades.append(listaAyuda)
def disparar(lista_personajes):
    """
    Simula un disparo entre dos personajes de Overwatch.
    Args:
        lista_personajes (list): Una lista de objetos de la clase `Personaje`.
    Returns:
        None
    """
    afectado_disparador = []
    if lista_personajes:
        for _ in range(2):
            attempts = 0
            while True:
                personaje = random.choice(lista_personajes)
                if personaje.id not in afectado_disparador:
                    afectado_disparador.append(personaje.id)
                    break
                attempts += 1
                if attempts >= len(lista_personajes):  # Verificar si hemos intentado con todos los personajes
                    break  # Salir del bucle si ya hemos intentado con todos los personajes
    modificar_personaje(afectado_disparador, lista_personajes)
def modificar_personaje(lista_ids, lista_personajes):
    """
    Actualiza el estado de los personajes que han recibido disparos y han perdido toda su vida.
    Args:
        lista_ids (list): Una lista de identificadores de personajes afectados.
        lista_personajes (list): Una lista de objetos de la clase `Personaje`.

    Returns:
        None
    """
    for personaje_id in lista_ids:
        for personaje in lista_personajes:
            if personaje.id == personaje_id:
                cantidad_disparo = random.randint(1, 100)  # Define la cantidad de daño que se inflige al personaje
                personaje.recibirDisparo(cantidad_disparo)  # Corregir el nombre del método
                print(f"Personaje {personaje_id} ha recibido {cantidad_disparo} de daño.")
                if personaje.vida <= 0:
                    print(f"Personaje {personaje_id} ha muerto.")
                    personaje.modificarEstado(False)