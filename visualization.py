import pygame
import sys
import time
import os

CELL_SIZE = 25
GRID_SIZE = 20
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

COLORS = {
    0: (255, 255, 255),       # Floor
    1: (50, 50, 50),          # Obstacle
    'x': (255, 100, 100),     # Path A1 (light red tiles)
    'y': (100, 100, 255),     # Path A2 (light blue tiles)
    'line_1': (200, 0, 0),    # Shortest path trace 1 (Dark Red)
    'line_2': (0, 0, 200),    # Shortest path trace 2 (Dark Blue)
    'p1_s': (0, 255, 0),      # Agent 1 Start
    'p1_g': (255, 255, 0),    # Agent 1 Goal
    'p2_s': (0, 150, 0),      # Agent 2 Start
    'p2_g': (200, 200, 0)     # Agent 2 Goal
}

def init_music():
    """Initializes a high-fidelity audio environment and plays BGM."""
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        music_file = "bbokari_theme.flac" # Replace with your audio file name
        if os.path.exists(music_file):
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(-1) # Loop indefinitely
    except Exception:
        pass # Silently fail if audio device or file is unavailable

def interactive_placement(matrix):
    """Opens a Pygame window to let the user click and place agents on the grid."""
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT + 50))
    pygame.display.set_caption("Interactive Agent Placement")
    font = pygame.font.SysFont("Arial", 16, bold=True)

    placements = []
    prompts = [
        ("Click to place Agent 1 Start (Green)", COLORS['p1_s']),
        ("Click to place Agent 1 Goal (Yellow)", COLORS['p1_g']),
        ("Click to place Agent 2 Start (Dark Green)", COLORS['p2_s']),
        ("Click to place Agent 2 Goal (Dark Yellow)", COLORS['p2_g'])
    ]

    running = True
    while running and len(placements) < 4:
        window.fill((30, 30, 30))
        
        # Draw the Grid
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                color = COLORS[1] if matrix[r][c] == 1 else COLORS[0]
                pygame.draw.rect(window, color, (c*CELL_SIZE, r*CELL_SIZE + 50, CELL_SIZE-1, CELL_SIZE-1))
        
        # Draw already placed points
        for i, p in enumerate(placements):
            pygame.draw.circle(window, prompts[i][1], (p[1]*CELL_SIZE + 12, p[0]*CELL_SIZE + 50 + 12), 10)

        # Draw current instructions
        txt = font.render(prompts[len(placements)][0], True, prompts[len(placements)][1])
        window.blit(txt, (10, 15))
        pygame.display.flip()

        # Handle mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                my -= 50 # Adjust for the top instruction bar
                
                if my >= 0:
                    r, c = my // CELL_SIZE, mx // CELL_SIZE
                    if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                        if matrix[r][c] != 1 and (r, c) not in placements:
                            placements.append((r, c))

    pygame.display.quit()
    return placements[0], placements[1], placements[2], placements[3]

def draw_shortest_path_line(window, path, x_off, y_off, color):
    """Overlays a solid line tracking the exact shortest path."""
    if len(path) > 1:
        points = [(c*CELL_SIZE + x_off + 12, r*CELL_SIZE + y_off + 12) for r, c in path]
        pygame.draw.lines(window, color, False, points, 3)

def draw_matrices(matrix_dijkstra, matrix_astar, p1_s, p2_s, p1_g, p2_g, path_d1, path_d2, path_a1, path_a2):
    pygame.init()
    init_music()
    
    window_width = WIDTH * 2 + 50
    window_height = HEIGHT + 150
    window = pygame.display.set_mode((window_width, window_height))
    
    pygame.display.set_caption("Dijkstra vs A*")
    font = pygame.font.SysFont("Arial", 18, bold=True)
    info_font = pygame.font.SysFont("Arial", 18)

    def draw_grid(m, x_off, y_off, title):
        txt = font.render(title, True, (255, 255, 255))
        window.blit(txt, (x_off + WIDTH//2 - 40, y_off - 30))
        
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                val = m[r][c]
                color = COLORS.get(val, COLORS[0])
                pygame.draw.rect(window, color, (c*CELL_SIZE + x_off, r*CELL_SIZE + y_off, CELL_SIZE-1, CELL_SIZE-1))
        
        for p, color in [(p1_s, COLORS['p1_s']), (p2_s, COLORS['p2_s']), (p1_g, COLORS['p1_g']), (p2_g, COLORS['p2_g'])]:
            pygame.draw.circle(window, color, (p[1]*CELL_SIZE + x_off + 12, p[0]*CELL_SIZE + y_off + 12), 8)

    def draw_instructions(color):
        instr_txt = info_font.render("Press 'R' for a new test | 'ESC' to close", True, color)
        window.blit(instr_txt, (window_width // 2 - instr_txt.get_width() // 2, HEIGHT + 80))

    d_copy = [row[:] for row in matrix_dijkstra]
    a_copy = [row[:] for row in matrix_astar]
    max_len = max(len(path_d1), len(path_d2), len(path_a1), len(path_a2))
    
    # Animation Block
    for i in range(max_len):
        if i < len(path_d1): d_copy[path_d1[i][0]][path_d1[i][1]] = 'x'
        if i < len(path_d2): d_copy[path_d2[i][0]][path_d2[i][1]] = 'y'
        if i < len(path_a1): a_copy[path_a1[i][0]][path_a1[i][1]] = 'x'
        if i < len(path_a2): a_copy[path_a2[i][0]][path_a2[i][1]] = 'y'
        
        window.fill((30, 30, 30))
        draw_grid(d_copy, 20, 50, "DIJKSTRA")
        draw_grid(a_copy, WIDTH + 30, 50, "A*")
        draw_instructions((150, 150, 150))
        
        pygame.display.flip()
        time.sleep(0.05)

    # Highlight Final Path Phase
    window.fill((30, 30, 30))
    draw_grid(d_copy, 20, 50, "DIJKSTRA")
    draw_grid(a_copy, WIDTH + 30, 50, "A*")
    
    # Overlay the shortest path lines explicitly
    draw_shortest_path_line(window, path_d1, 20, 50, COLORS['line_1'])
    draw_shortest_path_line(window, path_d2, 20, 50, COLORS['line_2'])
    draw_shortest_path_line(window, path_a1, WIDTH + 30, 50, COLORS['line_1'])
    draw_shortest_path_line(window, path_a2, WIDTH + 30, 50, COLORS['line_2'])

    draw_instructions((255, 255, 0))
    pygame.display.flip()

    # Event Loop Rest/Wait
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                return False 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.quit()
                    pygame.quit()
                    return False 
                elif event.key == pygame.K_r:
                    pygame.mixer.quit()
                    pygame.quit()
                    return True