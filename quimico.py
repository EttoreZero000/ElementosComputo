import requests
import json
def obtener_informacion_compuesto(compuesto):

    # Enviamos una solicitud a la API
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + compuesto
    response = requests.get(url)

    # Convertimos la respuesta a JSON
    data = response.json()

    # Devolvemos la información
    return data
compuesto = input("Ingrese el nombre del compuesto: ")
informacion = obtener_informacion_compuesto(compuesto)
print("Nombre:", informacion["Name"])
print("Fórmula química:", informacion["IUPACName"])
print("Masa molar:", informacion["MolecularWeight"])
print("Solubilidad en agua:", informacion["Solubility"])
print("Temperatura de fusión:", informacion["MeltingPoint"])
print("Temperatura de ebullición:", informacion["BoilingPoint"])
print("Densidad:", informacion["Density"])
