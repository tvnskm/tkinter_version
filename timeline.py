import tkinter as tk
from tkinter import ttk

class Timeline(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333")
        self.create_widgets()

    def create_widgets(self):
        # Scrollable timeline canvas
        self.timeline_canvas = tk.Canvas(self, bg="#333333")
        self.timeline_canvas.pack(side="left", fill="both", expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.timeline_canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.timeline_canvas.configure(yscrollcommand=scrollbar.set)

        # Create frame inside the canvas
        timeline_frame = tk.Frame(self.timeline_canvas, bg="#333333")
        self.timeline_canvas.create_window((0, 0), window=timeline_frame, anchor="nw")

        # Display 24 hours in 15-minute intervals
        self.add_timeline_labels(timeline_frame)

        # Update scroll region
        timeline_frame.bind("<Configure>", lambda e: self.timeline_canvas.configure(scrollregion=self.timeline_canvas.bbox("all")))

    def add_timeline_labels(self, frame):
        for hour in range(24):
            for minute in range(0, 60, 15):
                time_label = tk.Label(frame, text=f"{hour:02d}:{minute:02d}", bg="#333333", fg="white", width=7, anchor="w")
                time_label.pack(pady=5, anchor="w")
