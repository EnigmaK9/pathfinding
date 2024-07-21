import tkinter as tk
from obstacles import create_fixed_obstacles, create_random_obstacles

def get_input_data(matrix_fixed, matrix_random, A1_start_pos, A1_goal_pos, A2_start_pos, A2_goal_pos):
    '''
    This function sets up the Tkinter GUI to collect user input for the start and goal positions of two agents,
    as well as the type of obstacles (fixed or random) to be placed in the matrices.
    '''
    
    def on_submit():
        '''
        This function is called when the user submits the form. It processes the input data, 
        creates obstacles in the matrices, and sets the start and goal positions for the agents.
        '''
        global obstacle_type
        
        # Determine the type of obstacles based on user selection and create them in the matrices
        if obstacles_var.get() == 1:
            obstacle_type = "fixed"
            create_fixed_obstacles(matrix_fixed)
            create_fixed_obstacles(matrix_random)
        else:
            obstacle_type = "random"
            create_random_obstacles(matrix_fixed, int(num_obstacles_entry.get()))
            create_random_obstacles(matrix_random, int(num_obstacles_entry.get()))

        # Set the start and goal positions for agents A1 and A2
        A1_start_pos[:] = list(map(int, A1_start_entry.get().split(',')))
        A1_goal_pos[:] = list(map(int, A1_goal_entry.get().split(',')))
        A2_start_pos[:] = list(map(int, A2_start_entry.get().split(',')))
        A2_goal_pos[:] = list(map(int, A2_goal_entry.get().split(',')))

        # Update the matrices to mark the start and goal positions
        matrix_fixed[A1_start_pos[0]][A1_start_pos[1]] = 2
        matrix_fixed[A2_start_pos[0]][A2_start_pos[1]] = 3
        matrix_fixed[A1_goal_pos[0]][A1_goal_pos[1]] = 5
        matrix_fixed[A2_goal_pos[0]][A2_goal_pos[1]] = 6

        matrix_random[A1_start_pos[0]][A1_start_pos[1]] = 2
        matrix_random[A2_start_pos[0]][A2_start_pos[1]] = 3
        matrix_random[A1_goal_pos[0]][A1_goal_pos[1]] = 5
        matrix_random[A2_goal_pos[0]][A2_goal_pos[1]] = 6

        # Close the input window
        window.destroy()

    # Create the main window
    window = tk.Tk()
    window.title("Input Configuration")

    # Create and place labels and entry fields for the start and goal positions of agents A1 and A2
    tk.Label(window, text="A1 Start Position (row,col):").grid(row=0, column=0)
    A1_start_entry = tk.Entry(window)
    A1_start_entry.grid(row=0, column=1)
    A1_start_entry.insert(0, "10,10")

    tk.Label(window, text="A1 Goal Position (row,col):").grid(row=1, column=0)
    A1_goal_entry = tk.Entry(window)
    A1_goal_entry.grid(row=1, column=1)
    A1_goal_entry.insert(0, "0,0")

    tk.Label(window, text="A2 Start Position (row,col):").grid(row=2, column=0)
    A2_start_entry = tk.Entry(window)
    A2_start_entry.grid(row=2, column=1)
    A2_start_entry.insert(0, "12,12")

    tk.Label(window, text="A2 Goal Position (row,col):").grid(row=3, column=0)
    A2_goal_entry = tk.Entry(window)
    A2_goal_entry.grid(row=3, column=1)
    A2_goal_entry.insert(0, "14,19")

    # Create radio buttons for selecting the type of obstacles
    obstacles_var = tk.IntVar(value=1)
    tk.Radiobutton(window, text="Fixed Obstacles", variable=obstacles_var, value=1).grid(row=4, column=0)
    tk.Radiobutton(window, text="Random Obstacles", variable=obstacles_var, value=2).grid(row=4, column=1)

    # Create and place label and entry field for the number of random obstacles
    tk.Label(window, text="Number of Random Obstacles:").grid(row=5, column=0)
    num_obstacles_entry = tk.Entry(window)
    num_obstacles_entry.grid(row=5, column=1)
    num_obstacles_entry.insert(0, "50")

    # Create and place the submit button
    tk.Button(window, text="Submit", command=on_submit).grid(row=6, column=0, columnspan=2)

    # Start the Tkinter main loop
    window.mainloop()
    return obstacle_type
