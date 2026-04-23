import customtkinter as ctk
from tkinter import messagebox

def get_input_data():
    data = {}
    
    # Set appearance mode and color theme
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Pathfinding Config")
    root.geometry("400x300")
    
    # Make the root window grid responsive
    root.grid_columnconfigure(0, weight=1)

    # Main container frame
    main_frame = ctk.CTkFrame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=1)

    # Title Label
    title_lbl = ctk.CTkLabel(main_frame, text="Simulation Settings", font=ctk.CTkFont(size=20, weight="bold"))
    title_lbl.grid(row=0, column=0, pady=(20, 10))

    # Radio buttons for obstacle type
    obs_var = ctk.IntVar(value=1)
    radio_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    radio_frame.grid(row=1, column=0, pady=10)
    
    ctk.CTkRadioButton(radio_frame, text="Fixed", variable=obs_var, value=1).pack(side="left", padx=10)
    ctk.CTkRadioButton(radio_frame, text="Random", variable=obs_var, value=2).pack(side="left", padx=10)

    # Number of obstacles input
    obs_lbl = ctk.CTkLabel(main_frame, text="Random Obstacles (Min 40):")
    obs_lbl.grid(row=2, column=0, pady=(10, 0))

    obs_entry = ctk.CTkEntry(main_frame)
    obs_entry.insert(0, "40")
    obs_entry.grid(row=3, column=0, pady=(0, 15))

    def submit():
        # Validate that at least 40 obstacles are generated if 'Random' is selected
        try:
            obs_count = int(obs_entry.get())
        except ValueError:
            obs_count = 0

        if obs_var.get() == 2 and obs_count < 40:
            messagebox.showwarning("Warning", "Please enter at least 40 obstacles to proceed.")
            return

        data['obs_type'] = "fixed" if obs_var.get() == 1 else "random"
        data['obs_count'] = obs_count
        root.destroy()

    # Submit Button
    submit_btn = ctk.CTkButton(main_frame, text="Continue to Placement", font=ctk.CTkFont(size=15, weight="bold"), command=submit, height=40)
    submit_btn.grid(row=4, column=0, pady=20)

    root.mainloop()
    return data