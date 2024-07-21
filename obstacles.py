import random

def create_random_obstacles(matrix, num_obstacles):
    '''
    This function adds random obstacles to the matrix.
    It places a specified number of obstacles (1s) at random locations within the matrix.
    
    Parameters:
    matrix (list of lists): The 20x20 grid where obstacles will be placed.
    num_obstacles (int): The number of obstacles to be placed randomly.
    '''
    for i in range(num_obstacles):
        row = random.randint(0, 19)  # Select a random row index between 0 and 19
        col = random.randint(0, 19)  # Select a random column index between 0 and 19
        matrix[row][col] = 1  # Place an obstacle (1) at the randomly selected position

def create_fixed_obstacles(matrix):
    '''
    This function adds fixed obstacles to the matrix.
    It places obstacles (1s) at predefined locations within the matrix.
    
    Parameters:
    matrix (list of lists): The 20x20 grid where obstacles will be placed.
    '''
    # List of predefined (fixed) obstacle positions (row, col)
    fixed_obstacles = [
        (4, 2), (4, 3), (3, 4), (4, 6), (5, 7), (6, 7), (7, 7), (5, 8), (6, 8),
        (7, 8), (8, 8), (9, 8), (10, 8), (5, 9), (9, 9), (10, 9), (11, 9), 
        (12, 9), (13, 9), (4, 10), (1, 11), (2, 11), (3, 11), (4, 11), 
        (5, 11), (0, 11), (7, 12), (8, 12), (7, 13), (8, 13)
    ]
    
    # Place obstacles (1s) at the predefined positions
    for row, col in fixed_obstacles:
        matrix[row][col] = 1
