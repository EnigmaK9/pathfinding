import pygame
import sys
import time
import os

CELL_SIZE = 25
GRID_SIZE = 20
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

# Premium iOS-inspired sleek dark/light color palette
COLORS = {
    0: (245, 245, 247),       # Premium Floor (soft off-white)
    1: (44, 44, 46),          # Premium Obstacle (dark charcoal)
    'v1': (254, 226, 226),     # Explored by Agent 1 (soft pastel pink)
    'v2': (219, 234, 254),     # Explored by Agent 2 (soft pastel blue)
    'v_both': (243, 232, 255), # Explored by both (soft pastel lavender)
    'line_1': (220, 38, 38),   # Shortest Path 1 (vibrant cherry red)
    'line_2': (37, 99, 235),   # Shortest Path 2 (vibrant royal blue)
    'p1_s': (34, 197, 94),     # Agent 1 Start (emerald green)
    'p1_g': (239, 68, 68),     # Agent 1 Goal (coral red)
    'p2_s': (22, 163, 74),     # Agent 2 Start (dark green)
    'p2_g': (59, 130, 246)     # Agent 2 Goal (ocean blue)
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
        ("Click to place Agent 1 Start (Emerald Green)", COLORS['p1_s']),
        ("Click to place Agent 1 Goal (Coral Red)", COLORS['p1_g']),
        ("Click to place Agent 2 Start (Dark Green)", COLORS['p2_s']),
        ("Click to place Agent 2 Goal (Ocean Blue)", COLORS['p2_g'])
    ]

    running = True
    while running and len(placements) < 4:
        window.fill((30, 30, 32))
        
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
        pygame.draw.lines(window, color, False, points, 4)

def draw_matrices(matrix_dijkstra, matrix_astar, p1_s, p2_s, p1_g, p2_g, path_d1, path_d2, path_a1, path_a2, visited_d1, visited_d2, visited_a1, visited_a2):
    pygame.init()
    init_music()
    
    window_width = WIDTH * 2 + 50
    window_height = HEIGHT + 160
    window = pygame.display.set_mode((window_width, window_height))
    
    pygame.display.set_caption("Pathfinding Algorithm Comparison: Dijkstra vs A*")
    font = pygame.font.SysFont("Arial", 16, bold=True)
    info_font = pygame.font.SysFont("Arial", 14)
    stat_title_font = pygame.font.SysFont("Arial", 14, bold=True)

    def draw_grid(m, x_off, y_off, title):
        txt = font.render(title, True, (255, 255, 255))
        window.blit(txt, (x_off + WIDTH//2 - 40, y_off - 30))
        
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                val = m[r][c]
                color = COLORS.get(val, COLORS[0])
                pygame.draw.rect(window, color, (c*CELL_SIZE + x_off, r*CELL_SIZE + y_off, CELL_SIZE-1, CELL_SIZE-1))
        
        # Overlay the agent start and goals
        for p, color in [(p1_s, COLORS['p1_s']), (p2_s, COLORS['p2_s']), (p1_g, COLORS['p1_g']), (p2_g, COLORS['p2_g'])]:
            pygame.draw.circle(window, color, (p[1]*CELL_SIZE + x_off + 12, p[0]*CELL_SIZE + y_off + 12), 8)

    def draw_instructions(color):
        instr_txt = stat_title_font.render("Press 'R' to restart with new settings | 'ESC' to close simulation", True, color)
        window.blit(instr_txt, (window_width // 2 - instr_txt.get_width() // 2, HEIGHT + 135))

    def draw_statistics():
        # Premium dark container card for statistics
        pygame.draw.rect(window, (44, 44, 46), (20, HEIGHT + 60, window_width - 40, 65), border_radius=6)
        
        # --- Dijkstra Column ---
        col1_x = 35
        y_start = HEIGHT + 65
        
        title_d = stat_title_font.render("DIJKSTRA ALGORITHM (UNINFORMED)", True, (245, 245, 247))
        window.blit(title_d, (col1_x, y_start))
        
        d1_status = f"{len(path_d1)} steps" if path_d1 else "No Path Found"
        d2_status = f"{len(path_d2)} steps" if path_d2 else "No Path Found"
        
        txt_d1 = info_font.render(f"Agent 1 (Coral Goal): Path = {d1_status}  |  Tiles Explored: {len(visited_d1)}", True, (254, 202, 202))
        txt_d2 = info_font.render(f"Agent 2 (Blue Goal): Path = {d2_status}  |  Tiles Explored: {len(visited_d2)}", True, (191, 219, 254))
        
        window.blit(txt_d1, (col1_x, y_start + 20))
        window.blit(txt_d2, (col1_x, y_start + 38))
        
        # --- A* Column ---
        col2_x = WIDTH + 45
        
        title_a = stat_title_font.render("A* ALGORITHM (HEURISTIC-GUIDED)", True, (245, 245, 247))
        window.blit(title_a, (col2_x, y_start))
        
        a1_status = f"{len(path_a1)} steps" if path_a1 else "No Path Found"
        a2_status = f"{len(path_a2)} steps" if path_a2 else "No Path Found"
        
        txt_a1 = info_font.render(f"Agent 1 (Coral Goal): Path = {a1_status}  |  Tiles Explored: {len(visited_a1)}", True, (254, 202, 202))
        txt_a2 = info_font.render(f"Agent 2 (Blue Goal): Path = {a2_status}  |  Tiles Explored: {len(visited_a2)}", True, (191, 219, 254))
        
        window.blit(txt_a1, (col2_x, y_start + 20))
        window.blit(txt_a2, (col2_x, y_start + 38))

    d_copy = [row[:] for row in matrix_dijkstra]
    a_copy = [row[:] for row in matrix_astar]
    
    max_visited_len = max(len(visited_d1), len(visited_d2), len(visited_a1), len(visited_a2))
    
    # 1. Search Space Exploration Animation Phase
    # Process 2 visited tiles per loop iteration for fluid visualization
    step_size = 2
    for i in range(0, max_visited_len, step_size):
        # Event handler to prevent window hanging
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

        # Update Dijkstra exploration matrix
        for offset in range(step_size):
            idx = i + offset
            if idx < len(visited_d1):
                r, c = visited_d1[idx]
                if (r, c) not in (p1_s, p1_g, p2_s, p2_g):
                    if d_copy[r][c] == 0:
                        d_copy[r][c] = 'v1'
            if idx < len(visited_d2):
                r, c = visited_d2[idx]
                if (r, c) not in (p1_s, p1_g, p2_s, p2_g):
                    if d_copy[r][c] == 0:
                        d_copy[r][c] = 'v2'
                    elif d_copy[r][c] == 'v1':
                        d_copy[r][c] = 'v_both'

        # Update A* exploration matrix
        for offset in range(step_size):
            idx = i + offset
            if idx < len(visited_a1):
                r, c = visited_a1[idx]
                if (r, c) not in (p1_s, p1_g, p2_s, p2_g):
                    if a_copy[r][c] == 0:
                        a_copy[r][c] = 'v1'
            if idx < len(visited_a2):
                r, c = visited_a2[idx]
                if (r, c) not in (p1_s, p1_g, p2_s, p2_g):
                    if a_copy[r][c] == 0:
                        a_copy[r][c] = 'v2'
                    elif a_copy[r][c] == 'v1':
                        a_copy[r][c] = 'v_both'

        window.fill((30, 30, 32))
        draw_grid(d_copy, 20, 50, "DIJKSTRA (UNINFORMED)")
        draw_grid(a_copy, WIDTH + 30, 50, "A* (HEURISTIC-GUIDED)")
        draw_statistics()
        draw_instructions((150, 150, 150))
        pygame.display.flip()
        time.sleep(0.012)

    # 2. Final Shortest Path Overlay Phase
    window.fill((30, 30, 32))
    draw_grid(d_copy, 20, 50, "DIJKSTRA (UNINFORMED)")
    draw_grid(a_copy, WIDTH + 30, 50, "A* (HEURISTIC-GUIDED)")
    
    # Overlay the shortest paths explicitly
    draw_shortest_path_line(window, path_d1, 20, 50, COLORS['line_1'])
    draw_shortest_path_line(window, path_d2, 20, 50, COLORS['line_2'])
    draw_shortest_path_line(window, path_a1, WIDTH + 30, 50, COLORS['line_1'])
    draw_shortest_path_line(window, path_a2, WIDTH + 30, 50, COLORS['line_2'])

    draw_statistics()
    draw_instructions((255, 204, 0)) # Vibrant yellow for active instructions
    pygame.display.flip()

    # Event loop to keep window open and interactive
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