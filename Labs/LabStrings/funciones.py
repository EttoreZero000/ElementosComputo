COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"
def funcionTarjeta(entrada):
    """
    Función que analiza la entrada para determinar la capacidad y velocidad de una tarjeta.
    Parámetros:
        entrada: Cadena de entrada que contiene información sobre la tarjeta.
    Return:
        Una tupla que contiene la capacidad, velocidad mínima de escritura 1, velocidad máxima y velocidad mínima de escritura 2.
    """
    capacidad = velocidadMinimaEscritura1 = velocidadMaxima = velocidadMinimaEscritura2 = 0
    entrada = " " + entrada.lower() + " "
    capacidad = obtenerCapacidad(entrada)
    velocidadMinimaEscritura1 = obtenerVelocidad1(entrada)
    velocidadMaxima = obtenerVelocidadMaxima(entrada)
    velocidadMinimaEscritura2 = obtenerVelocidad2(entrada)
    return (capacidad, velocidadMinimaEscritura1, velocidadMaxima, velocidadMinimaEscritura2)
def obtenerVelocidad2(entrada):
    """
    Función que obtiene la velocidad mínima de escritura 2 de la tarjeta según la entrada.
    Parámetros:
        entrada: Cadena de entrada que contiene información sobre la tarjeta.
    Return:
        Una cadena que indica la velocidad mínima de escritura 2 de la tarjeta.
    """
    if "2" in entrada or "c2" in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}2MB/s{COLOR_RESET}")
    elif "4" in entrada or "c4" in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}4MB/s{COLOR_RESET}")
    elif "6" in entrada or "c6" in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}6MB/s{COLOR_RESET}")
    elif "10" in entrada or "c10" in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}10MB/s{COLOR_RESET}")
    else:
        return "Escribiste mal la clase C, son C2, C4, C6 y C10 o solamente los números"
def obtenerVelocidadMaxima(entrada):
    """
    Función que obtiene la velocidad máxima de la tarjeta según la entrada.
    Parámetros:
        entrada: Cadena de entrada que contiene información sobre la tarjeta.
    Return:
        Una cadena que indica la velocidad máxima de la tarjeta.
    """
    if "i" in entrada:
        return (f"Velocidad máxima de lectura/escritura: {COLOR_RED}104MB/s{COLOR_RESET}")
    elif "ii" in entrada:
        return (f"Velocidad máxima de lectura/escritura: {COLOR_RED}312MB/s{COLOR_RESET}")
    else: 
        return "Escribiste mal la clase UHS, son I e II"
def obtenerVelocidad1(entrada):
    """
    Función que obtiene la velocidad mínima de escritura 1 de la tarjeta según la entrada.
    Parámetros:
        entrada: Cadena de entrada que contiene información sobre la tarjeta.
    Return:
        Una cadena que indica la velocidad mínima de escritura 1 de la tarjeta.
    """
    if "3" in entrada or " u3 " in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}30MB/s{COLOR_RESET}")
    elif "1" in entrada or " u1 " in entrada:
        return (f"Velocidad mínima de escritura es de {COLOR_RED}10MB/s{COLOR_RESET}")
    else:
        return "Escribiste mal la clase UHS"
def obtenerCapacidad(entrada):
    """
    Función que obtiene la capacidad de la tarjeta según la entrada.
    Parámetros:
        entrada: Cadena de entrada que contiene información sobre la tarjeta.
    Return:
        Una cadena que indica la capacidad de la tarjeta.
    """
    if "microsd" in entrada:
        return (f"Una tarjeta: {COLOR_RED}MicroSD{COLOR_RESET} con capacidades de: {COLOR_RED}16MB, 32MB, 64MB, 128MB, 256MB, 512MB,"
        f"1GB, 2GB, 4GB, 8GB, 16GB y 32GB{COLOR_RESET}, {COLOR_RED}no tiene UHS{COLOR_RESET}")
    elif "microsdhc" in entrada:
        return (f"Una tarjeta: {COLOR_RED}MicroSDHC{COLOR_RESET} con capacidades de: {COLOR_RED}4GB, 8GB, 16GB y 32GB, si tiene UHS{COLOR_RESET}")
    elif "microsdxc" in entrada:
        return (f"Una tarjeta: {COLOR_RED}MicroSDXC{COLOR_RESET} con capacidades de: {COLOR_RED}64GB, 128GB, 200GB, 512GB y 2TB(2016), si tiene UHS{COLOR_RESET}")
    else:
        return "Error, escribiste mal el tipo de tarjeta, microSD, microSDHC, microSDXC son las opciones"
def funcionVarilla(entrada):
    """
    Función que obtiene todos los datos finales de otras funciones y los muestra al usuario.
    Parámetros:
        entrada: String introducido por el usuario y revisado.
    Return:
        Salida: Un print para cada dato a mostrar: fabricante, diámetro, proceso de fabricación y grados de acero.
    """
    nomenclaturaLetras = (f"El fabricante es: {entrada[:2]}.")
    diametroVarilla = (f"El diámetro de la varilla es: {obtenerDiametro(entrada)}.")
    procesoVarilla = (f"Proceso de Fabricación: {obtenerProceso(entrada)}.")
    gradoVarilla = (f"Grados de acero: {obtenerGrado(entrada)}.")
    return (nomenclaturaLetras, diametroVarilla, procesoVarilla, gradoVarilla)
def obtenerDiametro(nomenclaturaVarilla):
    """
    Función que obtiene el diámetro de entrada del string.
    Parámetros:
        nomenclaturaVarilla[2]: Valor del string equivalente a las pulgadas del diámetro.
    Return:
        Salidas: Prints indicando las pulgadas según el número introducido.
    """
    if nomenclaturaVarilla[2] == '3':
        return "3/8 pulgadas"
    elif nomenclaturaVarilla[2] == '4':
        return "1/2 pulgadas"
    elif nomenclaturaVarilla[2] == '5':
        return "5/8 pulgadas"
    elif nomenclaturaVarilla[2] == '6':
        return "3/4 pulgadas"
    elif nomenclaturaVarilla[2] == '8':
        return "1 pulgadas"
    else:
        return
def obtenerProceso(nomenclaturaVarilla):
    """
    Función que obtiene el proceso de fabricación del string.
    Parámetros:
        nomenclaturaVarilla[3]: Valor del string equivalente al valor del proceso de fabricación.
    Return:
        Salidas: "Acero al carbono no soldable a temperatura ambiente", "Acero al carbono soldable a temperatura ambiente".
    """
    if nomenclaturaVarilla[3] == 'S':
        return "Acero al carbono no soldable a temperatura ambiente"
    elif nomenclaturaVarilla[3] == 'W':
        return "Acero al carbono soldable a temperatura ambiente"
def obtenerGrado(nomenclaturaVarilla):
    """
    Función que obtiene el grado del acero del string.
    Parámetros:
        nomenclaturaVarilla[4:]: Valor del string equivalente al valor del grado del acero.
    Return:
        Salidas: "2800kgf/cm2", "4200kgf/cm2", "5000kgf/cm2".
    """
    if nomenclaturaVarilla[4:] == '40':
        return "2800kgf/cm2"
    elif nomenclaturaVarilla[4:] == '60':
        return "4200kgf/cm2"
    elif nomenclaturaVarilla[4:] == '70':
        return "5000kgf/cm2"
def funcionLeonisaMenu(codigo):
    """
    Función que muestra un menú de selección al usuario con las diferentes funciones.
    Parámetros:
        codigo: String solicitado al usuario.
    Return:
        Salidas: Prints del menú y opciones del menú.
    """
    while True:
        print("\nMENU:")
        print("1. Código del producto")
        print("2. Color del producto")
        print("3. Talla del producto")
        print("4. Copa del producto")
        print("5. Información completa")
        print("6. Continuar con otro código")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print(f"{COLOR_BLUE}El código del producto es: {codigo[:5]}\n{COLOR_RESET}")
        elif opcion == '2':
            print(f"{COLOR_GREEN}El color del producto es: {obtenerColor(codigo)}\n{COLOR_RESET}")
        elif opcion == '3':
            print(f"{COLOR_YELLOW}La talla del producto es: {obtenerTalla(codigo)}\n{COLOR_RESET}")
        elif opcion == '4':
            print(f"{COLOR_RED}La copa del producto es: {obtenerCopa(codigo)}\n{COLOR_RESET}")
        elif opcion == '5':
            print("Usted desea solicitar:")
            print(f"{COLOR_BLUE}El producto de código: {codigo[:5]}{COLOR_RESET}")
            print(f"{COLOR_GREEN}De color: {obtenerColor(codigo)}{COLOR_RESET}")
            print(f"{COLOR_YELLOW}Talla:{obtenerTalla(codigo)} y{COLOR_RESET}")
            print(f"{COLOR_RED}De copa: {obtenerCopa(codigo)}.{COLOR_RESET}")
        elif opcion == '6':
            continuar = input("¿Desea continuar? (Si/No): ")
            if continuar.lower() == 'no':
                return False
            elif continuar.upper() == 'SI':
                return True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.\n")
                continue
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
def obtenerColor(codigo):
    """
    Función que obtiene el color según los valores del código.
    Parámetros:
        codigo[5:7].upper(): Parte del código equivalente al color.
    Return:
        Prints indicando el color según las letras dadas.
    """
    if codigo[5:7].upper() == 'BL':
        return 'Negro'
    elif codigo[5:7].upper() == 'WH':
        return 'Blanco'
    elif codigo[5:7].upper() == 'BG':
        return 'Beige'
    elif codigo[5:7].upper() == 'RD':
        return 'Rojo'
    elif codigo[5:7].upper() == 'BE':
        return 'Azul'
    else:
        return
def obtenerTalla(codigo):
    """
    Función que obtiene la talla según los valores del código.
    Parámetros:
        codigo: String solicitado al usuario.
    Return:
        codigo[7:9]: Parte del código que indica la talla.
    """
    return codigo[7:9]
def obtenerCopa(codigo):
    # La función obtenerCopa estaba incompleta, por lo que la completé
    """
    Función que obtiene la copa del producto según los valores del código.
    Parámetros:
        codigo: String solicitado al usuario.
    Return:
        codigo[9]: Parte del código que indica la copa.
    """
    return codigo[9]

    """
    Función que obtiene la copa según los valores del código
    Parámetros: codigo: string solicitado al usuario
    Return: codigo[9] parte del codigo que indica la copa
    Salidas:
    """
    #Copa del codigo dado
    return codigo[9]