import heapq
from utils import neighbors, manhattan, get_path

def Dijkstra(matrix, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    visited = {}
    visited[start] = 0
    path = {}
    path[start] = [start]
    while queue:
        current = heapq.heappop(queue)[1]
        for neighbor in neighbors(matrix, current):
            if neighbor not in visited:
                if matrix[neighbor[0]][neighbor[1]] == 1:
                    continue
                distance = visited[current] + 1
                if neighbor not in visited or distance < visited[neighbor]:
                    visited[neighbor] = distance
                    path[neighbor] = path[current] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))
        if current == goal:
            return path[current]
    return None

def A_star(matrix, start, goal):
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (0, 0, start))
    g_cost = {start: 0}
    f_cost = {start: manhattan(start, goal)}
    while open_list:
        f, g, current = heapq.heappop(open_list)
        closed_list.append(current)
        if current == goal:
            return get_path(matrix, current, g_cost, start)
        for neighbor in neighbors(matrix, current):
            if neighbor in closed_list or matrix[neighbor[0]][neighbor[1]] == 1:
                continue
            temp_g = g + 1
            if neighbor not in [i[2] for i in open_list] or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f = temp_g + manhattan(neighbor, goal)
                heapq.heappush(open_list, (f, temp_g, neighbor))
    return None
