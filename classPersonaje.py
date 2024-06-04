###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Ultima actualización: XX/XX/XXXX XX:XX
###########################################################

#Importación de librerías
import pickle

#Definición de variables globales
Overwatch=[]

#Definción de clases
class Personaje:
    
    def __init__(self):
        self.ID=pID
        self.nombre=pNombre
        self.tipo=pTipo
        self.habilidades=pHabilidades
        self.vida=pVida
        self.dannoPrinc=pDannoPrinc
        self.estado=pEstado
    def asignarID(self,pID):
        self.ID=pID
        return
    def asignarNombre(self,pNombre):
        self.nombre=pNombre
        return
    def asignarTipo(self,pTipo):
        self.tipo=pTipo
        return
    def asignarHabilidades(self,pHabilidades):
        self.habilidades=pHabilidades
        return
    def asignarVida(self,pVida):
        self.vida=pVida
        return
    def asignarDannoPrinc(self,pDannoPrinc):
        self.dannoPrinc=pDannoPrinc
        return
    def asignarEstado(self,pEstado):
        self.Estado=pEstado
        return
    def indicarDatos(self):
        return self.ID+ self.nombre+self.tipo+self.habilidades+self.vida+self.dannoPrinc+self.estado
