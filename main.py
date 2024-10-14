import tkinter as tk
from tkinter import font
from sidebar import Sidebar
from header import Header
from timeline import Timeline
from content_pages import AttendancePage, MessMenuPage, SettingsPage, EventCardsPage

# Create the main window
root = tk.Tk()
root.title("LOCKED-IN")
root.geometry("900x600")

# Define colors and fonts
sidebar_bg = "#2e2e2e"
main_bg = "#1f1f1f"
navbar_bg = "#444444"
footer_bg = "#444444"

title_font = font.Font(family="Helvetica", size=24, weight="bold")

# Create the header (navbar)
header = Header(root, title_font, navbar_bg)
header.pack(side="top", fill="x")

# Main content frame
main_frame = tk.Frame(root, bg=main_bg)
main_frame.pack(side="right", expand=True, fill="both")

# Create a function to show the timeline and event cards
def show_timeline():
    for widget in main_frame.winfo_children():
        widget.destroy()  # Clear previous content

    # Create a frame for timeline and event cards
    content_frame = tk.Frame(main_frame, bg=main_bg)
    content_frame.pack(fill="both", expand=True)

    # Create a canvas for scrolling
    canvas = tk.Canvas(content_frame, bg=main_bg)
    scroll_y = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=main_bg)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scroll_y.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    # Create the timeline
    timeline = Timeline(scrollable_frame)
    timeline.pack(side="left", fill="y", expand=False)

    # Create the Event Cards Page
    event_cards_page = EventCardsPage(scrollable_frame, timeline.timeline_canvas)
    event_cards_page.pack(side="left", fill="y", expand=True)

# Create the sidebar with the profile action
sidebar = Sidebar(root, sidebar_bg, show_timeline)  # Provide show_timeline as the profile action
sidebar.pack(side="left", fill="y")

# Initially show the timeline and event cards
show_timeline()

# Function to switch pages in the main content area
def switch_page(page_class):
    for widget in main_frame.winfo_children():
        widget.destroy()
    page = page_class(main_frame)
    page.pack(fill="both", expand=True)

# Sidebar button actions
sidebar.set_attendance_action(lambda: switch_page(AttendancePage))
sidebar.set_mess_menu_action(lambda: switch_page(MessMenuPage))
sidebar.set_settings_action(lambda: switch_page(SettingsPage))

# Start the main loop
root.mainloop()
