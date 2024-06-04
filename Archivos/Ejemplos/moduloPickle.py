#
#
#
#

#------------------importación d elibrerias
#Ejemplo de uso del Pickle
import pickle

#------------------Definición de variables globales 

#------------------definición de funciones
def graba(nomArchGrabar,lista):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista

#------------------Programa Principal
nomArchivo='Estudiantes'
lista=[[1,"Ana"],[2,"Mario"],[3,"Pedro"],[4,"Marta"]]
graba(nomArchivo,lista)
lista2 = lee(nomArchivo)
print(lista2)
