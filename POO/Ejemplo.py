class Comida:
    def __init__(self):
        self.codigo = ""
        self.nombre = ""
        self.ingredientes = []
        self.precio = 0.0

    def ingresarCodigo(self, codigo):
        self.codigo = codigo

    def obtenerCodigo(self):
        return self.codigo

    def ingresarNombre(self, nombre):
        self.nombre = nombre

    def obtenerNombre(self):
        return self.nombre

    def ingresarIngredientes(self, ingredientes):
        self.ingredientes = ingredientes

    def obtenerIngredientes(self):
        return self.ingredientes

    def ingresarPrecio(self, precio):
        self.precio = precio

    def obtenerPrecio(self):
        return self.precio

    def imprimir(self):
        ingredientes_str = ', '.join(self.ingredientes)
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nIngredientes: {ingredientes_str}\nPrecio: {self.precio}"

def crearListaDeStrings():
    datos = []
    while True:
        dato = input("Ingrese un ingrediente (o dejar en blanco para terminar): ")
        if dato == '':
            break
        datos.append(dato)
    return datos

# Ejemplo de uso
producto = Comida()

codigo = input("Cual es el codigo de la comida: ")
producto.ingresarCodigo(codigo)

nombre = input("Nombre de la comida: ")
producto.ingresarNombre(nombre)

listaStrings = crearListaDeStrings()
producto.ingresarIngredientes(listaStrings)

precio = float(input("Precio de la comida: "))
producto.ingresarPrecio(precio)

# Imprimir los datos de la comida
print(producto.imprimir())
