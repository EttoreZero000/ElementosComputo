#Elaborado por Héctor Leiva y Mauricio Cortes
#Fecha de creacion 11-4-2024
#Fecha de ultima modificación 11-4-2024
#Version 3.12.2 64-bits
#Importacion de librerias
import funcionesListasLab
#Funcion que solicita el string inicial
def solicitarTexto():
    while True:
        textoCodificado = input("Texto codificado separado por comas:\n")
        if not textoCodificado:
            print("Introduce un texto válido.\n")
            continue
        elif any(letra.islower() for letra in textoCodificado) and any(letra.isupper() for letra in textoCodificado):
            print("El texto ingresado no puede tener mayúsculas y minúsculas.")
            print("Ingrese nuevamente el texto:\n")
            textoCodificado = input("Texto en mayúsculas o minúsculas: ")
            return textoCodificado
        else:
            return textoCodificado.upper() if textoCodificado.isupper() else textoCodificado.lower()
#Funcion que muestra el texto desifrado linea por linea
def mostrarTextoDecodificado(textoDecodificado):
    print(textoDecodificado)
#Funcion que pregunta si continuar el programa o terminarlo
def decisionContinuar():
    while True:
        opcion = input("¿Deseas decodificar más textos? (1: Sí, 2: No): ")
        if opcion == '1':
            return True
        elif opcion == '2':
            return False
        else:
            print("Opción no válida. Por favor, elige 1 para continuar o 2 para salir.")
#Funcion principal que recibe y descifra el texto con código murciélago mediante las demas funciones
def main():
    while True:
        textoCodificado = solicitarTexto()
        textos = textoCodificado.split(',')
        for texto in textos:
            textoDecodificado = funcionesListasLab.decodificarMurcielago(texto.strip())
            mostrarTextoDecodificado(textoDecodificado)
        
        if not decisionContinuar():
            return

if __name__ == "__main__":
    main()
