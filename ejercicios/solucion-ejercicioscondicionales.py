# Condicional
# Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

numero = int(input("ingrese numero"))
resultado = numero % 3
if resultado == 0:
    print(numero , "es divisble entre 3") 
