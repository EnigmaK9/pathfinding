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

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_path(matrix, current, g_cost, start):
    path = [current]
    while current != start:
        for neighbor in neighbors(matrix, current):
            if g_cost.get(neighbor, float('inf')) <= g_cost.get(current, float('inf')):
                current = neighbor
                path.append(current)
    return path[::-1]

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

def mark_paths(matrix, path_A1, path_A2):
    if path_A1:
        for x, y in path_A1:
            if matrix[x][y] == 'y':
                matrix[x][y] = 'xy'
            else:
                matrix[x][y] = 'x'
    if path_A2:
        for x, y in path_A2:
            if matrix[x][y] == 'x':
                matrix[x][y] = 'xy'
            else:
                matrix[x][y] = 'y'
