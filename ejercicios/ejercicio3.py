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
#Determinar la escala del imc
if imc > 18.5 and imc < 24.9:
    mensaje = "normal"
if imc > 25 and imc < 29.9:
    mensaje = "sobrepeso"
if imc > 30 and imc < 34.9:
    mensaje = "obesidad I"
if imc > 35 and imc < 39.9:
    mensaje = "obesidad II"
if imc >= 40:
    mensaje = "obesidad EXTREMA"

print(f"Paciente {nombre}, tiene un IMC de {imc:0.2f} y su condición es {mensaje}.") 


