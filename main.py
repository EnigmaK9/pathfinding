import random
import heapq


print("============================================================")
print(" paso 1, Inicializamos la matriz con 20 filas y 20 columnas, todas con valor 0")
print("Generamos 24 obstáculos aleatorios")
print("============================================================")
# inicializamos la matriz con 20 filas y 20 columnas, todas con valor 0
matriz = [[0 for _ in range(20)] for _ in range(20)]

# agregamos algunos obstáculos, marcados con el valor 1
#matriz[4][7] = 1
#matriz[5][9] = 1
#matriz[6][5] = 1
#matriz[8][2] = 1
#matriz[9][12] = 1
# generamos 24 obstáculos aleatorios
for _ in range(24):
    fila = random.randint(0, 19)
    columna = random.randint(0, 19)
    matriz[fila][columna] = 1

# imprimimos la matriz
for fila in matriz:
    print(fila)

# Para inicializar la posición inicial de A1 y A2 en la matriz, podemos agregar una tupla con las coordenadas (fila, columna) a cada agente. Luego, podemos marcar estas posiciones en la matriz con un valor específico, por ejemplo 2 para A1 y 3 para A2.

# inicializamos la posición inicial de A1 y A2 en la matriz
A1_posicion_inicial = (0, 0)
A2_posicion_inicial = (19, 19)

# marcamos las posiciones iniciales de A1 y A2 en la matriz
matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3


# imprimimos la matriz
print("============================================================")
print(" paso 2, inicializamos la posición de A1 y A2 en la matriz, A1 tiene el valor de 2 y A3 tiene el valor de 3")
print("============================================================")

for fila in matriz:
    print(fila)

# Paso 3, implementa el algoritmo de Dijkstra

import heapq

# define una función para calcular el vecino más cercano
def obtener_vecino_mas_cercano(posicion, matriz):
    fila, columna = posicion
    vecinos = []
    # comprueba los vecinos de la celda actual (arriba, abajo, derecha, izquierda)
    if fila > 0:
        vecinos.append((fila - 1, columna))
    if fila < len(matriz) - 1:
        vecinos.append((fila + 1, columna))
    if columna > 0:
        vecinos.append((fila, columna - 1))
    if columna < len(matriz[0]) - 1:
        vecinos.append((fila, columna + 1))
    return vecinos

# define una función para aplicar Dijkstra a un agente
def aplicar_dijkstra(matriz, posicion_inicial, posicion_destino):
    # inicializamos la distancia desde la posición inicial a cada celda con infinito
    distancias = [[float('inf') for _ in fila] for fila in matriz]
    # la distancia desde la posición inicial a sí misma es 0
    distancias[posicion_inicial[0]][posicion_inicial[1]] = 0
    # inicializamos el conjunto de celdas visitadas
    visitados = set()
    # inicializamos la cola de prioridad con la posición inicial
    cola_prioridad = [(0, posicion_inicial)]
    while cola_prioridad:
        # obtenemos la celda con menor distancia
        distancia, posicion = heapq.heappop(cola_prioridad)
        # si la celda actual es la posición de destino, terminamos
        if posicion == posicion_destino:
            break
        # si la celda actual ya fue visitada, continuamos con la siguiente
        if posicion in visitados:
            continue
        # marcamos la celda actual como visitada
        visitados.add(posicion)
        # obtenemos los vecinos de la celda actual
        vecinos = obtener_vecino_mas_cercano(posicion, matriz)
        # actualizamos la distancia a cada vecino
        for vecino in vecinos:
            nueva_distancia = distancia + matriz[vecino[0]][vecino[1]]
            if nueva_distancia < distancias[vecino[0]][vecino[1]]:
                distancias[vecino[0]][vecino[1]] = nueva_distancia
                # añadimos el vecino a la cola de prioridad
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
    # devolvemos la matriz de distancias
    return distancias

# usamos la función para aplicar Dijkstra a cada agente
distancias_A1 = aplicar_dijkstra(matriz, posicion_inicial_A1, posicion_destino_A1)
distancias_A2 = aplicar_dijkstra(matriz, posicion_inicial_A2, posicion_destino_A2)

# imprimimos las distancias obtenidas
print(distancias_A1)
print(distancias_A2)

#Esto debería calcular las distancias mínimas desde la posición inicial hasta la posición de destino para cada agente, utilizando el algoritmo de Dijkstra.


