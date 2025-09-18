'''
numero = int(input("Ingrese el numero entero positivo: "))
while numero < 0:
    numero = int(input("Ingrese el numero entero positivo: "))
acum = 0
for cont in range (1,numero+1):
    if cont % 2 == 0:
        acum += cont #acum = acum + cont
print(f"La suma de los pares es: {acum}")
'''
mensaje = "Universidad pontificia Bolivariana"
numero = int(input("Ingrese el numero entero positivo: "))
for i in range (numero):
    print(mensaje)
