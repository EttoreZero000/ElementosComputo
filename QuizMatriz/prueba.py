from funciones import funcionCrearEdificio
def crearEdificio():
    print("-------------\nCrear Edificio\n-------------")
    fila=int(input("Cuantas filas tiene tu edificio: "))
    columnas=int(input("Cuantas filas tiene tu edifico: "))
    print(funcionCrearEdificio(fila,columnas))

def menu():
    print("----\nMenu\n----")
    opcion=int(input("1-Ingresar nuevo edificio"))
    if opcion==1:
        crearEdificio()

menu()