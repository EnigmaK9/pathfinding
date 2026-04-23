def neighbors(matrix, current):
    x, y = current
    res = []
    # Up, Down, Left, Right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            res.append((nx, ny))
    return res

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_path(g_cost, start, goal, matrix):
    path = [goal]
    current = goal
    while current != start:
        best_neighbor = None
        min_cost = float('inf')
        for n in neighbors(matrix, current):
            if n in g_cost and g_cost[n] < min_cost:
                min_cost = g_cost[n]
                best_neighbor = n
        if best_neighbor is None: break
        current = best_neighbor
        path.append(current)
    return path[::-1]
