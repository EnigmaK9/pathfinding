import tkinter as tk

def show_results(path_lengths):
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
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - Agent 1 Path Length: {len(path_A1_fixed_dijkstra) if path_A1_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - Agent 2 Path Length: {len(path_A2_fixed_dijkstra) if path_A2_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - Agent 1 Path Length: {len(path_A1_fixed_a_star) if path_A1_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - Agent 2 Path Length: {len(path_A2_fixed_a_star) if path_A2_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - Agent 1 Path Length: {len(path_A1_random_dijkstra) if path_A1_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - Agent 2 Path Length: {len(path_A2_random_dijkstra) if path_A2_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - Agent 1 Path Length: {len(path_A1_random_a_star) if path_A1_random_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - Agent 2 Path Length: {len(path_A2_random_a_star) if path_A2_random_a_star else 'No Path'}\n")

    # Display the number of tiles traversed
    text.insert(tk.END, f"\nTiles Traversed:\n")
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - Agent 1: {path_lengths[1]} tiles, Agent 2: {path_lengths[2]} tiles\n")
    text.insert(tk.END, f"Fixed Obstacles A* - Agent 1: {path_lengths[4]} tiles, Agent 2: {path_lengths[5]} tiles\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - Agent 1: {path_lengths[7]} tiles, Agent 2: {path_lengths[8]} tiles\n")
    text.insert(tk.END, f"Random Obstacles A* - Agent 1: {path_lengths[10]} tiles, Agent 2: {path_lengths[11]} tiles\n")

    # Pack the Text widget into the window
    text.pack()
    
    # Start the Tkinter main loop to display the window
    results.mainloop()
