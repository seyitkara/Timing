import tkinter as tk
from tkinter import messagebox

# Function to increase time by 1 minute
def increase_time():
    global remaining_time
    remaining_time += 60
    update_time_label()

def increase_time_5m():
    global remaining_time
    remaining_time += 300
    update_time_label()

# Function to reset time
def reset_time():
    global remaining_time
    remaining_time = initial_time
    update_time_label()

# Function to start countdown
def start_countdown():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        update_time_label()
        if remaining_time > 0:
            root.after(1000, start_countdown)
        else:
            messagebox.showwarning("Time's Up!", "The time has run out.")

# Function to update time label
def update_time_label():
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    time_label.config(text=f"Time Remaining: {minutes:02d}:{seconds:02d}")

# Main tkinter window
root = tk.Tk()
root.geometry("300x200")
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'white')  # Set background color as transparent
root.title("Countdown Timer")

# Initialize variables
initial_time = 5 * 60  # Initial time in seconds (5 minutes)
remaining_time = initial_time

# Create buttons
increase_button = tk.Button(root, text="Increase Time by 1 Minute", command=increase_time)
increase_button_5m = tk.Button(root, text="Increase Time by 5 Minute", command=increase_time_5m)
reset_button = tk.Button(root, text="Reset Time", command=reset_time)
countdown_button = tk.Button(root, text="Start Countdown", command=start_countdown)

# Create time label
time_label = tk.Label(root, text="Time Remaining: 05:00", font=("Arial", 14))

# Place widgets in the window
time_label.pack(pady=20)
increase_button.pack()
increase_button_5m.pack()
reset_button.pack()
countdown_button.pack()

# Start the Tkinter event loop
root.mainloop()
