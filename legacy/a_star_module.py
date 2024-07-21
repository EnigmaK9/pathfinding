import heapq
from python.vecinos import vecinos

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
            return path(matriz,current, g_cost, inicio)
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

def path(matriz, current, g_cost, inicio):
    # creamos una lista para almacenar el camino encontrado
    camino = [current]
    # mientras el nodo actual no sea el inicio
    while current != inicio:
        # iteramos sobre los vecinos del nodo actual
        for neighbor in vecinos(matriz, current):
            # si el vecino tiene un costo g menor
            if g_cost.get(neighbor, float('inf')) <= g_cost.get(current, float('inf')):
                current = neighbor
                # agregamos el vecino al camino
                camino.append(current)
    # retornamos el camino encontrado
    return camino[::-1]



