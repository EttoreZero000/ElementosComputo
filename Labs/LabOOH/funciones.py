#Elaborado por Hector Leiva y Mauricio Cortes
#Fecha creacion 25/5/2025
#Fecha modificacion 25/5/2025
#Version 3.12.2 64-bits Visual Studio Code
from clases import Arma, Armadura
def numeroAMetal(p):
    if p==1:
        return "oro"
    elif p==2:
        return "diamante"
    elif p==3:
        return "hierro"
def numeroAColor(p):
    if p==1:
        return "azul"
    elif p==2:
        return "amarillo"
    elif p==3:
        return "gris"
def fRegistrarArma(danno, velocidad, metal, color, inventario):
    arma = Arma(metal, color, danno, velocidad,inventario)
    inventario.append(arma)
    print(f"Arma registrada con ID {arma.getId()}")
    return inventario
def fRegistrarArmadura(defensa,metal,color,inventario):
    armadura = Armadura(metal,color,defensa,inventario)
    inventario.append(armadura)
    print(f"Armadura registrada con ID {armadura.getId()}")
    return inventario
def fDesgastarArma(id, inventario):
    for herramienta in inventario:
        if isinstance(herramienta, Arma) and herramienta.getId() == id:
            herramienta.setDurabilidad(herramienta.getDurabilidad() - 25)
            if herramienta.getDurabilidad() <= 0:
                herramienta.setEstado(False)
                print(f"El arma con ID {id} se ha gastado del inventario por desgaste.")
            else:
                print(f"El arma con ID {id} ahora tiene una durabilidad de {herramienta.getDurabilidad()}")
            return inventario  # Devuelve el inventario actualizado después de modificarlo
    print(f"No se encontró un arma con ID {id}")
    return inventario  # Si no se encuentra el arma, devuelve el inventario sin cambios
def fEliminarEquipo(id, inventario):
    for herramienta in inventario:
        if herramienta.getId() == id:
            inventario.remove(herramienta)  # Eliminar el elemento específico de la lista
            print(f"Equipo con ID {id} eliminado.")
            break  # Salir del bucle una vez que se ha encontrado y eliminado el equipo
    else:
        print(f"No se encontró un equipo con la ID {id}.")
    return inventario
def fMostrarHerramientas(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        for herramienta in inventario:
            parametros=herramienta.imprimirTodo()
            metal=numeroAMetal(parametros[1])
            color=numeroAColor(parametros[2])
            print (f"Id: {parametros[0]}, Metal: {metal}, Color: {color}, Durabilidad: {parametros[3]}, Estado: {parametros[4]}, Defensa: {parametros[5]}, Daño: {parametros[6]}, Velocidad: {parametros[7]}")
def fMostrarArmasPorMetal(metal,inventario):
    if 0 < metal < 4:
        armasFiltradas = [arma for arma in inventario if isinstance(arma, Arma) and arma.getMetales() == metal]
        if not armasFiltradas:
            print(f"No se encontraron armas con metal {metal}")
        else:
            for arma in armasFiltradas:
                parametros=arma.imprimirTodo()
                metal=numeroAMetal(parametros[1])
                color=numeroAColor(parametros[2])
                print (f"Id: {parametros[0]}, Metal: {metal}, Color: {color}, Durabilidad: {parametros[3]}, Estado: {parametros[4]}, Defensa: {parametros[5]}, Daño: {parametros[6]},  Velocidad: {parametros[7]}")
    else:
        print("Metal inválido. Debe ser un entero entre 0 y 3.")
def fMostrarHerramientasGastadas(inventario):
    herramientasGastadas = [herramienta for herramienta in inventario if herramienta.getDurabilidad() <= 0]
    if not herramientasGastadas:
        print("No hay herramientas gastadas.")
    else:
        for herramienta in herramientasGastadas:
            tipo = "Arma" if isinstance(herramienta, Arma) else "Armadura"
            parametros=herramienta.imprimirTodo()
            metal1=numeroAMetal(parametros[1])
            color=numeroAColor(parametros[2])
            print(f"Tipo: {tipo}, Id: {parametros[0]}, Metal: {metal1}, Color: {color}, Durabilidad: {parametros[3]}, Estado: {parametros[4]}, Defensa: {parametros[5]}, Daño: {parametros[6]},  Velocidad: {parametros[7]}")