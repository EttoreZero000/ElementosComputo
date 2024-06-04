import random
def cicloHabilidades():
    listaHabilidades=[]
    while True:
        listaAyuda=input("Habilidad de tu personaje: ")
        if listaAyuda=="":
            return listaHabilidades
        else:
            listaHabilidades.append(listaAyuda)
def disparar(diccionario):
    afectadoDisparador = []
    if diccionario:
        for _ in range(2):
            while True:
                personajeId = random.choice(list(diccionario.keys()))
                if personajeId not in afectadoDisparador:
                    afectadoDisparador.append(personajeId)
                    break