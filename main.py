import sys
import pygame
from pathfinding import Dijkstra, A_star
from utils import print_path, mark_paths
from visualization import draw_matrices
from input_data import get_input_data
from results import show_results

pygame.init()  # Initialize pygame

matrix_fixed = []
matrix_random = []
A1_start_pos = []
A1_goal_pos = []
A2_start_pos = []
A2_goal_pos = []

obstacle_type = None

path_lengths = []  # List to store path lengths

def configure_matrices():
    global matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos, matrix_fixed_paths_star, matrix_random_paths_star, obstacle_type
    matrix_fixed = [[0 for _ in range(20)] for _ in range(20)]
    matrix_random = [[0 for _ in range(20)] for _ in range(20)]
    obstacle_type = get_input_data(matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos)
    matrix_fixed_paths_star = [row[:] for row in matrix_fixed]
    matrix_random_paths_star = [row[:] for row in matrix_random]

def execute_pathfinding():
    global matrix_fixed_dijkstra, matrix_fixed_a_star, matrix_random_dijkstra, matrix_random_a_star
    
    path_A1_fixed_dijkstra = Dijkstra(matrix_fixed, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_fixed_dijkstra = Dijkstra(matrix_fixed, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    matrix_fixed_dijkstra = [row[:] for row in matrix_fixed]
    mark_paths(matrix_fixed_dijkstra, path_A1_fixed_dijkstra, path_A2_fixed_dijkstra)
    path_lengths.append(len(path_A1_fixed_dijkstra) if path_A1_fixed_dijkstra else 0)
    path_lengths.append(len(path_A2_fixed_dijkstra) if path_A2_fixed_dijkstra else 0)

    path_A1_fixed_a_star = A_star(matrix_fixed_paths_star, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_fixed_a_star = A_star(matrix_fixed_paths_star, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    matrix_fixed_a_star = [row[:] for row in matrix_fixed]
    mark_paths(matrix_fixed_a_star, path_A1_fixed_a_star, path_A2_fixed_a_star)
    path_lengths.append(len(path_A1_fixed_a_star) if path_A1_fixed_a_star else 0)
    path_lengths.append(len(path_A2_fixed_a_star) if path_A2_fixed_a_star else 0)

    path_A1_random_dijkstra = Dijkstra(matrix_random, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_random_dijkstra = Dijkstra(matrix_random, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    matrix_random_dijkstra = [row[:] for row in matrix_random]
    mark_paths(matrix_random_dijkstra, path_A1_random_dijkstra, path_A2_random_dijkstra)
    path_lengths.append(len(path_A1_random_dijkstra) if path_A1_random_dijkstra else 0)
    path_lengths.append(len(path_A2_random_dijkstra) if path_A2_random_dijkstra else 0)

    path_A1_random_a_star = A_star(matrix_random_paths_star, tuple(A1_start_pos), tuple(A1_goal_pos))
    path_A2_random_a_star = A_star(matrix_random_paths_star, tuple(A2_start_pos), tuple(A2_goal_pos))
    
    matrix_random_a_star = [row[:] for row in matrix_random]
    mark_paths(matrix_random_a_star, path_A1_random_a_star, path_A2_random_a_star)
    path_lengths.append(len(path_A1_random_a_star) if path_A1_random_a_star else 0)
    path_lengths.append(len(path_A2_random_a_star) if path_A2_random_a_star else 0)

def display_results():
    if obstacle_type == "fixed":
        print_path(matrix_fixed, "Fixed Obstacles")
        print_path(matrix_fixed_dijkstra, "Fixed Obstacles Dijkstra")
        print_path(matrix_fixed_a_star, "Fixed Obstacles A*")
        draw_matrices(matrix_fixed, matrix_fixed_dijkstra, matrix_fixed_a_star, A1_start_pos, A2_start_pos, A1_goal_pos, A2_goal_pos, path_lengths[:4])
    else:
        print_path(matrix_random, "Random Obstacles")
        print_path(matrix_random_dijkstra, "Random Obstacles Dijkstra")
        print_path(matrix_random_a_star, "Random Obstacles A*")
        draw_matrices(matrix_random, matrix_random_dijkstra, matrix_random_a_star, A1_start_pos, A2_start_pos, A1_goal_pos, A2_goal_pos, path_lengths[4:])
    
    show_results(path_lengths)

if __name__ == "__main__":
    configure_matrices()
    execute_pathfinding()
    display_results()
