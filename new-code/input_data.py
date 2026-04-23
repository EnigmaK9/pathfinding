import tkinter as tk
from obstacles import create_fixed_obstacles, create_random_obstacles

def get_input_data():
    data = {}
    root = tk.Tk()
    root.title("Pathfinding Config")

    fields = [("A1 Start (r,c)", "10,10"), ("A1 Goal (r,c)", "0,0"), 
              ("A2 Start (r,c)", "12,12"), ("A2 Goal (r,c)", "14,19")]
    entries = []

    for label, default in fields:
        row = tk.Frame(root)
        lbl = tk.Label(row, text=label, width=15)
        ent = tk.Entry(row)
        ent.insert(0, default)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lbl.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append(ent)

    obs_var = tk.IntVar(value=1)
    tk.Radiobutton(root, text="Fixed Obstacles", variable=obs_var, value=1).pack()
    tk.Radiobutton(root, text="Random Obstacles", variable=obs_var, value=2).pack()

    def submit():
        data['p1_s'] = tuple(map(int, entries[0].get().split(',')))
        data['p1_g'] = tuple(map(int, entries[1].get().split(',')))
        data['p2_s'] = tuple(map(int, entries[2].get().split(',')))
        data['p2_g'] = tuple(map(int, entries[3].get().split(',')))
        data['obs_type'] = "fixed" if obs_var.get() == 1 else "random"
        root.destroy()

    tk.Button(root, text="Start Simulation", command=submit).pack(pady=10)
    root.mainloop()
    return data
