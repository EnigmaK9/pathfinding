import pygame
import sys

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

def draw_all_matrices(matrix_fixed, matrix_random, matrix_fixed_dijkstra, matrix_fixed_a_star, matrix_random_dijkstra, matrix_random_a_star, A1_start_pos, A2_start_pos, A1_goal_pos, A2_goal_pos):
    pygame.init()  # Asegurarse de que pygame esté inicializado

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
    path_both_image = pygame.image.load("img/camino_both.png")
    floor_image = pygame.image.load("img/piso.png")

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
