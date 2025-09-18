# Seccion de las funciones
def suma(a, b):
	resultado = a + b
	return resultado
def resta(a, b):
	res = a - b
	return res

	


# Seccion para el programa
#Llamando a la función
numero1 = 5
numero2 = 3
# Las variables pertenecen al contexto donde fueron creadas.
a = 1000
b = 5000
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")


res_resta = resta(a, b)
print(res_resta)


