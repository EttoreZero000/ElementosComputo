#Elaborado por Hector Leiva y Mauricio Cortes
#Fehca de creacion 18/5/2024
#Fehca de ultima version 18/5/2024
#Version 3.12.2 64-bit
import random
class Personaje:
    idCounter = 1
    def __init__(self, nombre, tipo, habilidades, danno):
        """
        Inicializa un objeto de la clase Personaje.
        Args:
            nombre (str): El nombre del personaje.
            tipo (str): El tipo del personaje (Tanque, Daño, Cura o Soporte).
            habilidades (list): Una lista de habilidades del personaje.
            danno (int): El daño principal del personaje.
        Attributes:
            id (int): El identificador único del personaje.
            nombre (str): El nombre del personaje.
            tipo (str): El tipo del personaje (Tanque, Daño, Cura o Soporte).
            habilidades (list): Una lista de habilidades del personaje.
            vida (int): La vida actual del personaje (se inicializa aleatoriamente entre 1 y 1000).
            dannoPrinc (int): El daño principal del personaje.
            estado (bool): El estado del personaje (True si está vivo, False si está muerto).
        """
        self.id = Personaje.generarId()
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades
        self.vida = random.randint(1, 1000)
        self.dannoPrinc = danno
        self.estado = True
    def imprimirDatos(self):
        """
        Devuelve una cadena de texto con los datos del personaje.
        Returns:
            str: Una cadena de texto que contiene los datos del personaje.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo}, Habilidades: {self.habilidades}, Vida: {self.vida}, Danno Principal: {self.dannoPrinc}, Estado: {self.estado}"
    @classmethod
    def generarId(cls):
        """
        Genera y devuelve un identificador único para el personaje.
        Returns:
            int: El identificador único del personaje.
        """
        id = cls.idCounter
        cls.idCounter += 1
        return id
    def modificarEstado(self, nuevoEstado):
        """
        Modifica el estado del personaje.
        Args:
            nuevoEstado (bool): El nuevo estado del personaje (True para vivo, False para muerto).
        Returns:
            None
        """
        self.estado = nuevoEstado
    def recibirDisparo(self, cantidad):
        """
        Reduce la vida del personaje cuando recibe un disparo.
        Args:
            cantidad (int): La cantidad de daño que recibe el personaje.
        Returns:
            None
        """
        self.vida -= cantidad
        if self.vida <= 0:
            self.estado = False
    def imprimirId(self):
        return self.id
    def imprimirNombre(self):
        return self.nombre
    def imprimirTipo(self):
        return self.tipo
    def imprimirHabilidades(self):
        return self.habilidades
    def imprimirVida(self):
        return self.vida
    def imprimirDannoPrinc(self):
        return self.dannoPrinc
    def imprimirEstado(self):
        return self.estado