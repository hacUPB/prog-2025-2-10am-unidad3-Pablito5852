'''
import mod_funciones
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
mod_funciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
mod_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones.tabla(multiplicando)
'''
from mod_funciones import *
def main():
    while True:
        opc = menu()
        match opc: 
            case 1:
                print("Calcular si un numero es primo.")
                valor = int(input("ingrese un numero mayor que 1 >> "))
                primo(valor)
            case 2:
                print("imprime las serie de fibonacci.")
                num = int(input("ingrese el numero de terminos >> "))
                fibonacci(num)
            case 3:
                print("Imprime la tabla de miltiplicacion.")
                numero = int(input("ingrese el numero >> "))
                tabla(numero)
            case 4:
                break
            case _:
                print("La opcion que ingreso no es valida")



if _name_ == "_main_":
    main()
