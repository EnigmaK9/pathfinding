import tkinter as tk

def show_results():
    results = tk.Tk()
    results.title("Pathfinding Results")

    text = tk.Text(results)
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A1 Path Length: {len(path_A1_fixed_dijkstra) if path_A1_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles Dijkstra - A2 Path Length: {len(path_A2_fixed_dijkstra) if path_A2_fixed_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A1 Path Length: {len(path_A1_fixed_a_star) if path_A1_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Fixed Obstacles A* - A2 Path Length: {len(path_A2_fixed_a_star) if path_A2_fixed_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A1 Path Length: {len(path_A1_random_dijkstra) if path_A1_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles Dijkstra - A2 Path Length: {len(path_A2_random_dijkstra) if path_A2_random_dijkstra else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A1 Path Length: {len(path_A1_random_a_star) if path_A1_random_a_star else 'No Path'}\n")
    text.insert(tk.END, f"Random Obstacles A* - A2 Path Length: {len(path_A2_random_a_star) if path_A2_random_a_star else 'No Path'}\n")

    text.pack()
    results.mainloop()
