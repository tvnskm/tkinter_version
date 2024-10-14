import tkinter as tk

class Header(tk.Frame):
    def __init__(self, parent, title_font, bg_color):
        super().__init__(parent, bg=bg_color, height=50)
        self.create_widgets(title_font, bg_color)

    def create_widgets(self, title_font, bg_color):
        title_label = tk.Label(self, text="LOCKED-IN", font=title_font, fg="white", bg=bg_color)
        title_label.pack(pady=10)
