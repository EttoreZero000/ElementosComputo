import random
class Personaje:
    idConter=1
    def __init__(self,nombre,tipo,habilidades):
        self.id=Personaje.generarId()
        self.nombre=nombre
        self.tipo=tipo
        self.habilidades=habilidades
        self.vida=random.randint(1, 1000)
        self.DannoPrinc=0
        self.Estado=True
    def imprimirDatos(self):
        return(self.id,self.nombre,self.tipo,self.habilidades,self.vida,self.DannoPrinc,self.Estado)
    @classmethod
    def generarId(cls):
        id=cls.idConter
        cls.idConter+=1
        return id
    # Métodos para modificar atributos
    def modificarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
    def modificarTipo(self, nuevoTipo):
        self.tipo = nuevoTipo
    def modificarHabilidades(self, nuevasHabilidades):
        self.habilidades = nuevasHabilidades
    def modificarVida(self, nuevaVida):
        self.vida = nuevaVida
    def modificarDannoPrinc(self, nuevoDannoPrinc):
        self.DannoPrinc = nuevoDannoPrinc
    def modificarEstado(self, nuevoEstado):
        self.Estado = nuevoEstado
    # Métodos para imprimir atributos
    def imprimirNombre(self):
        print(f'Nombre: {self.nombre}')
    def imprimirTipo(self):
        print(f'Tipo: {self.tipo}')
    def imprimirHabilidades(self):
        print(f'Habilidades: {self.habilidades}')
    def imprimirVida(self):
        print(f'Vida: {self.vida}')
    def imprimirDannoPrinc(self):
        print(f'Daño Principal: {self.DannoPrinc}')
    def imprimirEstado(self):
        print(f'Estado: {self.Estado}')