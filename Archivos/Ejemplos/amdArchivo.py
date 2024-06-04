#####Este archivo muestra un proceso secuencial y evolutivo manejando Strings,
#####por si mismo no va a correr completamente

# CREAR UN ARCHIVO NUEVO Y AGREGARLE FRASES

referencia = open("frases.txt","w")
referencia.write('La mente es como un paracaídas, de nada sirve, si no está abierta\n')
referencia.write('No dejes para mañana lo que puedes hacer hoy\n')
referencia.write('Todos los días pegaré pequeños brinquitos para llegar a mi meta')
referencia.close()
print("Archivo creado....")

print("------------------------------------------------")
"""
# CREAR UN ARCHIVO NUEVO Y AGREGARLE FRASES
referencia = open("frases.txt","a")
referencia.write('Hoy seré mejor que ayer\n')
referencia.close()
print("Archivo modificado....")

print("------------------------------------------------")

#Manejo de excepciones.
try:
        edad=int(input("Indique la edadde una mujer: "))
        print("La edad es: ",edad-1)
except:
        print("La edad debe ser un numero.")

print("------------------------------------------------")

### LEER UN ARCHIVO
try:   
        referencia = open("frases2.txt","r")
        print("->Imprime línea por línea...")
        linea = referencia.readline()
        print(linea)
        linea = referencia.readline()
        print(linea)
        linea = referencia.readline()
        print(linea)
        referencia.close()
except:
    print("El archivo deseado no existe.")

print("------------------------------------------------")

# READ Lee cantidad de caracteres
referencia = open("frases.txt","r")
print("->Imprime 20 caracteres...")
linea = referencia.read(20)
print(linea)
referencia.close()

print("------------------------------------------------")

#Lee todo el archivo
referencia = open("frases.txt","r")
print("->Imprime todo el archivo...")
lista = referencia.readlines()
print(lista)
referencia.close()

print("------------------------------------------------")

#Otra Manera
referencia = open("frases.txt","r")
print("->Imprime todo el archivo de otra manera...")
for linea in referencia.readlines():
    #for linea in referencia:
    print(linea)
referencia.close()

print("------------------------------------------------")

#Otra manera mas...
referencia=open("frases.txt") #Abre el archivo
linea=referencia.readline() #lee una línea
while linea != "": #lea una línea mientras no esté vacía
    print(linea)
    linea=referencia.readline() #lee una línea
referencia.close() #cierro el archivo para liberar la memoria

print("------------------------------------------------")
#Y otra manera mas...
f=open("frases.txt") #Abre el archivo
for i, linea in enumerate(f):
    #Cuando se itera sobre una secuencia(f se manipula como lista),
    #se puede obtener el índice de posición junto a su valor

    #correspondiente usando la función enumerate().
    #ver ejemplo en: http://docs.python.org.ar/tutorial/pdfs/TutorialPython2.pdf
    print("La línea: ",i,", tiene el texto: ",linea)
f.close() #cierro el archivo para liberar la memoria

print("------------------------------------------------")

manejo_archivo=open("frases.txt") #Abre el archivo
for i, linea in enumerate(manejo_archivo):
   if i>1:  #lee las primeras
      break
   print("La línea: ",i,", tiene el texto: ",linea)
manejo_archivo.close() #cierro el archivo para liberar la memoria

print("------------------------------------------------")

#Originalmente un archivo sólo guarda str
f = open ("variableEnArchivo.py","w")
x=52
#f.write(x)
f.write(str(x))
f.close()

f = open("variableEnArchivo.py","r")
print("->Imprime todo el archivo...")
lista = f.readlines()
print(lista)
f.close()

print("------------------------------------------------")
"""

