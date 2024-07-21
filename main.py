import sys
import heapq
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# Initialize pygame
pygame.init()

# Global variables to store input data
matrix_fixed = []
matrix_random = []
A1_start_pos = ()
A1_goal_pos = ()
A2_start_pos = ()
A2_goal_pos = ()

# Necessary functions and classes

def create_random_obstacles(matrix, num_obstacles):
    for i in range(num_obstacles):
        row = random.randint(0, 19)
        col = random.randint(0, 19)
        matrix[row][col] = 1

def create_fixed_obstacles(matrix):
    matrix[4][2] = 1
    matrix[4][3] = 1
    matrix[3][4] = 1
    matrix[4][6] = 1
    matrix[5][7] = 1
    matrix[6][7] = 1
    matrix[7][7] = 1
    matrix[5][8] = 1
    matrix[6][8] = 1
    matrix[7][8] = 1
    matrix[8][8] = 1
    matrix[9][8] = 1
    matrix[10][8] = 1
    matrix[5][9] = 1
    matrix[9][9] = 1
    matrix[10][9] = 1
    matrix[11][9] = 1
    matrix[12][9] = 1
    matrix[13][9] = 1
    matrix[4][10] = 1
    matrix[1][11] = 1
    matrix[2][11] = 1
    matrix[3][11] = 1
    matrix[4][11] = 1
    matrix[5][11] = 1
    matrix[0][11] = 1
    matrix[7][12] = 1
    matrix[8][12] = 1
    matrix[7][13] = 1
    matrix[8][13] = 1

def print_path(matrix, label):
    print(f"===========================================")
    print(f"{label}")
    print(f"===========================================")
    for row in matrix:
        for value in row:
            if value == 0:
                print(".", end=" ")
            elif value == 1:
                print("#", end=" ")
            elif value == 2:
                print("A1", end=" ")
            elif value == 3:
                print("A2", end=" ")
            elif value == 5:
                print("G1", end=" ")
            elif value == 6:
                print("G2", end=" ")
            elif value == "x":
                print("x", end=" ")
            elif value == "y":
                print("y", end=" ")
            elif value == "xy":
                print("xy", end=" ")
        print()
    print("===========================================")

def neighbors(matrix, current):
    x, y = current
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if x < len(matrix) - 1:
        neighbors.append((x + 1, y))
    if y < len(matrix[0]) - 1:
        neighbors.append((x, y + 1))
    return neighbors

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

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

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

def get_path(matrix, current, g_cost, start):
    path = [current]
    while current != start:
        for neighbor in neighbors(matrix, current):
            if g_cost.get(neighbor, float('inf')) <= g_cost.get(current, float('inf')):
                current = neighbor
                path.append(current)
    return path[::-1]

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

def draw_all_matrices():
    WINDOW_WIDTH = WIDTH * 3 + 40
    WINDOW_HEIGHT = HEIGHT * 2 + 30
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Comparison - Fixed and Random Obstacles with Dijkstra and A*")
    
    obstacle_image = pygame.image.load("img/obstaculo.png")
    agent_image = pygame.image.load("img/agente.png")
    agent2_image = pygame.image.load("img/agente2.png")
    goal1_image = pygame.image.load("img/meta.png")
    goal2_image = pygame.image.load("img/meta.png")
    path_image = pygame.image.load("img/camino.png")
    path2_image = pygame.image.load("img/camino2.png")
    floor_image = pygame.image.load("img/piso.png")
    path_both_image = pygame.image.load("img/camino_both.png")

    drawing = {
        1: obstacle_image,
        2: agent_image,
        3: agent2_image,
        5: goal1_image,
        6: goal2_image,
        'x': path_image,
        'y': path2_image,
        'xy': path_both_image,
        0: floor_image
    }

    matrices = [
        (matrix_fixed, "Fixed Obstacles", (5, 5)),
        (matrix_random, "Random Obstacles", (WIDTH + 15, 5)),
        (matrix_fixed_dijkstra, "Fixed Obstacles Dijkstra", (WIDTH * 2 + 25, 5)),
        (matrix_fixed_a_star, "Fixed Obstacles A*", (5, HEIGHT + 15)),
        (matrix_random_dijkstra, "Random Obstacles Dijkstra", (WIDTH + 15, HEIGHT + 15)),
        (matrix_random_a_star, "Random Obstacles A*", (WIDTH * 2 + 25, HEIGHT + 15))
    ]

    for matrix, title, pos in matrices:
        x_offset, y_offset = pos
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                x = j * CELL_SIZE + x_offset
                y = i * CELL_SIZE + y_offset
                window.blit(drawing[value], (x, y))

        font = pygame.font.SysFont(None, 24)
        label_surface = font.render(title, True, (0, 0, 0))  # Black color for text
        window.blit(label_surface, (x_offset + 5, y_offset + 5))

        # Draw agents and goals on top
        window.blit(agent_image, (A1_start_pos[1] * CELL_SIZE + x_offset, A1_start_pos[0] * CELL_SIZE + y_offset))
        window.blit(agent2_image, (A2_start_pos[1] * CELL_SIZE + x_offset, A2_start_pos[0] * CELL_SIZE + y_offset))
        window.blit(goal1_image, (A1_goal_pos[1] * CELL_SIZE + x_offset, A1_goal_pos[0] * CELL_SIZE + y_offset))
        window.blit(goal2_image, (A2_goal_pos[1] * CELL_SIZE + x_offset, A2_goal_pos[0] * CELL_SIZE + y_offset))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

def get_input_data():
    def on_submit():
        global matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos
        matrix_fixed = [[0 for _ in range(20)] for _ in range(20)]
        matrix_random = [[0 for _ in range(20)] for _ in range(20)]
        if obstacles_var.get() == 1:
            create_fixed_obstacles(matrix_fixed)
            create_fixed_obstacles(matrix_random)
        else:
            create_random_obstacles(matrix_fixed, int(num_obstacles_entry.get()))
            create_random_obstacles(matrix_random, int(num_obstacles_entry.get()))

        A1_start_pos = tuple(map(int, A1_start_entry.get().split(',')))
        A1_goal_pos = tuple(map(int, A1_goal_entry.get().split(',')))
        A2_start_pos = tuple(map(int, A2_start_entry.get().split(',')))
        A2_goal_pos = tuple(map(int, A2_goal_entry.get().split(',')))

        matrix_fixed[A1_start_pos[0]][A1_start_pos[1]] = 2
        matrix_fixed[A2_start_pos[0]][A2_start_pos[1]] = 3
        matrix_fixed[A1_goal_pos[0]][A1_goal_pos[1]] = 5
        matrix_fixed[A2_goal_pos[0]][A2_goal_pos[1]] = 6

        matrix_random[A1_start_pos[0]][A1_start_pos[1]] = 2
        matrix_random[A2_start_pos[0]][A2_start_pos[1]] = 3
        matrix_random[A1_goal_pos[0]][A1_goal_pos[1]] = 5
        matrix_random[A2_goal_pos[0]][A2_goal_pos[1]] = 6

        window.destroy()

    window = tk.Tk()
    window.title("Input Configuration")

    tk.Label(window, text="A1 Start Position (row,col):").grid(row=0, column=0)
    A1_start_entry = tk.Entry(window)
    A1_start_entry.grid(row=0, column=1)
    A1_start_entry.insert(0, "10,10")

    tk.Label(window, text="A1 Goal Position (row,col):").grid(row=1, column=0)
    A1_goal_entry = tk.Entry(window)
    A1_goal_entry.grid(row=1, column=1)
    A1_goal_entry.insert(0, "0,0")

    tk.Label(window, text="A2 Start Position (row,col):").grid(row=2, column=0)
    A2_start_entry = tk.Entry(window)
    A2_start_entry.grid(row=2, column=1)
    A2_start_entry.insert(0, "12,12")

    tk.Label(window, text="A2 Goal Position (row,col):").grid(row=3, column=0)
    A2_goal_entry = tk.Entry(window)
    A2_goal_entry.grid(row=3, column=1)
    A2_goal_entry.insert(0, "14,19")

    obstacles_var = tk.IntVar(value=1)
    tk.Radiobutton(window, text="Fixed Obstacles", variable=obstacles_var, value=1).grid(row=4, column=0)
    tk.Radiobutton(window, text="Random Obstacles", variable=obstacles_var, value=2).grid(row=4, column=1)

    tk.Label(window, text="Number of Random Obstacles:").grid(row=5, column=0)
    num_obstacles_entry = tk.Entry(window)
    num_obstacles_entry.grid(row=5, column=1)
    num_obstacles_entry.insert(0, "50")

    tk.Button(window, text="Submit", command=on_submit).grid(row=6, column=0, columnspan=2)

    window.mainloop()

def show_results():
    results = tk.Tk()
    results.title("Pathfinding Results")

    text = tk.Text(results)
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A1 Path Length: {len(path_A1_fixed_dijkstra) if path_A1_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A2 Path Length: {len(path_A2_fixed_dijkstra) if path_A2_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A1 Path Length: {len(path_A1_fixed_a_star) if path_A1_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A2 Path Length: {len(path_A2_fixed_a_star) if path_A2_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A1 Path Length: {len(path_A1_random_dijkstra) if path_A1_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A2 Path Length: {len(path_A2_random_dijkstra) if path_A2_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A1 Path Length: {len(path_A1_random_a_star) if path_A1_random_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A2 Path Length: {len(path_A2_random_a_star) if path_A2_random_a_star else 'No Path'}\n")

    text.pack()
    results.mainloop()

# Create a 20x20 matrix with value 0
matrix_fixed = []
matrix_random = []
A1_start_pos = ()
A1_goal_pos = ()
A2_start_pos = ()
A2_goal_pos = ()

get_input_data()

print_path(matrix_fixed, "Fixed Obstacles")
print_path(matrix_random, "Random Obstacles")

# Copies of the original matrices to use with A*
matrix_fixed_paths_star = [row[:] for row in matrix_fixed]
matrix_random_paths_star = [row[:] for row in matrix_random]

# Dijkstra for fixed obstacles
path_A1_fixed_dijkstra = Dijkstra(matrix_fixed, A1_start_pos, A1_goal_pos)
print("===========================================")
if path_A1_fixed_dijkstra:
    print("Dijkstra. A1 Distance: ", len(path_A1_fixed_dijkstra), "units")
    print("===========================================")
    print("A1 Path: ", path_A1_fixed_dijkstra)
else:
    print("Dijkstra. A1 Path not found")
path_A2_fixed_dijkstra = Dijkstra(matrix_fixed, A2_start_pos, A2_goal_pos)
print("===========================================")
if path_A2_fixed_dijkstra:
    print("Dijkstra. A2 Distance: ", len(path_A2_fixed_dijkstra), "units")
    print("===========================================")
    print("A2 Path: ", path_A2_fixed_dijkstra)
else:
    print("Dijkstra. A2 Path not found")
print("===========================================")

matrix_fixed_dijkstra = [row[:] for row in matrix_fixed]
if path_A1_fixed_dijkstra:
    for x, y in path_A1_fixed_dijkstra:
        if matrix_fixed_dijkstra[x][y] == 'y':
            matrix_fixed_dijkstra[x][y] = 'xy'
        else:
            matrix_fixed_dijkstra[x][y] = 'x'
if path_A2_fixed_dijkstra:
    for x, y in path_A2_fixed_dijkstra:
        if matrix_fixed_dijkstra[x][y] == 'x':
            matrix_fixed_dijkstra[x][y] = 'xy'
        else:
            matrix_fixed_dijkstra[x][y] = 'y'

# A* for fixed obstacles
path_A1_fixed_a_star = A_star(matrix_fixed_paths_star, A1_start_pos, A1_goal_pos)
print("===========================================")
if path_A1_fixed_a_star:
    print("A*. A1 Distance: ", len(path_A1_fixed_a_star), "units")
    print("===========================================")
    print("A1 Path: ", path_A1_fixed_a_star)
else:
    print("A*. A1 Path not found")
path_A2_fixed_a_star = A_star(matrix_fixed_paths_star, A2_start_pos, A2_goal_pos)
print("===========================================")
if path_A2_fixed_a_star:
    print("A*. A2 Distance: ", len(path_A2_fixed_a_star), "units")
    print("===========================================")
    print("A2 Path: ", path_A2_fixed_a_star)
else:
    print("A*. A2 Path not found")
print("===========================================")

matrix_fixed_a_star = [row[:] for row in matrix_fixed]
if path_A1_fixed_a_star:
    for x, y in path_A1_fixed_a_star:
        if matrix_fixed_a_star[x][y] == 'y':
            matrix_fixed_a_star[x][y] = 'xy'
        else:
            matrix_fixed_a_star[x][y] = 'x'
if path_A2_fixed_a_star:
    for x, y in path_A2_fixed_a_star:
        if matrix_fixed_a_star[x][y] == 'x':
            matrix_fixed_a_star[x][y] = 'xy'
        else:
            matrix_fixed_a_star[x][y] = 'y'

# Dijkstra for random obstacles
path_A1_random_dijkstra = Dijkstra(matrix_random, A1_start_pos, A1_goal_pos)
print("===========================================")
if path_A1_random_dijkstra:
    print("Dijkstra. A1 Distance: ", len(path_A1_random_dijkstra), "units")
    print("===========================================")
    print("A1 Path: ", path_A1_random_dijkstra)
else:
    print("Dijkstra. A1 Path not found")
path_A2_random_dijkstra = Dijkstra(matrix_random, A2_start_pos, A2_goal_pos)
print("===========================================")
if path_A2_random_dijkstra:
    print("Dijkstra. A2 Distance: ", len(path_A2_random_dijkstra), "units")
    print("===========================================")
    print("A2 Path: ", path_A2_random_dijkstra)
else:
    print("Dijkstra. A2 Path not found")
print("===========================================")

matrix_random_dijkstra = [row[:] for row in matrix_random]
if path_A1_random_dijkstra:
    for x, y in path_A1_random_dijkstra:
        if matrix_random_dijkstra[x][y] == 'y':
            matrix_random_dijkstra[x][y] = 'xy'
        else:
            matrix_random_dijkstra[x][y] = 'x'
if path_A2_random_dijkstra:
    for x, y in path_A2_random_dijkstra:
        if matrix_random_dijkstra[x][y] == 'x':
            matrix_random_dijkstra[x][y] = 'xy'
        else:
            matrix_random_dijkstra[x][y] = 'y'

# A* for random obstacles
path_A1_random_a_star = A_star(matrix_random_paths_star, A1_start_pos, A1_goal_pos)
print("===========================================")
if path_A1_random_a_star:
    print("A*. A1 Distance: ", len(path_A1_random_a_star), "units")
    print("===========================================")
    print("A1 Path: ", path_A1_random_a_star)
else:
    print("A*. A1 Path not found")
path_A2_random_a_star = A_star(matrix_random_paths_star, A2_start_pos, A2_goal_pos)
print("===========================================")
if path_A2_random_a_star:
    print("A*. A2 Distance: ", len(path_A2_random_a_star), "units")
    print("===========================================")
    print("A2 Path: ", path_A2_random_a_star)
else:
    print("A*. A2 Path not found")
print("===========================================")

matrix_random_a_star = [row[:] for row in matrix_random]
if path_A1_random_a_star:
    for x, y in path_A1_random_a_star:
        if matrix_random_a_star[x][y] == 'y':
            matrix_random_a_star[x][y] = 'xy'
        else:
            matrix_random_a_star[x][y] = 'x'
if path_A2_random_a_star:
    for x, y in path_A2_random_a_star:
        if matrix_random_a_star[x][y] == 'x':
            matrix_random_a_star[x][y] = 'xy'
        else:
            matrix_random_a_star[x][y] = 'y'

# Print paths in terminal
print_path(matrix_fixed, "Fixed Obstacles")
print_path(matrix_random, "Random Obstacles")
print_path(matrix_fixed_dijkstra, "Fixed Obstacles Dijkstra")
print_path(matrix_fixed_a_star, "Fixed Obstacles A*")
print_path(matrix_random_dijkstra, "Random Obstacles Dijkstra")
print_path(matrix_random_a_star, "Random Obstacles A*")

# Display matrices in a single Pygame window
draw_all_matrices()

# Show results in an additional window
show_results()
