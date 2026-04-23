from input_data import get_input_data
from obstacles import create_fixed_obstacles, create_random_obstacles
from pathfinding import Dijkstra, A_star
from visualization import draw_matrices, interactive_placement

def main():
    while True:
        # 1. Get user configuration
        config = get_input_data()
        if not config: 
            break

        # 2. Setup matrices and generate obstacles FIRST
        grid_d = [[0 for _ in range(20)] for _ in range(20)]
        grid_a = [[0 for _ in range(20)] for _ in range(20)]
        
        if config['obs_type'] == "fixed":
            create_fixed_obstacles(grid_d)
            create_fixed_obstacles(grid_a)
        else:
            create_random_obstacles(grid_d, config['obs_count'])
            # Clone layout for A* so they share the exact same grid
            for r in range(20):
                for c in range(20):
                    grid_a[r][c] = grid_d[r][c]

        # 3. Interactive Agent Placement (User clicks on grid)
        p1_s, p1_g, p2_s, p2_g = interactive_placement(grid_d)

        # 4. Execute pathfinding algorithms
        path_d1 = Dijkstra(grid_d, p1_s, p1_g)
        path_d2 = Dijkstra(grid_d, p2_s, p2_g)
        
        path_a1 = A_star(grid_a, p1_s, p1_g)
        path_a2 = A_star(grid_a, p2_s, p2_g)

        # 5. Visualize Results
        # Returns True if 'R' is pressed, False if ESC/Close is pressed
        restart = draw_matrices(grid_d, grid_a, 
                                p1_s, p2_s, 
                                p1_g, p2_g,
                                path_d1, path_d2, path_a1, path_a2)
        
        if not restart:
            break

if __name__ == "__main__":
    main()