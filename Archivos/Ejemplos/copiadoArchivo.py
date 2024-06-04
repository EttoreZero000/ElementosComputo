def copiaArch(antArch,nuevoArch):
    f1 = open (antArch,"r")
    f2 = open (nuevoArch,"w")
    texto = f1.read(50)
    while texto!="":
        f2.write(texto)
        texto=f1.read(50)
    f1.close()
    f2.close()
    print("copia del archivo creada como:", nuevoArch, ", en la misma carpeta")
    return

#Programa Principal
antArch = "frases.txt"
nuevoArch = "nuevo.dat"
copiaArch(antArch,nuevoArch)

