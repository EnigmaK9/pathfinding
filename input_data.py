import customtkinter as ctk
import tkinter as tk
from obstacles import create_fixed_obstacles, create_random_obstacles

def get_input_data():
    data = {}
    
    # Set appearance mode and color theme
    ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

    root = ctk.CTk()
    root.title("Pathfinding Config")
    root.geometry("500x400")
    
    # Make the root window grid responsive
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # Main container frame
    main_frame = ctk.CTkFrame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Configure inner frame columns to expand
    main_frame.grid_columnconfigure(1, weight=1)

    fields = [
        ("A1 Start (r,c)", "10,10"), 
        ("A1 Goal (r,c)", "0,0"), 
        ("A2 Start (r,c)", "12,12"), 
        ("A2 Goal (r,c)", "14,19")
    ]
    entries = []

    # Title Label
    title_lbl = ctk.CTkLabel(main_frame, text="Simulation Parameters", font=ctk.CTkFont(size=20, weight="bold"))
    title_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 15))

    # Generate input fields dynamically
    for i, (label, default) in enumerate(fields, start=1):
        lbl = ctk.CTkLabel(main_frame, text=label, font=ctk.CTkFont(size=14))
        lbl.grid(row=i, column=0, padx=20, pady=10, sticky="w")
        
        ent = ctk.CTkEntry(main_frame, font=ctk.CTkFont(size=14))
        ent.insert(0, default)
        ent.grid(row=i, column=1, padx=20, pady=10, sticky="ew")
        entries.append(ent)

    # Radio buttons for obstacle type
    obs_var = tk.IntVar(value=1)
    radio_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    radio_frame.grid(row=5, column=0, columnspan=2, pady=20)
    
    ctk.CTkRadioButton(radio_frame, text="Fixed Obstacles", variable=obs_var, value=1, font=ctk.CTkFont(size=14)).pack(side="left", padx=15)
    ctk.CTkRadioButton(radio_frame, text="Random Obstacles", variable=obs_var, value=2, font=ctk.CTkFont(size=14)).pack(side="left", padx=15)

    def submit():
        # Retrieve and parse data on submit
        data['p1_s'] = tuple(map(int, entries[0].get().split(',')))
        data['p1_g'] = tuple(map(int, entries[1].get().split(',')))
        data['p2_s'] = tuple(map(int, entries[2].get().split(',')))
        data['p2_g'] = tuple(map(int, entries[3].get().split(',')))
        data['obs_type'] = "fixed" if obs_var.get() == 1 else "random"
        root.destroy()

    # Submit Button
    submit_btn = ctk.CTkButton(main_frame, text="Start Simulation", font=ctk.CTkFont(size=15, weight="bold"), command=submit, height=40)
    submit_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")

    root.mainloop()
    return data