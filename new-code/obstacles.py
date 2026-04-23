import random

def create_random_obstacles(matrix, num_obstacles, reserved_positions):
    count = 0
    while count < num_obstacles:
        r, c = random.randint(0, 19), random.randint(0, 19)
        if matrix[r][c] == 0 and (r, c) not in reserved_positions:
            matrix[r][c] = 1
            count += 1

def create_fixed_obstacles(matrix):
    fixed = [
        (4, 2), (4, 3), (3, 4), (4, 6), (5, 7), (6, 7), (7, 7), (5, 8), (6, 8),
        (7, 8), (8, 8), (9, 8), (10, 8), (5, 9), (9, 9), (10, 9), (11, 9), 
        (12, 9), (13, 9), (4, 10), (1, 11), (2, 11), (3, 11), (4, 11), 
        (5, 11), (0, 11), (7, 12), (8, 12), (7, 13), (8, 13)
    ]
    for r, c in fixed:
        if 0 <= r < 20 and 0 <= c < 20:
            matrix[r][c] = 1
