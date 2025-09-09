'''
Crear una funcion llamada menu()
Parametros de entrada: Ninguno
Lo que realiza: muestra un meno y pide al usuario que seleccione una opcion.
Valor de retorno: la opcion seleccionada
'''
print("Bienvenido a Delicias la costa")

def menu():
    print("1. Entradas\n2. Platos fuertes\n3. Bebidad\n4. Postres\n5. Salida")
    opcion = int(input("Elija una opcion: "))
    return opcion
def entradas():
    print("1. Pan de bono\t\t$30000")
    print("2. Empanada\t\t$35000")
    print("3. nachos\t\t$40000")
    
def Fuertes():
    print("1. Mojarra Cartagenera\t\t$700000")
    print("2. Salmón\t\t$600000")
    print("3. Bandeja paisa\t\t$500000")

def bebidas():
    print("1. coca cola\t\t$20000")
    print("2. Limonada\t\t$15000")
    print("3. Cerveza costeña\t\t$50000")

def postres():
    print("1. Postre de limon\t\t$39900")
    print("2. Postre tres leches\t\t$29900")
    print("3. Banana split\t\t$50000")


# Funcion principal
eleccion = menu()
print(eleccion)

def main():
    match(eleccion):
        case 1:
            entradas()
        case 2:
            Fuertes()
        case 3:
            bebidas()
        case 4:
            postres()
        case _:
            print("opcion no valida")

# Aqui se llama a la funcion principal
if __name__ == "__main__":
    main()