##  Problema 1: Despegue del avión

**Enunciado:**  
Un F-16 recorre la pista del aeropuerto José María Córdova durante 10 segundos. En cada segundo, el piloto decide si acelera o no. El programa calcula si la sustentación llega a ser mayor que el peso para poder despegar, además de la distancia recorrida.

###  Tabla de Variables
| Variable | Significado | Unidad |
|----------|-------------|--------|
| masa | Masa del avión | kg |
| g | Aceleración de la gravedad | m/s² |
| W | Peso del avión | N |
| S | Área alar | m² |
| CL_max | Coeficiente máximo de sustentación | - |
| rho | Densidad del aire | kg/m³ |
| velocidad | Velocidad actual del avión | m/s |
| a | Aceleración cuando el piloto acelera | m/s² |
| tiempo_total | Duración de la carrera | s |
| L | Sustentación | N |
| distancia | Distancia recorrida | m |

###  Fórmulas Matemáticas
- Peso:  
  
  W = m \cdot g
  

- Sustentación:  
  
  L = \tfrac{1}{2} \cdot \rho \cdot V^2 \cdot S \cdot C_L
  

- Distancia acumulada:  
  
  d = d + V \cdot \Delta t
  

###  Pseudocódigo 
```

INICIO
Definir masa, g, S, CL\_max, rho
W = masa \* g
velocidad = 0
distancia = 0
a = 6.3
rho = 1.225
tiempo\_total = 10

PARA t DESDE 1 HASTA tiempo\_total HACER
LEER decision (1 = acelera, 0 = no acelera)
SI decision = 1 ENTONCES
velocidad = velocidad + a
FIN SI

```
  L = 0.5 * rho * velocidad^2 * S * CL_max
  distancia = distancia + velocidad

  IMPRIMIR "Segundo ", t, " velocidad=", velocidad, " sustentación=", L

  SI L >= W ENTONCES
      IMPRIMIR "El avión despega en el segundo ", t
      IMPRIMIR "Distancia recorrida = ", distancia
      TERMINAR
  FIN SI
```

FIN PARA

IMPRIMIR "El avión no despegó en 10 segundos"
FIN

```

---

##  Problema 2: Combustible en vuelo

**Enunciado:**  
Un avión inicia con cierta cantidad de combustible. Durante 5 minutos de vuelo. El programa verifica si el combustible alcanza para ascender.

###  Tabla de Variables
| Variable             | Significado                             | Unidad          |
| -------------------- | --------------------------------------- | --------------- |
| combustible\_inicial | Cantidad inicial de combustible         | litros o kg     |
| combustible          | Combustible disponible en cada instante | litros o kg     |
| consumo\_ascenso     | Consumo de combustible en ascenso       | litros/s o kg/s |
| tiempo\_total        | Duración total del ascenso (5 min)      | segundos (s)    |
| t                    | Tiempo transcurrido                     | segundos (s)    |


###  Fórmulas Matemáticas
- Actualización de combustible:  
  
  combustible(t)=combustible(t−1)−consumo_ascenso⋅Δt
  
- Condición de agotamiento:

  combustible(t)≤0
  
- Condicion de exito:

  combustible(t)>0para todo t∈[0,tiempo_total]


###  Pseudocódigo Universal
```

INICIO
    Definir combustible_inicial
    Definir consumo_ascenso
    Definir tiempo_total = 300
    combustible = combustible_inicial

    PARA t DESDE 1 HASTA tiempo_total HACER
        combustible = combustible - consumo_ascenso

        SI combustible <= 0 ENTONCES
            IMPRIMIR "Se acabó el combustible en el segundo ", t
            TERMINAR
        FIN SI
    FIN PARA

    IMPRIMIR "El avión completó el ascenso con ", combustible, " de combustible"
FIN

```

---

##  Problema 3: Arrastre en crucero

**Enunciado:**  
Un avión vuela a una velocidad inicial. Durante 8 segundos, el piloto decide si sube o baja la velocidad. El programa calcula la fuerza de arrastre y avisa si esta se vuelve demasiado grande.

###  Tabla de Variables
| Variable | Significado | Unidad |
|----------|-------------|--------|
| V | Velocidad del avión | m/s |
| Cd | Coeficiente de arrastre | - |
| S | Área de referencia | m² |
| rho | Densidad del aire | kg/m³ |
| D | Fuerza de arrastre | N |
| tiempo_total | Tiempo de simulación (8 s) | s |
| decision | Acción del piloto (1 = acelerar, 0 = desacelerar) | - |
| aumento | Cambio de velocidad | m/s |

###  Fórmulas Matemáticas
- Arrastre aerodinámico:  
  
  D = \tfrac{1}{2} \cdot \rho \cdot V^2 \cdot S \cdot C_d
  

- Actualización de velocidad:  
  
  V = V \pm \Delta V
  

###  Pseudocódigo 
```

INICIO
Definir velocidad inicial V
Definir rho, S, Cd
tiempo\_total = 8
aumento = 10

PARA t DESDE 1 HASTA tiempo\_total HACER
LEER decision (1 = acelerar, 0 = desacelerar)
SI decision = 1 ENTONCES
V = V + aumento
SINO
V = V - aumento
FIN SI

```
  D = 0.5 * rho * V^2 * S * Cd

  IMPRIMIR "Segundo ", t, " velocidad=", V, " arrastre=", D

  SI D > 100000 ENTONCES
      IMPRIMIR " Arrastre excesivo en el segundo ", t
  FIN SI
```

FIN PARA
FIN