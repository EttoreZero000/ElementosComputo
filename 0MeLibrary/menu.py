import os
import requests
from PIL import Image
from io import BytesIO

def obtener_estructura(formula, record_type):
    # Consultar la API de PubChem para obtener la estructura
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{formula}/PNG?record_type={record_type}"
    response = requests.get(url)
    if response.status_code == 200:
        # Si la solicitud es exitosa, devolver la imagen
        return Image.open(BytesIO(response.content))
    else:
        return None

def guardar_imagen(imagen, nombre_archivo):
    if imagen is not None:
        imagen.save(nombre_archivo)
        print(f"Imagen guardada como {nombre_archivo}")
    else:
        print("No se pudo guardar la imagen.")

def main():
    formula = "H3O"
    
    # Obtener estructura 2D y guardarla
    imagen_2d = obtener_estructura(formula, "2d")
    nombre_archivo_2d = f"{formula}_2D.png"
    guardar_imagen(imagen_2d, nombre_archivo_2d)
    
    # Obtener estructura 3D y guardarla
    imagen_3d = obtener_estructura(formula, "3d")
    nombre_archivo_3d = f"{formula}_3D.png"
    guardar_imagen(imagen_3d, nombre_archivo_3d)

if __name__ == "__main__":
    main()
