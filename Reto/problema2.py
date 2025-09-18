combustible_inicial = float(input("Ingrese el combustible inicial (L): "))    # litros
consumo_ascenso = float(input("Ingrese el consumo por segundo en ascenso: "))        # litros por segundo
tiempo_total = 300             # segundos

combustible = combustible_inicial

for t in range(1, tiempo_total + 1):
    combustible -= consumo_ascenso

    if combustible <= 0:
        print(f"Se acabó el combustible en el segundo {t}")
        break
else:
    print(f"El avión completó el ascenso con {combustible} litros de combustible")

