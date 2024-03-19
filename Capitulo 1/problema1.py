#Elaborado por: Hector Lieva G.
#Fecha de creacion: 6/3/2024
#Ultima modificacion: 6/3/2024
#Version: 3.12.2 64-bit

#Programa principal
prepro = 0.0
pago = 0.0
#funcion para entrada y verficar su entrada de float
def obtener_valor_numerico(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valorNumerico = float(entrada)
            return valorNumerico
        except ValueError:
            print("Error: Ingresa un número decimal válido.")

prepro = obtener_valor_numerico('Cantidad de dinero de todos los productos?: ')
pago = obtener_valor_numerico('Cantidad de dinero que entrega el cliente?: ')

cambio = pago - prepro
print("Cambio:", cambio)