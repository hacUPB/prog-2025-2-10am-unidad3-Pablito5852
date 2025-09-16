nombre = input("ingresa tu nombre y apellido")
#opcion 2
print("Bienvenido: ", nombre)
#calcular el IMC de esa persona
#Leer peso, altura
peso = input("ingresa tu peso en kg: ")
peso = float(peso)
altura = input("ingresa tu talla en metros: ")
altura = float(altura)
#calculos
imc = peso/altura**2
#mostrar imc
print("Tu IMC = ", imc)
