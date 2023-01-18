import sys
import random
import heapq
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# inicializamos pygame
pygame.init()
# parametros de la ventana
ANCHO = 400
ALTO = 400
tamaño_celda = 25

#
# TODO
# no se asegura que sean al menos 40 obstáculos
# Agregar musica
# Funcion para dibujar camino más corto en todos los casos
# Poder colocar a los agentes dentro de la matriz.
# Que no haya necesidad de interactuar con la terminal

# Creamos una matriz de 20x20 con valor 0
matriz = [[0 for _ in range(20)] for _ in range(20)]
# Funcion que muestra un cuadro de dialogo para que el usuario
# Pregunta al usuario si quiere que sean generados de manera aleatoria o agregados de manera manual
obstacle_choice = messagebox.askyesno(
    "Opción de obstáculos", "¿Deseas usar obstaculos generados de manera aleatoria?")

# If user chooses "yes", use randomly generated obstacles
if obstacle_choice:
    # ingrese el numero de obstaculos deseados
    numero_obstaculos = int(input("Ingrese el número de obstáculos deseados:"))
    # Generamos obstáculos
    for i in range(numero_obstaculos):
        fila = random.randint(0, 19)
        columna = random.randint(0, 19)
        matriz[fila][columna] = 1
# Si el usuario escoge no, usa obstaculos colocados de manera manual
else:
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
    matriz[5][9] = 1
    matriz[9][9] = 1
    matriz[10][9] = 1
    matriz[11][9] = 1
    matriz[12][9] = 1
    matriz[13][9] = 1
    matriz[4][10] = 1
    matriz[1][11] = 1
    matriz[2][11] = 1
    matriz[3][11] = 1
    matriz[4][11] = 1
    matriz[5][11] = 1
    matriz[0][11] = 1
    matriz[7][12] = 1
    matriz[8][12] = 1
    matriz[7][13] = 1
    matriz[8][13] = 1


A1_posicion_inicial = tuple(map(int, input(
    "Ingrese la posición inicial del agente A1 en formato (fila,columna):").split(',')))
A1_posicion_destino = tuple(map(int, input(
    "Ingrese la posición destino del agente A1 en formato (fila,columna):").split(',')))
A2_posicion_inicial = tuple(map(int, input(
    "Ingrese la posición inicial del agente A2 en formato (fila,columna):").split(',')))
A2_posicion_destino = tuple(map(int, input(
    "Ingrese la posición destino del agente A2 en formato (fila,columna):").split(',')))

# Marcamos las posiciones iniciales y finales en la matriz
matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5


print("===========================================")

# Visualizamos A1 y A2
for fila in matriz:
    for valor in fila:
        if valor == 0:
            print(".", end=" ")
        elif valor == 1:
            print("#", end=" ")
        elif valor == 2:
            print("A1", end=" ")
        elif valor == 3:
            print("A2", end=" ")
        elif valor == 5:
            print("G", end=" ")
        elif valor == "x":
            print("x", end=" ")
        elif valor == "y":
            print("y", end=" ")
    print()

print("===========================================")
#copia de la matriz original para usarla con A*
matriz_astar = [fila[:] for fila in matriz]

# Función para obtener los vecinos de una posición en la matriz


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

# Función para encontrar el camino mínimo usando Dijkstra


def Dijkstra(matriz, inicio, destino):
    # Creamos una cola de prioridad para almacenar los nodos a explorar
    cola = []
    # agregamos el nodo inicial con distancia 0
    heapq.heappush(cola, (0, inicio))
    # creamos un diccionario para almacenar los nodos visitados
    visitados = {}
    # Inicializamos la distancia del nodo inicial en 0
    visitados[inicio] = 0
    # creamos un diccionario para almacenar el camino desde el nodo inicial hasta cada uno de los nodos visitados
    camino = {}
    camino[inicio] = [inicio]
    # mientras la cola no esté vacía
    while cola:
        # obtenemos el nodo con menor distancia
        current = heapq.heappop(cola)[1]
        # para cada vecino del nodo actual
        for vecino in vecinos(matriz, current):
            # si el vecino no ha sido visitado
            if vecino not in visitados:
                # si el vecino es un obstáculo, ignoramos
                if matriz[vecino[0]][vecino[1]] == 1:
                    continue
                # calculamos la distancia del vecino
                distancia = visitados[current] + 1
                # actualizamos la distancia del vecino si es menor
                if vecino not in visitados or distancia < visitados[vecino]:
                    visitados[vecino] = distancia
                    camino[vecino] = camino[current] + [vecino]
                    # agregamos el vecino a la cola de prioridad
                    heapq.heappush(cola, (distancia, vecino))
        # si el nodo actual es el destino, devolvemos el camino
        if current == destino:
            return camino[current]
    # si no se encontró un camino, devolvemos None
    return None


camino_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
print("===========================================")
print("Distancia A1: ", len(camino_A1), "unidades")
print("===========================================")
print("Camino A1: ", camino_A1)

camino_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)
print("===========================================")
print("Distancia A2: ", len(camino_A2), "unidades")
print("===========================================")
print("Camino A2: ", camino_A2)
print("===========================================")
# Visualizamos el camino encontrado en la matriz
# Crear una copia de la matriz original para no alterarla

matriz_caminos = [fila[:] for fila in matriz]
for x, y in camino_A1:
    matriz_caminos[x][y] = 'x'
for x, y in camino_A2:
    matriz_caminos[x][y] = 'y'

print("===========================================")
# Visualizamos A1 y A2
for fila in matriz_caminos:
    for valor in fila:
        if valor == 0:
            print(".", end=" ")
        elif valor == 1:
            print("#", end=" ")
        elif valor == "x":
            print("x", end=" ")
        elif valor == "y":
            print("y", end=" ")
        elif valor == 2:
            print("A1", end=" ")
        elif valor == 3:
            print("A2", end=" ")
    print()
print("===========================================")

# Almacenamos la distancia y el camino encontrado
distancia_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
camino_A1 = distancia_A1

distancia_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)
camino_A2 = distancia_A1

# Visualizamos el camino encontrado en la matriz
matriz_caminos = [fila[:] for fila in matriz]

for i, j in camino_A1:
    matriz_caminos[i][j] = "x"

camino_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
for i, j in camino_A2:
    matriz_caminos[i][j] = "y"
camino_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)

# Visualizamos los caminos encontrados en el mapa
# Crear una copia de la matriz original para no alterarla
matriz_caminos = [fila[:] for fila in matriz]

print("===========================================")
for x, y in camino_A1:
    matriz_caminos[x][y] = 'x'
for x, y in camino_A2:
    matriz_caminos[x][y] = 'y'

for fila in matriz_caminos:
    for valor in fila:
        if valor == 0:
            print(".", end=" ")
        elif valor == 1:
            print("#", end=" ")
        elif valor == 2:
            print("A1", end=" ")
        elif valor == 3:
            print("A2", end=" ")
        elif valor == "x":
            print("x", end=" ")
        elif valor == "y":
            print("y", end=" ")
    print()

print("===========================================")


def manhattan(pos1, pos2):
    # calculamos la distancia manhattan entre dos puntos
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


# A*
inicio = A1_posicion_inicial
start = inicio


def A_star(matriz, inicio, destino):
    # creamos una cola de prioridad para almacenar los nodos a explorar
    abierta = []
    cerrada = []
    cola = []
    # agregamos el nodo inicial a la lista abierta con un costo g=0
    heapq.heappush(abierta, (0, 0, inicio))
    # creamos un diccionario para almacenar el costo g de cada nodo
    g_cost = {inicio: 0}
    # creamos un diccionario para almacenar el costo f de cada nodo
    f_cost = {inicio: manhattan(inicio, destino)}
    # mientras la lista abierta no esté vacía
    while abierta:
        # extraemos el nodo con menor f costo
        f, g, current = heapq.heappop(abierta)
        # agregamos el nodo a la lista cerrada
        cerrada.append(current)
        # si encontramos el destino
        if current == destino:
            # retornamos el camino
            return path(current, g_cost)
        # iteramos sobre los vecinos del nodo actual
        for neighbor in vecinos(matriz, current):
            # si el vecino esta en la lista cerrada o es un obstaculo
            if neighbor in cerrada or matriz[neighbor[0]][neighbor[1]] == 1:
                continue
            # calculamos el costo g del vecino
            temp_g = g + 1
            # si el vecino no esta en la lista abierta o el costo g es menor que el costo g anterior
            if neighbor not in [i[2] for i in abierta] or temp_g < g_cost[neighbor]:
                # actualizamos el costo g
                g_cost[neighbor] = temp_g
                # calculamos el costo f del vecino
                f = temp_g + manhattan(neighbor, destino)
                # agregamos el vecino a la lista abierta con su costo f
                heapq.heappush(abierta, (f, temp_g, neighbor))
    # si no se encuentra un camino retornamos None
    return None


def path(current, g_cost):
    # creamos una lista para almacenar el camino encontrado
    camino = [current]
    # mientras el nodo actual no sea el inicio
    while current != inicio:
        # iteramos sobre los vecinos del nodo actual
        for neighbor in vecinos(matriz, current):
            # si el vecino tiene un costo g menor
            if g_cost.get(neighbor, float('inf')) <= g_cost.get(current, float('inf')):
                current = neighbor
                # actualizamos el nodo actual
                current = neighbor
                # agregamos el vecino al camino
                camino.append(current)
    # retornamos el camino encontrado
    return camino[::-1]


# Preguntamos al usuario qué algoritmo desea utilizar
opcion = int(input("Ingrese 1 para A* o 2 para Dijkstra:"))


# Verificamos la opción seleccionada
if opcion == 1:
    # Llamamos a la función A*
    camino = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
else:
    # Llamamos a la función Dijkstra
    camino = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)

if camino:
    for pos in camino:
        matriz_astar = matriz
        matriz_astar[pos[0]][pos[1]] = "x"

print("===========================================")
for x, y in camino_A1:
    matriz_astar[x][y] = 'x'
for x, y in camino_A2:
    matriz_astar[x][y] = 'y'

for fila in matriz_astar:
    for valor in fila:
        if valor == 0:
            print(".", end=" ")
        elif valor == 1:
            print("#", end=" ")
        elif valor == 2:
            print("A1", end=" ")
        elif valor == 3:
            print("A2", end=" ")
        elif valor == "x":
            print("x", end=" ")
        elif valor == "y":
            print("y", end=" ")
    print()

print("===========================================")

camino_A1 = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
print("===========================================")
print("A*.Distancia A1: ", len(camino_A1), "unidades")
print("===========================================")
print("A*.Camino A1: ", camino_A1)

camino_A2 = A_star(matriz, A2_posicion_inicial, A2_posicion_destino)
print("===========================================")
print("A*.Distancia A2: ", len(camino_A2), "unidades")
print("===========================================")
print("A*.Camino A2: ", camino_A2)
print("===========================================")

# Configuramos las dimensiones de la ventana y su título
ventana = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Camino encontrado en el mapa")

# Crear la ventana
ventana = pygame.display.set_mode((500, 500))

# Cargar las imagenes
imagen_obstaculo = pygame.image.load("obstaculo.png")
imagen_agente = pygame.image.load("agente.png")
imagen_agente2 = pygame.image.load("agente2.png")
imagen_meta = pygame.image.load("meta.png")
imagen_camino = pygame.image.load("camino.png")
imagen_camino2 = pygame.image.load("camino2.png")
imagen_piso = pygame.image.load("piso.png")

# Marcamos las posiciones iniciales y finales en la matriz
matriz_caminos[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz_caminos[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz_caminos[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz_caminos[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5

dibujo = {
    1: imagen_obstaculo,
    2: imagen_agente,
    3: imagen_agente2,
    5: imagen_meta,
    'x': imagen_camino,
    'y': imagen_camino2,
    0: imagen_piso
}


# Dibuja cada celda de matriz_caminos en su posición correspondiente
for i, fila in enumerate(matriz_caminos):
    for j, valor in enumerate(fila):
        x = j * 25
        y = i * 25
        ventana.blit(dibujo[valor], (x, y))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
