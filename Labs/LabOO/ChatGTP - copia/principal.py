from clase import Personaje
import archivos

overwatch = archivos.cargaPersonajes()

def registrarPersonaje():
    nombre = input("Ingrese el nombre del personaje: ")
    tipo = input("Ingrese el tipo del personaje (tanque, daño, cura): ").capitalize()
    while tipo not in ['Tanque', 'Daño', 'Cura']:
        tipo = input("Tipo inválido. Ingrese el tipo del personaje (tanque, daño, cura): ").capitalize()
    habilidades = []
    numHabilidades = int(input("Ingrese la cantidad de habilidades del personaje: "))
    for i in range(numHabilidades):
        habilidad = input(f"Ingrese habilidad {i+1}: ")
        habilidades.append(habilidad)
    vida = int(input("Ingrese la vida del personaje: "))
    dannoPrinc = int(input("Ingrese el daño principal del personaje: "))
    nuevoPersonaje = Personaje(nombre, tipo, habilidades, vida, dannoPrinc)
    overwatch.append(nuevoPersonaje)
    archivos.grabaPersonajes(overwatch)

def modificarPersonaje(idDisparador, cantidadDisparos, idAfectado):
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
    archivos.grabaPersonajes(overwatch)

def mostrarTodosPersonajes():
    for personaje in overwatch:
        habilidades = ", ".join(personaje.getHabilidades())
        estado = "Activo" if personaje.getEstado() else "Muerto"
        print(f"ID: {personaje.id}, Nombre: {personaje.getNombre()}, Tipo: {personaje.getTipo()}, "
              f"Habilidades: {habilidades}, Vida: {personaje.getVida()}, Estado: {estado}")

def mostrarPersonajesMuertos():
    for personaje in overwatch:
        if not personaje.getEstado():
            habilidades = ", ".join(personaje.getHabilidades())
            print(f"ID: {personaje.id}, Nombre: {personaje.getNombre()}, Tipo: {personaje.getTipo()}, "
                  f"Habilidades: {habilidades}, Vida: {personaje.getVida()}, Estado: Muerto")

def menu():
    print("Bienvenido al juego de Overwatch")
    while True:
        print("\nMenú:")
        print("1. Registrar un personaje")
        print("2. Modificar personaje")
        print("3. Mostrar todos los personajes")
        print("4. Mostrar todos los personajes muertos")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrarPersonaje()
        elif opcion == 2:
            idDisparador = int(input("Ingrese el ID del personaje que disparó: "))
            cantidadDisparos = int(input("Ingrese la cantidad de disparos: "))
            idAfectado = int(input("Ingrese el ID del personaje afectado: "))
            modificarPersonaje(idDisparador, cantidadDisparos, idAfectado)
        elif opcion == 3:
            mostrarTodosPersonajes()
        elif opcion == 4:
            mostrarPersonajesMuertos()
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
