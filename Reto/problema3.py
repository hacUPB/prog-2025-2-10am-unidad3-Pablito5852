V = float(input("Ingrese la velocidad inicial: "))            # velocidad inicial
rho = float(input("Ingrese la densidad del aire: "))       # densidad del aire (kg/m^3)
S = float(input("Ingrese la superficie alar: "))             # superficie alar (m^2)
Cd = float(input("Ingrese el coeficiente de arrastre: "))          # coeficiente de arrastre
tiempo_total = 8
aumento = 10

for t in range(1, tiempo_total + 1):
    decision = int(input(f"Segundo {t}: ¿Acelerar (1) o Desacelerar (0)? "))

    if decision == 1:
        V = V + aumento
    else:
        V = V - aumento

    D = 0.5 * rho * (V ** 2) * S * Cd

    print(f"Segundo {t}: velocidad = {V}, arrastre = {D}")

    if D > 100000:
        print(f"Arrastre excesivo en el segundo {t}")