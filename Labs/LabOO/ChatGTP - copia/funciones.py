from archivos import *
def modificarPersonaje(overwatch, idDisparador, cantidadDisparos, idAfectado):
    for personaje in overwatch:
        if personaje.id == idAfectado:
            vidaActual = personaje.getVida()
            dannoTotal = cantidadDisparos * overwatch[idDisparador - 1].getDannoPrinc()
            vidaNueva = vidaActual - dannoTotal
            if vidaNueva <= 0:
                personaje.setEstado(False)
                personaje.setVida(0)
            else:
                personaje.setVida(vidaNueva)
            print(f"La vida del personaje {personaje.getNombre()} ahora es {vidaNueva}")
    grabaPersonajes(overwatch)

def mostrarTodosPersonajes(overwatch):
    for personaje in overwatch:
        habilidades = ", ".join(personaje.getHabilidades())
        estado = "Activo" if personaje.getEstado() else "Muerto"
        print(f"ID: {personaje.id}, Nombre: {personaje.getNombre()}, Tipo: {personaje.getTipo()}, "
              f"Habilidades: {habilidades}, Vida: {personaje.getVida()}, Estado: {estado}")

def mostrarPersonajesMuertos(overwatch):
    for personaje in overwatch:
        if not personaje.getEstado():
            habilidades = ", ".join(personaje.getHabilidades())
            print(f"ID: {personaje.id}, Nombre: {personaje.getNombre()}, Tipo: {personaje.getTipo()}, "
                  f"Habilidades: {habilidades}, Vida: {personaje.getVida()}, Estado: Muerto")
