while True:
    Peso = float(input("Cual es tu peso: "))
    Estaltura = float(input("Cual es tu estatura: "))

    Peso=Peso/(Estaltura*Estaltura)
    print(Peso) 


    if (Peso<18.5):
        print("Bajo peso")
    elif (Peso<24.9):
        print("Normal")
    elif (Peso<29.9):
        print("Sobrepeso")
    elif (Peso<34.9):
        print("Obesidad I")
    elif (Peso<39.9):
        print("Obesidad II")
    elif (Peso<49.9):
        print("Obesidad III")
    elif (Peso>50):
        print("Obesidad IV")