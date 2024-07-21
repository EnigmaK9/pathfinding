import tkinter as tk

def show_results():
    '''
    This function creates a Tkinter window to display the results of the pathfinding algorithms.
    It shows the path lengths for both fixed and random obstacles for both Dijkstra and A* algorithms.
    '''
    
    # Create the main Tkinter window for displaying results
    results = tk.Tk()
    results.title("Pathfinding Results")  # Set the title of the window

    # Create a Text widget to display the results
    text = tk.Text(results)
    
    # Insert the results into the Text widget
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A1 Path Length: {len(path_A1_fixed_dijkstra) if path_A1_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A2 Path Length: {len(path_A2_fixed_dijkstra) if path_A2_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A1 Path Length: {len(path_A1_fixed_a_star) if path_A1_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A2 Path Length: {len(path_A2_fixed_a_star) if path_A2_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A1 Path Length: {len(path_A1_random_dijkstra) if path_A1_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A2 Path Length: {len(path_A2_random_dijkstra) if path_A2_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A1 Path Length: {len(path_A1_random_a_star) if path_A1_random_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A2 Path Length: {len(path_A2_random_a_star) if path_A2_random_a_star else 'No Path'}\n")

    # Pack the Text widget into the window
    text.pack()
    
    # Start the Tkinter main loop to display the window
    results.mainloop()
