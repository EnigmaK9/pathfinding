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
for i in range(40):
    fila = random.randint(0, 19)
    columna = random.randint(0, 19)
    matriz[fila][columna] = 1
# Asignamos las posiciones iniciales y finales de A1 y A2

A1_posicion_inicial = (4, 9)
A1_posicion_destino = (5, 10)
A2_posicion_inicial = (3, 9)
A2_posicion_destino = (5, 10)
#Marcamos las posiciones iniciales y finales en la matriz
matriz[A1_posicion_inicial[0]][A1_posicion_inicial[1]] = 2
matriz[A2_posicion_inicial[0]][A2_posicion_inicial[1]] = 3
matriz[A1_posicion_destino[0]][A1_posicion_destino[1]] = 5
matriz[A2_posicion_destino[0]][A2_posicion_destino[1]] = 5

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
print("Distancia A1: ", len(camino_A1))
print("Camino A1: ", camino_A1)

camino_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)
print("Distancia A2: ", len(camino_A2))
print("Camino A2: ", camino_A2)

#Visualizamos el camino encontrado en la matriz
#Crear una copia de la matriz original para no alterarla

matriz_caminos = [fila[:] for fila in matriz]
for x,y in camino_A1:
    matriz_caminos[x][y] = 'X'

for fila in matriz_caminos:
    print(fila)

# Almacenamos la distancia y el camino encontrado
distancia_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
camino_A1 = distancia_A1

distancia_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)
camino_A2 = distancia_A1

# Visualizamos el camino encontrado en la matriz
matriz_caminos = [fila[:] for fila in matriz]

for i, j in camino_A1:
    matriz_caminos[i][j] = "X"
for i, j in camino_A2:
    matriz_caminos[i][j] = "X"
camino_A1 = Dijkstra(matriz, A1_posicion_inicial, A1_posicion_destino)
camino_A2 = Dijkstra(matriz, A2_posicion_inicial, A2_posicion_destino)

#Visualizamos los caminos encontrados en el mapa
#Crear una copia de la matriz original para no alterarla
matriz_caminos = [fila[:] for fila in matriz]

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
        elif valor == "X":
            print("X", end=" ")    
    print()
    
# Crear la ventana
ventana = pygame.display.set_mode((500, 500))

# Cargar las imagenes
imagen_obstaculo = pygame.image.load("obstaculo.png")
imagen_agente = pygame.image.load("agente.png")
imagen_meta = pygame.image.load("meta.png")
imagen_camino = pygame.image.load("camino.png")

#Dibujar en pantalla

for i, fila in enumerate(matriz_caminos):
    for j, valor in enumerate(fila):
        x = j * 25
        y = i * 25
if valor == 1:
    ventana.blit(imagen_obstaculo, (x, y))
elif valor == 2:
    ventana.blit(imagen_agente, (x, y))
elif valor == 3:
    ventana.blit(imagen_agente, (x, y))
elif valor == 5:
    ventana.blit(imagen_meta, (x, y))
elif valor == 'X':
    ventana.blit(imagen_camino, (x, y))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   

            pygame.quit()
sys.exit()