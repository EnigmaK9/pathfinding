import pygame
import sys
import time

CELL_SIZE = 25
WIDTH = HEIGHT = 20 * CELL_SIZE

def draw_matrices(matrix_dijkstra, matrix_astar, p1_s, p2_s, p1_g, p2_g, path_d1, path_d2, path_a1, path_a2):
    pygame.init()
    
    # Dimensiones de la ventana
    window_width = WIDTH * 2 + 50
    window_height = HEIGHT + 150
    window = pygame.display.set_mode((window_width, window_height))
    
    pygame.display.set_caption("Dijkstra vs A*")
    font = pygame.font.SysFont("Arial", 18, bold=True)
    info_font = pygame.font.SysFont("Arial", 18)

    colors = {0: (255, 255, 255), 1: (50, 50, 50), 'x': (255, 0, 0), 'y': (0, 0, 255), 'xy': (255, 0, 255)}

    def draw_grid(m, x_off, y_off, title):
        # Dibujar título
        txt = font.render(title, True, (255, 255, 255))
        window.blit(txt, (x_off + WIDTH//2 - 40, y_off - 30))
        
        # Dibujar celdas
        for r in range(20):
            for c in range(20):
                val = m[r][c]
                color = colors.get(val, (200, 200, 200))
                pygame.draw.rect(window, color, (c*CELL_SIZE + x_off, r*CELL_SIZE + y_off, CELL_SIZE-1, CELL_SIZE-1))
        
        # Dibujar Inicio y Meta
        for p, color in [(p1_s, (0, 255, 0)), (p2_s, (0, 200, 0)), (p1_g, (255, 255, 0)), (p2_g, (200, 200, 0))]:
            pygame.draw.circle(window, color, (p[1]*CELL_SIZE + x_off + 12, p[0]*CELL_SIZE + y_off + 12), 8)

    def draw_instructions(color):
        instr_txt = info_font.render("Presiona 'R' para un nuevo test | 'ESC' para cerrar", True, color)
        # Centrar el texto en la parte inferior
        window.blit(instr_txt, (window_width // 2 - instr_txt.get_width() // 2, HEIGHT + 80))

    # Variables de animación
    d_copy = [row[:] for row in matrix_dijkstra]
    a_copy = [row[:] for row in matrix_astar]
    
    max_len = max(len(path_d1), len(path_d2), len(path_a1), len(path_a2))
    
    # Bucle de animación
    for i in range(max_len):
        if i < len(path_d1): d_copy[path_d1[i][0]][path_d1[i][1]] = 'x'
        if i < len(path_d2): d_copy[path_d2[i][0]][path_d2[i][1]] = 'y'
        if i < len(path_a1): a_copy[path_a1[i][0]][path_a1[i][1]] = 'x'
        if i < len(path_a2): a_copy[path_a2[i][0]][path_a2[i][1]] = 'y'
        
        window.fill((30, 30, 30))
        draw_grid(d_copy, 20, 50, "DIJKSTRA")
        draw_grid(a_copy, WIDTH + 30, 50, "A*")
        
        # Instrucciones tenues mientras se anima
        draw_instructions((150, 150, 150))
        
        pygame.display.flip()
        time.sleep(0.05)

    # Resaltar las instrucciones cuando termine la animación
    window.fill((30, 30, 30))
    draw_grid(d_copy, 20, 50, "DIJKSTRA")
    draw_grid(a_copy, WIDTH + 30, 50, "A*")
    draw_instructions((255, 255, 0)) # Amarillo para llamar la atención
    pygame.display.flip()

    # Esperar acción del usuario (R para reiniciar, ESC/X para salir)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Cierra el programa
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False  # Cierra el programa
                elif event.key == pygame.K_r:
                    pygame.quit()
                    return True   # Reinicia (abre el menú de nuevo)