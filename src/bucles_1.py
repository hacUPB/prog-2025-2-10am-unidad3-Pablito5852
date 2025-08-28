'''
numero = 100
while numero >= 0:
    print(numero)
    numero -= 5     #numero = numero + 5
'''
# Solicitar 2 numeros al usuario e imprimir los pares entre ellos

Numero1 = int(input("ingrese el primer numero"))
Numero2 = int(input("ingrese el segundo numero"))
if Numero1 > Numero2:
    mayor = Numero1
    menor = Numero2
else:
    mayor = Numero2
    menor = Numero1
'''
while menor <= mayor:
    if menor % 2 == 0:
     print(menor)
    menor += 1
'''
if menor % 2 == 1:
    menor  += 1
while menor <= mayor:
    print(menor)
    menor += 2
