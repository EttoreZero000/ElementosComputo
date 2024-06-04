#Funcion que decodifica según el código murciélago
def decodificarMurcielago(cadena):
    textoDecodificado = ''
    for caracter in cadena:
        if caracter == '0':
            textoDecodificado += 'm'
        elif caracter == '1':
            textoDecodificado += 'u'
        elif caracter == '2':
            textoDecodificado += 'r'
        elif caracter == '3':
            textoDecodificado += 'c'
        elif caracter == '4':
            textoDecodificado += 'i'
        elif caracter == '5':
            textoDecodificado += 'e'
        elif caracter == '6':
            textoDecodificado += 'l'
        elif caracter == '7':
            textoDecodificado += 'a'
        elif caracter == '8':
            textoDecodificado += 'g'
        elif caracter == '9':
            textoDecodificado += 'o'
        else:
            textoDecodificado += caracter
    
    if any(letra.isupper() for letra in cadena):
        return textoDecodificado.upper()
    else:
        return textoDecodificado.lower()
