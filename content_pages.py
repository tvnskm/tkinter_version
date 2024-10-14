import tkinter as tk

class AttendancePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1f1f1f")
        label = tk.Label(self, text="Attendance Page", bg="#1f1f1f", fg="white")
        label.pack(pady=20)

class MessMenuPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1f1f1f")
        label = tk.Label(self, text="Mess Menu Page", bg="#1f1f1f", fg="white")
        label.pack(pady=20)

class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1f1f1f")
        label = tk.Label(self, text="Settings Page", bg="#1f1f1f", fg="white")
        label.pack(pady=20)

class EventCardsPage(tk.Frame):
    def __init__(self, parent, timeline_canvas):
        super().__init__(parent, bg="#444444")
        self.timeline_canvas = timeline_canvas
        self.create_event_cards()

    def create_event_cards(self):
        # Example events with associated times
        events = [
            ("Eating", "12:30", "#ffcc00"),
            ("Gym", "14:00", "#00ccff"),
            ("Meeting", "16:00", "#ff6699"),
        ]

        for event_name, event_time, bg_color in events:
            # Create a card for each event
            event_card = tk.Frame(self, bg=bg_color, pady=10, padx=10)
            event_label = tk.Label(event_card, text=f"{event_name} at {event_time}", bg=bg_color, fg="white")
            event_label.pack(fill="both", expand=True)

            # Pack the event card
            event_card.pack(pady=5, fill="x")
