#Elaborado por Hector Leiva y Mauricio Cortes
#Fehca de creacion 18/5/2024
#Fehca de ultima version 18/5/2024
#Version 3.12.2 64-bit
import pickle
def graba(nombre_archivo, lista_personajes):
    """
    Guarda una lista de personajes en un archivo binario.
    Args:
        nombre_archivo (str): El nombre del archivo en el que se guardarán los datos.
        lista_personajes (list): La lista de personajes que se desea guardar.
    Returns:
        None
    """
    try:
        with open(nombre_archivo + ".dat", "wb") as archivo:
            pickle.dump(lista_personajes, archivo)
        print("Guardado correctamente")
    except Exception as e:
        print("Error al guardar el archivo:", e)
def lee(nomArchLeer):
    """
    Lee una lista de personajes desde un archivo binario.
    Args:
        nomArchLeer (str): El nombre del archivo del que se leerán los datos.
    Returns:
        list: La lista de personajes leída desde el archivo, o una lista vacía si hay un error.
    """
    try:
        with open(nomArchLeer + ".dat", "rb") as archivo:
            datos = pickle.load(archivo)
        print("Carga finalizada")
        return datos
    except FileNotFoundError:
        print("El archivo", nomArchLeer, "no existe. Creando una nueva lista de personajes.")
        return []
    except Exception as e:
        print("Error al leer el archivo:", e)
        return []