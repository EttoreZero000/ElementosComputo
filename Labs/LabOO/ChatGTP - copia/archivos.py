import pickle

def graba(nombre_archivo, datos):
    try:
        with open(nombre_archivo + '.pickle', 'wb') as f:
            pickle.dump(datos, f)
        print(f"Se guardaron los datos en '{nombre_archivo}.pickle' con éxito.")
    except Exception as e:
        print("Error al guardar los datos:", e)

def lee(nombre_archivo):
    try:
        with open(nombre_archivo + '.pickle', 'rb') as f:
            datos = pickle.load(f)
        print(f"Se cargaron los datos desde '{nombre_archivo}.pickle' con éxito.")
        return datos
    except Exception as e:
        print("Error al cargar los datos:", e)
        return []
