import heapq
from utils import neighbors, manhattan, get_path

def Dijkstra(matrix, start, goal):
    '''
    Implements Dijkstra's algorithm to find the shortest path in a grid.
    
    Parameters:
    matrix (list of lists): The 20x20 grid where the pathfinding takes place.
    start (tuple): The starting position (row, col) in the grid.
    goal (tuple): The goal position (row, col) in the grid.
    
    Returns:
    list: The shortest path from start to goal as a list of tuples.
    '''
    queue = []
    heapq.heappush(queue, (0, start))  # Initialize the priority queue with the start position
    visited = {}  # Dictionary to keep track of visited nodes and their distances
    visited[start] = 0
    path = {}  # Dictionary to store the path to each node
    path[start] = [start]
    
    while queue:
        current = heapq.heappop(queue)[1]  # Get the node with the smallest distance
        for neighbor in neighbors(matrix, current):
            if neighbor not in visited:
                if matrix[neighbor[0]][neighbor[1]] == 1:  # Skip obstacles
                    continue
                distance = visited[current] + 1
                if neighbor not in visited or distance < visited[neighbor]:
                    visited[neighbor] = distance
                    path[neighbor] = path[current] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))
        if current == goal:
            return path[current]  # Return the path once the goal is reached
    return None

def A_star(matrix, start, goal):
    '''
    Implements the A* algorithm to find the shortest path in a grid using a heuristic.
    
    Parameters:
    matrix (list of lists): The 20x20 grid where the pathfinding takes place.
    start (tuple): The starting position (row, col) in the grid.
    goal (tuple): The goal position (row, col) in the grid.
    
    Returns:
    list: The shortest path from start to goal as a list of tuples.
    '''
    open_list = []
    closed_list = []
    heapq.heappush(open_list, (0, 0, start))  # Initialize the priority queue with the start position
    g_cost = {start: 0}  # Dictionary to keep track of the cost from start to each node
    f_cost = {start: manhattan(start, goal)}  # Dictionary to keep track of the total cost (g + h)
    
    while open_list:
        f, g, current = heapq.heappop(open_list)  # Get the node with the smallest f value
        closed_list.append(current)
        if current == goal:
            return get_path(matrix, current, g_cost, start)  # Return the path once the goal is reached
        
        for neighbor in neighbors(matrix, current):
            if neighbor in closed_list or matrix[neighbor[0]][neighbor[1]] == 1:  # Skip obstacles and closed nodes
                continue
            temp_g = g + 1
            if neighbor not in [i[2] for i in open_list] or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f = temp_g + manhattan(neighbor, goal)
                heapq.heappush(open_list, (f, temp_g, neighbor))
    
    return None
