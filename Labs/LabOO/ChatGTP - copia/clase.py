class Personaje:
    id_counter = 0

    def __init__(self, nombre, tipo, habilidades, vida, dannoPrinc):
        Personaje.id_counter += 1
        self.id = Personaje.id_counter
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades
        self.vida = vida
        self.dannoPrinc = dannoPrinc
        self.estado = True

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTipo(self, tipo):
        self.tipo = tipo

    def setHabilidades(self, habilidades):
        self.habilidades = habilidades

    def setVida(self, vida):
        self.vida = vida

    def setDannoPrinc(self, dannoPrinc):
        self.dannoPrinc = dannoPrinc

    def setEstado(self, estado):
        self.estado = estado

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getHabilidades(self):
        return self.habilidades

    def getVida(self):
        return self.vida

    def getDannoPrinc(self):
        return self.dannoPrinc

    def getEstado(self):
        return self.estado
