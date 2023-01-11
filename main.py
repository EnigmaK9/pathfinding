import random
import heapq
from termcolor import colored



print("============================================================")
print("Paso 1: inicializamos la matriz 20x20")
print("Generamos los obstáculos")
print("============================================================")
# inicializamos la matriz con 20 filas y 20 columnas, todas con valor 0
matriz = [[0 for _ in range(20)] for _ in range(20)]

# agregamos algunos obstáculos, marcados con el valor 1
matriz[4][2] = 1

matriz[4][3] = 1

matriz[3][4] = 1


matriz[4][6] = 1

matriz[5][7] = 1
matriz[6][7] = 1
matriz[7][7] = 1

matriz[5][8] = 1
matriz[6][8] = 1
matriz[7][8] = 1
matriz[8][8] = 1
matriz[9][8] = 1
matriz[10][8] = 1

matriz[5][9]  = 1
matriz[9][9]  = 1
matriz[10][9] = 1
matriz[10][9] = 1
matriz[11][9] = 1
matriz[12][9] = 1
matriz[13][9] = 1

matriz[4][10] = 1

matriz[1][11] = 1
matriz[2][11] = 1
matriz[3][11] = 1
matriz[4][11] = 1
matriz[0][11] = 1
matriz[7][12] = 1
matriz[8][12] = 1

matriz[7][13] = 1
matriz[8][13] = 1

# generamos 24 obstáculos aleatorios

#for _ in range(24):
#    fila = random.randint(0, 19)
#    columna = random.randint(0, 19)
#    matriz[fila][columna] = 1
# Cambiamos a color rojo los 1 para una mejor visualización
for fila in matriz:
    for num in fila:
        if num == 1:
            print(colored(num, 'red'), end=' ')
        else:
            print(num, end=' ')
    print()
# imprimimos la matriz sin color rojo
#for fila in matriz:
#    print(fila)

# Para inicializar la posición inicial de A1 y A2 en la matriz, podemos agregar una tupla con las coordenadas (fila, columna) a cada agente. Luego, podemos marcar estas posiciones en la matriz con un valor específico, por ejemplo 2 para A1 y 3 para A2.

# Costo del movimiento 
costo_movimiento = 1

# inicializamos la posición inicial de A1 y A2 en la matriz
A1_posicion_inicial = (4, 9)
A1_posicion_destino = (5, 10)
A2_posicion_inicial = (3, 9)
A2_posicion_destino = (5, 10)

# marcamos las posiciones iniciales de A1 y A2 en la matriz
matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3


# imprimimos la matriz
print("============================================================")
print(" Paso 2, inicializamos la posición de A1 y A2 en la matriz, A1 tiene el valor de 2 y A3 tiene el valor de 3")
print("============================================================")

for fila in matriz:
    for num in fila:
        if num ==1:
            print(colored(num,'red'),end=' ')
        elif num ==2:
            print(colored(num,'blue'),end=' ')
        elif num ==3:
            print(colored(num,'yellow'),end=' ')    
        else:
            print(num, end=' ')
    print(fila)

# Paso 3, implementa el algoritmo de Dijkstra

def obtener_vecino_mas_cercano(posicion_inicial, matriz, costo_movimiento):
    # Inicializamos la distancia de todos los nodos como infinito
    distancias = [[float('inf') for _ in range(20)] for _ in range(20)]
    distancias[posicion_inicial[0]][posicion_inicial[1]] = 0
    predecesores = [[(0,0) for _ in range(20)] for _ in range(20)]
    # Inicializamos la cola de prioridad con el nodo inicial
    cola = [(0, posicion_inicial[0], posicion_inicial[1])]
    heapq.heapify(cola)
    
    while cola:
        # obtenemos el nodo con la distancia mínima
        distancia, fila, columna = heapq.heappop(cola)
        vecinos = [(fila+1, columna), (fila-1, columna), (fila, columna+1), (fila, columna-1)]
        
        for vecino in vecinos:
            # Verificamos si el vecino está dentro de los límites de la matriz
            if vecino[0] < 0 or vecino[0] >= 20 or vecino[1] < 0 or vecino[1] >= 20:
                continue
            # Verificamos si el vecino es un obstáculo
            if matriz[vecino[0]][vecino[1]] == 1:
                continue
            # si se encuentra un camino mas corto se actualiza la distancia y el predecesor
            if distancias[vecino[0]][vecino[1]] > distancias[fila][columna] + costo_movimiento:
                distancias[vecino[0]][vecino[1]] = distancias[fila][columna] + costo_movimiento
                predecesores[vecino[0]][vecino[1]] = (fila, columna)
                heapq.heappush(cola, (distancias[vecino[0]][vecino[1]], vecino[0], vecino[1]))

    # retorna el camino mas corto y la distancia total
    return predecesores, distancias[19][19]

nearest_neighbor_A1 = obtener_vecino_mas_cercano(A1_posicion_inicial,matriz,costo_movimiento)

# print('\n'.join(map(str, nearest_neighbor_A1)))
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

distancias_A1 = aplicar_dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
distancias_A2 = aplicar_dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)

# imprimimos las distancias obtenidas
print("============================================================")
print("Usamos la funcion para imprimir la distancia obtenida en A1")
print("============================================================")
print('\n'.join(map(str, distancias_A1)))
print("============================================================")
print("Usamos la funcion para imprimir la distancia obtenida en A2")
print("============================================================")
print('\n'.join(map(str, distancias_A2)))

#Esto debería calcular las distancias mínimas desde la posición inicial hasta la posición de destino para cada agente, utilizando el algoritmo de Dijkstra.


