while True:
    angulo1 = float(input("Ingrese el primer ángulo del triángulo: "))
    angulo2 = float(input("Ingrese el segundo ángulo del triángulo: "))
    angulo3 = float(input("Ingrese el tercer ángulo del triángulo: "))
    base = float(input("Ingrese la longitud de la base del triángulo rectángulo: "))
    altura = float(input("Ingrese la altura del triángulo rectángulo: "))
    if(angulo1+angulo2+angulo3>180):
        print('Este triangulo no existe')
    else:
        if (angulo1<90 and angulo2<90 and angulo3<90):
            print("Triangulo chiquito")
        elif (angulo1==90 or angulo2==90 or angulo3==90):
            sumaAngulos=angulo1+angulo2+angulo3
            print("Rectangulo")
            print((base*altura)/2)
        else:
            print("Triangulo grande")