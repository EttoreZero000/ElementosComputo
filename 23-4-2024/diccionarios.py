diccionario={}
copyDiccionario={}
anno=2024
def ingresarCedula(diccionario):
    cedula=int(input("Cedula: "))
    nombre=input("Nombre: ")
    Anno=int(input("Anno de nacimiento: "))
    datosPersona=[nombre,Anno]
    diccionario[cedula]=datosPersona
    return "Datos igresado correctamente"
def obtenerAnno(diccionario,anno):
    cedulaABuscar=int(input("Cual cedula quieres buscar su edad: "))
    datosPersona=diccionario[cedulaABuscar]
    return (f"Cedula de la persona: {cedulaABuscar}\nNomre ed la persona: {datosPersona[0]}\nEdad de la persona:{anno-datosPersona[1]}")
def muricion(diccionario,copyDiccionario):
    cedulaAEliminar=int(input("Digite la cedula a eliminar: "))
    copyDiccionario=diccionario[cedulaAEliminar].copy()
    del(diccionario[cedulaAEliminar])
def obtenerEdades(diccionario):
    keys=list(diccionario.key())
    for key in keys:
        
def menu():
    print("1-Ingresar cedula\n2-Obtener informacion\n3-Eliminar persona\n4-Obtener edades de todos")
    opcion=int(input("Opcion: "))
    if opcion==1:
        ingresarCedula(diccionario)
        menu()
    if opcion==2:
        print(obtenerAnno(diccionario,anno))
        menu()
    if opcion==3:
        muricion(diccionario,copyDiccionario)
        menu()
    if opcion==4:
        obtenerEdades(diccionario)
menu()