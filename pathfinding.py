import sys
import heapq
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import print_module
from dijkstra_module import Dijkstra
#from a_star_module import A_star
from obstaculos import crear_obstaculos_fijos
from obstaculos import crear_obstaculos_aleatorios
import graphics

# inicializamos pygame
pygame.init()
# parametros de la ventana
ANCHO = 400
ALTO = 400
tamaño_celda = 25



# Creamos una matriz de 20x20 con valor 0
matriz = [[0 for _ in range(20)] for _ in range(20)]
# Funcion que muestra un cuadro de dialogo para que el usuario
# Pregunta al usuario si quiere que sean generados de manera aleatoria o agregados de manera manual
obstacle_choice = messagebox.askyesno(
    "Opción de obstáculos", "¿Deseas usar obstaculos generados de manera aleatoria?")

# If user chooses "yes", use randomly generated obstacles
if obstacle_choice:
    crear_obstaculos_aleatorios(matriz)
# Si el usuario escoge no, usa obstaculos colocados de manera manual
else:
    # agregamos algunos obstáculos, marcados con el valor 1
    crear_obstaculos_fijos(matriz)


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

print_module.print_path(matriz)

#copia de la matriz original para usarla con A*
matriz_star = [fila[:] for fila in matriz]

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

# Función para encontrar el camino mínimo usando Dijkstra iba aqui


camino_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
print("===========================================")
print("Dijkstra. Distancia A1: ", len(camino_A1), "unidades")
print("===========================================")
print("Camino A1: ", camino_A1)

camino_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)
print("===========================================")
print("Dijkstra. Distancia A2: ", len(camino_A2), "unidades")
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
    
print_module.print_path(matriz_caminos)

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

print_module.print_path(matriz_caminos)

#A estrella va aqui

# A*

def manhattan(pos1, pos2):
    # calculamos la distancia manhattan entre dos puntos
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) 

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

camino_star_A1 = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
camino_star_A2 = A_star(matriz,A2_posicion_inicial, A2_posicion_destino)
camino_dijkstra = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)

if camino_star_A1:
    for pos in camino_star_A1:
        matriz_star = matriz
        matriz_star[pos[0]][pos[1]] = "x"
if camino_star_A2:
    for pos in camino_star_A2:
        matriz_star = matriz
        matriz_star[pos[0]][pos[1]] = "y"

for x, y in camino_A1:
    matriz_star[x][y] = 'x'
for x, y in camino_A2:
    matriz_star[x][y] = 'y'
    
print_module.print_path(matriz_star)

camino_A1_star = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
print("===========================================")
print("A*.Distancia A1: ", len(camino_A1_star), "unidades")
print("===========================================")
print("A*.Camino A1: ", camino_A1_star)

camino_A2_star = A_star(matriz, A2_posicion_inicial, A2_posicion_destino)
print("===========================================")
print("A*.Distancia A2: ", len(camino_A2_star), "unidades")
print("===========================================")
print("A*.Camino A2: ", camino_A2_star)
print("===========================================")


# Visualizamos el camino encontrado en la matriz
# Crear una copia de la matriz original para no alterarla

matriz_star = [fila[:] for fila in matriz]
for x, y in camino_A1_star:
    matriz_star[x][y] = 'x'
for x, y in camino_A2_star:
    matriz_star[x][y] = 'y'
    
print_module.print_path(matriz_star)








# Marcamos las posiciones iniciales y finales en la matriz
matriz_caminos[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz_caminos[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz_caminos[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz_caminos[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5

graphics.dibujar_mapa(matriz_caminos)
graphics.dibujar_mapa(matriz_star)