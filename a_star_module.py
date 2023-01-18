
from vecinos import vecinos

matriz = None
inicio = None

def manhattan(pos1, pos2):
    # calculamos la distancia manhattan entre dos puntos
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) 

def A_star(matriz, inicio, destino):
    # creamos una cola de prioridad para almacenar los nodos a explorar
    abierta = []
    cerrada = []
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




"""
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

"""