#Ejercicio 7

'''
Variables de entrada
nombre              tipo
opcion              str
temperatura         float

Variables de salida
Nombre              tipo           
conversion          float

Variable de control
opcion
'''
opcion = 'Z'            #Asigno un valor diferente de Q
while opcion != 'Q' :
    opcion = input("F. Fahrenheit a celsius\nC. Celsius a Fahrenheit\nQ .Salir\n")
    opcion = opcion.upper()
    if opcion != 'Q':
        temperatura = float(input("ingrese la temperatura a convertir: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) * (5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C': 
                conversion = (temperatura * 9 /5) + 32
                print(f"{temperatura}°C = {conversion}°F")
            case _:
                print("Opcion no valida")

else:
    print("Saliendo del programa...")
