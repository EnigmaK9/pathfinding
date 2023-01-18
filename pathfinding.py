import sys
import heapq
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import print_module
from dijkstra_module import Dijkstra
from a_star_module import A_star
from a_star_module import manhattan
from a_star_module import path

from obstaculos import crear_obstaculos_fijos
from obstaculos import crear_obstaculos_aleatorios
import graphics

# inicializamos pygame
pygame.init()



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
matriz_caminos_star = [fila[:] for fila in matriz]

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


# Función para encontrar el camino mínimo usando A*


camino_A1_star = A_star(matriz_star, A1_posicion_inicial, A1_posicion_destino)
print("===========================================")
print("A*. Distancia A1: ", len(camino_A1_star), "unidades")
print("===========================================")
print("Camino A1: ", camino_A1_star) 

camino_A2_star = A_star(matriz_star, A2_posicion_inicial, A2_posicion_destino)
print("===========================================")
print("Dijkstra. Distancia A2: ", len(camino_A2_star), "unidades")
print("===========================================")
print("Camino A2: ", camino_A2_star)
print("===========================================")

# Visualizamos el camino encontrado en la matriz
# Crear una copia de la matriz original para no alterarla

matriz_caminos_star = [fila[:] for fila in matriz]
for x, y in camino_A1_star:
    matriz_caminos_star[x][y] = 'x'
for x, y in camino_A2:
    matriz_caminos_star[x][y] = 'y'
    
print_module.print_path(matriz_caminos_star)

# Almacenamos la distancia y el camino encontrado
distancia_A1 = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
camino_A1 = distancia_A1

distancia_A2 = A_star(matriz, A2_posicion_inicial, A2_posicion_destino)
camino_A2 = distancia_A1

# Visualizamos el camino encontrado en la matriz
matriz_caminos_star = [fila[:] for fila in matriz]

for i, j in camino_A1_star:
    matriz_caminos_star[i][j] = "x"

camino_A1 = A_star(matriz, A1_posicion_inicial, A1_posicion_destino)
for i, j in camino_A2:
    matriz_caminos_star[i][j] = "y"
camino_A2 = A_star(matriz, A2_posicion_inicial, A2_posicion_destino)

print_module.print_path(matriz_caminos_star)
















# Marcamos las posiciones iniciales y finales en la matriz
matriz_caminos[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz_caminos[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz_caminos[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz_caminos[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5

graphics.dibujar_mapa(matriz_caminos)
graphics.dibujar_mapa(matriz_star)