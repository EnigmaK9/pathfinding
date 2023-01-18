import heapq

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
        vecinos.apFpend((x, y + 1))
    return vecinos



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
