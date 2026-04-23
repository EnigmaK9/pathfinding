import heapq
from utils import neighbors, manhattan, get_path

def Dijkstra(matrix, start, goal):
    queue = [(0, start)]
    g_cost = {start: 0}
    
    while queue:
        dist, current = heapq.heappop(queue)
        if current == goal:
            return get_path(g_cost, start, goal, matrix)
        
        for n in neighbors(matrix, current):
            if matrix[n[0]][n[1]] == 1: continue
            new_cost = g_cost[current] + 1
            if n not in g_cost or new_cost < g_cost[n]:
                g_cost[n] = new_cost
                heapq.heappush(queue, (new_cost, n))
    return []

def A_star(matrix, start, goal):
    open_list = [(manhattan(start, goal), 0, start)]
    g_cost = {start: 0}
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal:
            return get_path(g_cost, start, goal, matrix)
        
        for n in neighbors(matrix, current):
            if matrix[n[0]][n[1]] == 1: continue
            new_g = g + 1
            if n not in g_cost or new_g < g_cost[n]:
                g_cost[n] = new_g
                f_score = new_g + manhattan(n, goal)
                heapq.heappush(open_list, (f_score, new_g, n))
    return []
