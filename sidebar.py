# sidebar.py
import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, parent, bg_color, profile_action):
        super().__init__(parent, bg=bg_color)
        self.profile_action = profile_action  # Action callback for the Profile button
        self.create_widgets(bg_color)

    def create_widgets(self, bg_color):
        # Profile button instead of label
        self.profile_btn = tk.Button(self, text="Profile", bg=bg_color, fg="white", font=("Arial", 14), bd=0, command=self.profile_action)
        self.profile_btn.pack(pady=20, anchor="w", padx=20)

        # Sidebar buttons
        self.attendance_btn = tk.Button(self, text="Attendance", bg=bg_color, fg="white", bd=0)
        self.attendance_btn.pack(pady=10, anchor="w", padx=20)

        self.mess_btn = tk.Button(self, text="Mess Menu", bg=bg_color, fg="white", bd=0)
        self.mess_btn.pack(pady=10, anchor="w", padx=20)

        self.settings_btn = tk.Button(self, text="Settings", bg=bg_color, fg="white", bd=0)
        self.settings_btn.pack(pady=10, anchor="w", padx=20)

        # ADD TASK button below all other buttons, anchored at the bottom
        self.add_task_btn = tk.Button(self, text="ADD TASK", bg=bg_color, fg="white", bd=0)
        self.add_task_btn.pack(side="bottom", pady=20, anchor="w", padx=20)

    def set_attendance_action(self, action):
        self.attendance_btn.config(command=action)

    def set_mess_menu_action(self, action):
        self.mess_btn.config(command=action)

    def set_settings_action(self, action):
        self.settings_btn.config(command=action)

    def set_add_task_action(self, action):
        self.add_task_btn.config(command=action)
