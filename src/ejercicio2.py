# Determinar si un numero es par o impar
numero = int(input("Ingrese un número entero: "))
residuo = numero % 2
#si residuo es 0 es par
if residuo == 0: 
    print(numero, " es par")
#si no es impar
else:
    print(numero, "es impar")