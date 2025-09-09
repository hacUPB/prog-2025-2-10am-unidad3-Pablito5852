#  Calculadora
while True:
    Numero1 = int(input("ingrese el primer numero"))
    Numero2 = int(input("ingrese el segundo numero"))
    print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion = input("elija una opcion: ")
    opcion = opcion.upper() # se convierte el texto a mayuscula
    match opcion:
        case 'S':
            print("Suma")
            resultado = Numero1 + Numero2
        case 'R':
            print("Resta")
            resultado = Numero1 - Numero2
        case 'M':
            print("Muntiplicacion")
            resultado = Numero1 * Numero2
        case 'D':
            print("Division")
            resultado = Numero1 / Numero2
        case 'E':
            print("Raiz cuadrada")
            resultado = (Numero1)**0.5
        case 'F':
            break
        case _:
            print("Modo no valido")
    print(f"Resultado = {resultado}")