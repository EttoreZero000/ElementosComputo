def crearEdificio(fila, columnas):
    matriz=[]
    for i in range(fila):
        fila=[]
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz