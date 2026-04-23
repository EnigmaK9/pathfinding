from input_data import get_input_data
from obstacles import create_fixed_obstacles, create_random_obstacles
from pathfinding import Dijkstra, A_star
from visualization import draw_matrices

def main():
    while True:
        # 1. Obtener datos del usuario
        config = get_input_data()
        
        # Si el usuario cierra la ventana de CustomTkinter con la 'X', terminamos el programa
        if not config: 
            break

        # 2. Configurar matrices
        grid_d = [[0 for _ in range(20)] for _ in range(20)]
        grid_a = [[0 for _ in range(20)] for _ in range(20)]
        
        reserved = [config['p1_s'], config['p1_g'], config['p2_s'], config['p2_g']]
        
        if config['obs_type'] == "fixed":
            create_fixed_obstacles(grid_d)
            create_fixed_obstacles(grid_a)
        else:
            create_random_obstacles(grid_d, 50, reserved)
            # Asegurarse de que ambos algoritmos usen exactamente el mismo mapa aleatorio
            for r in range(20):
                for c in range(20):
                    grid_a[r][c] = grid_d[r][c]

        # 3. Ejecutar algoritmos
        path_d1 = Dijkstra(grid_d, config['p1_s'], config['p1_g'])
        path_d2 = Dijkstra(grid_d, config['p2_s'], config['p2_g'])
        
        path_a1 = A_star(grid_a, config['p1_s'], config['p1_g'])
        path_a2 = A_star(grid_a, config['p2_s'], config['p2_g'])

        # 4. Visualizar y esperar acción del usuario
        # draw_matrices devolverá True (reiniciar) o False (salir)
        restart = draw_matrices(grid_d, grid_a, 
                                config['p1_s'], config['p2_s'], 
                                config['p1_g'], config['p2_g'],
                                path_d1, path_d2, path_a1, path_a2)
        
        # Si el usuario presionó ESC o la X, salimos del bucle
        if not restart:
            break

if __name__ == "__main__":
    main()