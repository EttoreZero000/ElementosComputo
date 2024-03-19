#Elaborado por: Hector Lieva G.
#Fecha de creacion: 5/3/2024
#Ultima modificacion: 5/3/2024
#Version: 3.12.2 64-bit

#Programa principal
nombre=input("¿Cual es tu nombre?: ")
apellido=input(nombre+" ¿Cual es tu apellido?: ")
anno=int(input(nombre+" "+apellido+" ¿Cual es tu año de nacimiento?"))
edad=2024-anno
print(nombre+" "+apellido+" tienes", str(edad), "años")
if edad>=18: #Condicional simple
    print(nombre+" "+apellido+" eres mayor de edad.")
elif edad>=12:
    print(nombre+" "+apellido+" eres mayor de edad.")
else:
    print(nombre+" "+apellido+" es un niño")
while edad>=1:
    if edad==1:
        print("Usted tiene:", edad,"año.")
    else: 
        print("Usted tiene:", edad,"años.")
    edad=edad-1