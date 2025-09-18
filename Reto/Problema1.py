masa = float(input("Ingrese la masa del avión (kg): "))
S = float(input("Ingrese el área alar S (m^2): "))
CL_max = float(input("Ingrese el CL_max: "))


g = 9.81
rho = 1.225
W = masa * g   
velocidad = 0  
distancia = 0  
a = 6.3        
tiempo_total = 10

for t in range(1, tiempo_total + 1):
    decision = int(input(f"Segundo {t}: ¿Acelerar? (1 = sí, 0 = no): "))

    if decision == 1:
        velocidad += a

    L = 0.5 * rho * (velocidad ** 2) * S * CL_max
    distancia += velocidad
    print(f"Segundo {t}: velocidad = {velocidad:.2f} m/s, sustentación = {L:.2f} N")

    if L >= W:
        print(f"\nEl avión despega en el segundo {t}")
        print(f"Distancia recorrida = {distancia:.2f} m")
        break
else:
    print("\nEl avión no despegó en 10 segundos")