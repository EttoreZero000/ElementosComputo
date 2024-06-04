###########################################################
#Elaborado por: XXX
#Fecha de Realización: XX/XX/XXXX XX:XX
#Ultima actualización: XX/XX/XXXX XX:XX
# Versión: 3.9.1
###########################################################

#El programa define la clase "perro"
class Perro:
    """Definición de Atributos de la clase"""

    """Definición de los métodos de la clase"""
    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase perro
        Método que se llama al instanciar
        """
        self.nombre=""
        self.raza=""
        self.color=""
        self.edad=0
        return
 
    def asignarNombre(self,pnombre):
        """
        F: Asigna el nombre a una mascota
        E: el nombre del perro (string)
        S: Asigna un nombre al atributo nombre del perro
        """   
        self.nombre=pnombre
        return 
    
    def asignarRaza(self,praza):
        """
        F: Asigna la raza de la mascota
        E: Nombre de la raza del perro (string)
        S: Asigna la raza al atributo raza del perro
        """
        self.raza=praza
        return 

    def asignarEdad(self,pedad):
        """
        F: Asigna la Edad de la mascota
        E: La edad del perro (int)
        S: Asigna la edad al atributo edad del perro
        """
        self.edad=pedad
        #¿SErá mejor guardar la edad o la fecha de nacimiento?
        return 
   
    def asignarColor(self,pcolor):
        """
        F: Define el color del pelo del perro
        E: El código del color del perro (int)
        S: Asigna el color del pelo al atributo color del perro
        """ 
        if pcolor==1:
            self.color="Negro"
        elif pcolor==2:
            self.color="Blanco"
        elif pcolor==3:
            self.color= "Gris"
        elif pcolor==4:
            self.color= "Café"
        else:
            self.color= "Combinado"
        return 

    def mostrarNombre(self):
        """
        F:Devuelve sólo el nombre del perro. 
        E:NA
        S:Nombre del perro
        """
        return self.nombre
    def mostrarRaza(self):
        """
        F:Devuelve sólo el nombre del perro. 
        E:NA
        S:Nombre del perro
        """
        return self.raza
    #...
    def indicarDatos(self):
        """
        F:ColordePelo,
        E:el codigo del color del perro (int)
        S:Asigna el color del pelo al atributo color del perro
        """
        return self.nombre,self.raza,self.color,self.edad
        #return "El perro: "+self.nombre+", es de la raza: "+self.raza+",su color de pelaje es:"+self.color+ " y su edad es:"+self.edad

##########################
####Programa Principal####
##########################
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")    
perrito=Perro() #instaciación de la variable, llama al método init

vnombre=input("Ingrese el nombre del perro: ")
perrito.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo: "))
perrito.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito.mostrarNombre())
print("Todos sus datos son: ")
#print(f"el nombre es: {perrito.indicarDatos()[0]}, su raza: {perrito.indicarDatos()[1]}")
print(f"***El nombre es: {perrito.mostrarNombre()}, su raza: {perrito.mostrarRaza()}")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

perrito2=Perro()#instaciación de la variable, llama al método init

vnombre=input("Ingrese el nombre del perro: ")
perrito2.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito2.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito2.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo del perro: "))
perrito2.asignarColor(vcolor)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Se ha registrado correctamente el perro: ", perrito2.mostrarNombre())
print("Todos sus datos son: ")
print(perrito2.indicarDatos())
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
























        
