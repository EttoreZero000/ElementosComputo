import pickle
def graba(nomArchGrabar,lista):
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return
def lee (nomArchLeer):
    dicc={}
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        dicc = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return dicc