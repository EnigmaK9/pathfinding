import sys
import pygame
from pathfinding import Dijkstra, A_star
from utils import print_path, mark_paths
from visualization import draw_matrices
from input_data import get_input_data
from results import show_results

# Initialize pygame
pygame.init()

# Initialize global variables for matrices and positions
matrix_fixed = []
matrix_random = []
A1_start_pos = []
A1_goal_pos = []
A2_start_pos = []
A2_goal_pos = []

# Variable to store the type of obstacles (fixed or random)
obstacle_type = None

def configure_matrices():
    '''
    Configure the matrices based on the user input. Initialize the matrices
    and get the input data from the user to set up the start and goal positions
    as well as the type of obstacles.
    '''
    global matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos, matrix_fixed_paths_star, matrix_random_paths_star, obstacle_type
    
    # Initialize the matrices with zeros (20x20 grid)
    matrix_fixed = [[0 for _ in range(20)] for _ in range(20)]
    matrix_random = [[0 for _ in range(20)] for _ in range(20)]
    
    # Get input data from the user
    obstacle_type = get_input_data(matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos)
    
    # Create copies of the matrices for A* algorithm paths
    matrix_fixed_paths_star = [row[:] for row in matrix_fixed]
    matrix_random_paths_star = [row[:] for row in matrix_random]

def execute_pathfinding():
    '''
    Execute the pathfinding algorithms (Dijkstra and A*) on the configured matrices.
    Mark the paths found by each algorithm on the matrices.
    '''
    global matrix_fixed_dijkstra, matrix_fixed_a_star, matrix_random_dijkstra, matrix_random_a_star
    
    # Perform Dijkstra's algorithm on the fixed obstacles matrix
    path_A1_fixed_dijkstra = Dijkstra(matrix_fixed, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_fixed_dijkstra = Dijkstra(matrix_fixed, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    # Create a copy of the matrix and mark the paths found by Dijkstra's algorithm
    matrix_fixed_dijkstra = [row[:] for row in matrix_fixed]
    mark_paths(matrix_fixed_dijkstra, path_A1_fixed_dijkstra, path_A2_fixed_dijkstra)

    # Perform A* algorithm on the fixed obstacles matrix
    path_A1_fixed_a_star = A_star(matrix_fixed_paths_star, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_fixed_a_star = A_star(matrix_fixed_paths_star, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    # Create a copy of the matrix and mark the paths found by A* algorithm
    matrix_fixed_a_star = [row[:] for row in matrix_fixed]
    mark_paths(matrix_fixed_a_star, path_A1_fixed_a_star, path_A2_fixed_a_star)

    # Perform Dijkstra's algorithm on the random obstacles matrix
    path_A1_random_dijkstra = Dijkstra(matrix_random, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_random_dijkstra = Dijkstra(matrix_random, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    # Create a copy of the matrix and mark the paths found by Dijkstra's algorithm
    matrix_random_dijkstra = [row[:] for row in matrix_random]
    mark_paths(matrix_random_dijkstra, path_A1_random_dijkstra, path_A2_random_dijkstra)

    # Perform A* algorithm on the random obstacles matrix
    path_A1_random_a_star = A_star(matrix_random_paths_star, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_random_a_star = A_star(matrix_random_paths_star, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    # Create a copy of the matrix and mark the paths found by A* algorithm
    matrix_random_a_star = [row[:] for row in matrix_random]
    mark_paths(matrix_random_a_star, path_A1_random_a_star, path_A2_random_a_star)

def display_results():
    '''
    Display the results of the pathfinding algorithms. Depending on the type of obstacles
    (fixed or random) selected by the user, display the corresponding matrices and paths.
    '''
    if obstacle_type == "fixed":
        # Print and draw the results for fixed obstacles
        print_path(matrix_fixed, "Fixed Obstacles")
        print_path(matrix_fixed_dijkstra, "Fixed Obstacles Dijkstra")
        print_path(matrix_fixed_a_star, "Fixed Obstacles A*")
        draw_matrices(matrix_fixed, matrix_fixed_dijkstra, matrix_fixed_a_star, A1_start_pos, A2_start_pos, A1_goal_pos, A2_goal_pos)
    else:
        # Print and draw the results for random obstacles
        print_path(matrix_random, "Random Obstacles")
        print_path(matrix_random_dijkstra, "Random Obstacles Dijkstra")
        print_path(matrix_random_a_star, "Random Obstacles A*")
        draw_matrices(matrix_random, matrix_random_dijkstra, matrix_random_a_star, A1_start_pos, A2_start_pos, A1_goal_pos, A2_goal_pos)
    
    # Show the results in a Tkinter window
    show_results()

# Main entry point of the program
if __name__ == "__main__":
    configure_matrices()  # Configure the matrices based on user input
    execute_pathfinding()  # Execute the pathfinding algorithms
    display_results()  # Display the results
