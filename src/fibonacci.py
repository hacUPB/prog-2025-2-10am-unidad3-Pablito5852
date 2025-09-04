numero = int(input("ingrese el numero de terminos de la serie"))
if numero <= 0:
    print("Por favor, ingrese el numero positivo")
elif numero == 1:
    print("serie de Fibonacci")
    print(0)
else:
    a = 0
    b = 1
    contador = 2
    print("serie de Fibonacci")
    print(a)
    print(b)

    while contador < numero:
        siguiente = a + b
        print(siguiente)
        a = b
        b = siguiente
        contador += 1 