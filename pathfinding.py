import sys
import random
import heapq
import pygame

#inicializamos pygame
pygame.init()
# parametros de la ventana
ANCHO = 400
ALTO = 400
tamaño_celda = 25
# Configuramos las dimensiones de la ventana y su título
ventana = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Camino encontrado en el mapa")

# Creamos una matriz de 20x20 con valor 0
matriz = [[0 for _ in range(20)] for _ in range(20)]

# Generamos obstáculos
for i in range(120):
    fila = random.randint(0, 19)
    columna = random.randint(0, 19)
    matriz[fila][columna] = 1
# Asignamos las posiciones iniciales y finales de A1 y A2

A1_posicion_inicial = (1, 0)
A1_posicion_destino = (1, 17)
A2_posicion_inicial = (19, 19)
A2_posicion_destino = (1, 17)

#Marcamos las posiciones iniciales y finales en la matriz
matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5


print("===========================================")

#Visualizamos A1 y A2
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

#Visualizamos el camino encontrado en la matriz
#Crear una copia de la matriz original para no alterarla

matriz_caminos = [fila[:] for fila in matriz]
for x,y in camino_A1:
    matriz_caminos[x][y] = 'x'
for x,y in camino_A2:
    matriz_caminos[x][y] = 'y'

print("===========================================")
#Visualizamos A1 y A2
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

#Visualizamos los caminos encontrados en el mapa
#Crear una copia de la matriz original para no alterarla
matriz_caminos = [fila[:] for fila in matriz]

print("===========================================")
for x,y in camino_A1:
    matriz_caminos[x][y] = 'x'
for x,y in camino_A2:
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

#Marcamos las posiciones iniciales y finales en la matriz
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
