#Elaborado por Hector Leiva y Mauricio Cortes
#Fecha creacion 25/5/2025
#Fecha modificacion 25/5/2025
#Version 3.12.2 64-bits Visual Studio Code
import random
#Clase padre
class Herramienta:
    _id_counter = 1
    def __init__(self,metal,color,inventario):
        self.id = Herramienta.generarId(inventario)
        self.durabilidad=random.randint(1,100)
        self.metales=metal
        self.color=color
        self.estado=True
    @classmethod
    def generarId(cls, inventario):
        if not inventario:
            return cls._id_counter
        else:
            maxId = max(herramienta.getId() for herramienta in inventario)
            return maxId + 1
    def getId(self):
        return self.id
    def getDurabilidad(self):
        return self.durabilidad
    def getMetales(self):
        return self.metales
    def getColor(self):
        return self.color
    def getEstado(self):
        return self.estado
    def setDurabilidad(self, durabilidad):
        self.durabilidad = durabilidad
    def setMetales(self, metales):
        if isinstance(metales, int) and 4>metales >= 0:
            self.metales = metales
        else:
            raise ValueError("Los metales deben ser un entero menor a 4 y no negativo")
    def setColor(self, color):
        if isinstance(color, int) and  0<=color<4:
            self.color = color
        else:
            raise ValueError("El color debe ser un entero menor a 4 y no negativo")
    def setEstado(self, estado):
        if isinstance(estado, bool):
            self.estado = estado
        else:
            raise ValueError("El estado debe ser un valor booleano")
#Clase con la herencia
class Arma(Herramienta):
    def __init__(self,metal,color,danno,velocidad,inventario):
        super().__init__(metal,color,inventario)
        self.danno=danno
        self.velocidadAtaque=velocidad
    def getDanno(self):
        return self.danno
    def getVelocidadAtaque(self):
        return self.velocidadAtaque
    def setDanno(self,danno):
        self.danno=danno
    def setVelocidadAtaque(self,velocidadAtaque):
        self.velocidadAtaque=velocidadAtaque
    def imprimirTodo(self):
        return (self.id, self.metales, self.color, self.durabilidad, self.estado, 0 ,self.danno, self.velocidadAtaque)
class Armadura(Herramienta):
    def __init__(self,metal,color,defensa,inventario):
        super().__init__(metal,color,inventario)
        self.defensa=defensa
    def getDefensa(self):
        return self.defensa
    def setDefensa(self,defensa):
        self.defensa=defensa
    def imprimirTodo(self):
        return (self.id, self.metales, self.color, self.durabilidad, self.estado, self.defensa,0,0)