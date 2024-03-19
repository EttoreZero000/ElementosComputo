#Elaborado por: Mauricio Cortés V.
#Fecha de creación: 13/3/2024 3:30 am
#Última modificación: 14/3/2024 8:30 am
#Versión: 3.10.2from funciones import *



#Programa Principal

def gestionParticipantes(participantesCR=0, hombres=0, mujeres=0, mujeresConOro=0, hombresJovenesConMedallas=0):
    print("1 - Guatemala")
    print("2 - El Salvador")
    print("3 - Panamá")
    print("4 - Costa Rica")
    print("5 - Honduras")
    print("6 - Belice")
    print("7 - República Dominicana")
    print("8 - Nicaragua")
    print("")

    while True:
        try:
            pais = int(input("Ingrese el valor de 'pais' (1-8): "))
            if pais < 1 or pais > 8:
                print("El valor de 'pais' debe estar entre 1 y 8. Por favor, inténtelo nuevamente.")
                continue

            if pais == 4:
                participantesCR += 1

            sexo = int(input("Ingrese el valor de 'sexo' (1: hombre, 2: mujer): "))
            if sexo not in [1, 2]:
                print("El valor de 'sexo' debe ser 1 (hombre) o 2 (mujer). Por favor, inténtelo nuevamente.")
                continue

            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                print("La edad debe ser un número positivo. Por favor, inténtelo nuevamente.")
                continue

            medallas = int(input("Ingrese el número de medallas: "))
            if medallas < 0:
                print("El número de medallas debe ser un número positivo. Por favor, inténtelo nuevamente.")
                continue

            if sexo == 1:
                hombres += 1
                if edad < 25 and medallas > 2:
                    hombresJovenesConMedallas += 1
            else:
                mujeres += 1
                if medallas >= 1:
                    mujeresConOro += 1

            print("\nEstadísticas:")
            print("Número total de participantes de Costa Rica:", participantesCR)
            print("Número total de hombres:", hombres)
            print("Número total de mujeres:", mujeres)
            print("Número de mujeres con al menos una medalla de oro:", mujeresConOro)
            print("Número de hombres menores de 25 años con más de 2 medallas:", hombresJovenesConMedallas)

        except ValueError:
            print("Por favor, ingrese valores numéricos.")
        else:
            break

    # Llamada recursiva con los valores actualizados
    gestionParticipantes(participantesCR, hombres, mujeres, mujeresConOro, hombresJovenesConMedallas)

# Llamada inicial a la función
gestionParticipantes()
