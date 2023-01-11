import random
import heapq

matriz = [[0 for _ in range(20)] for _ in range(20)]

# Generamos obstáculos
for i in range(40):
    fila = random.randint(0, 19)
    columna = random.randint(0, 19)
    matriz[fila][columna] = 1

A1_posicion_inicial = (4, 9)
A1_posicion_destino = (5, 10)
A2_posicion_inicial = (3, 9)
A2_posicion_destino = (5, 10)

matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5

def vecinos(matriz, current):
    x, y = current
    vecinos = []
    if x > 0:
        vecinos.append((x - 1, y))
    if y > 0:
        vecinos.append((x, y - 1))
    if x < len(matriz) - 1:
        vecinos.append((x + 1, y))
    if y < len(matriz[0]) - 1:
        vecinos.append((x, y + 1))
    return vecinos


def Dijkstra(matriz, inicio, destino):
    cola = []
    heapq.heappush(cola, (0, inicio))
    visitados = {}
    visitados[inicio] = 0
    while cola:
        current = heapq.heappop(cola)[1]
        if current == destino:
            return visitados[current]
        for vecino in vecinos(matriz, current):
            if vecino not in visitados:
                if matriz[vecino[0]][vecino[1]] == 1:
                    continue
                distancia = visitados[current] + 1
                if vecino not in visitados or distancia < visitados[vecino]:
                    visitados[vecino] = distancia
                    heapq.heappush(cola, (distancia, vecino))
    return None
