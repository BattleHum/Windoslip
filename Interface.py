from tkinter import *
from tkinter import messagebox, ttk
import subprocess
import os

# Global variable to control the timer
stop_timer = False

def cancel_shutdown():
    subprocess.call(["shutdown", "/a"])

def shutdown():
    subprocess.call(["shutdown", "/s", "/f", "/t", "0"])

def hibernate():
    subprocess.call(["shutdown", "/h"])

def restart():
    subprocess.call(["shutdown", "/r", "/f", "/t", "0"])

def start_timer(duration, callback):
    """Starts the timer with the given duration in minutes and executes the callback."""
    global stop_timer
    stop_timer = False  # Reset stop flag

    def timer_logic(remaining_time):
        global stop_timer
        if stop_timer:  # Stop timer if stop flag is set
            Timer.set("Canceled")
            return
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            Timer.set(f"{minutes:02}:{seconds:02}")
            Main.after(1000, timer_logic, remaining_time - 1)
        else:
            callback()

    timer_logic(duration)

def select_time():
    """Handles the selection of action after the timer ends."""
    global stop_timer
    if Radio.get() == 0:  # If no radio button is selected
        messagebox.showerror("Error", "Please select a shutdown option!")
        return

    try:
        time_minutes = int(timeEntry.get())
        if time_minutes <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid time in minutes!")
        return

    duration_seconds = time_minutes * 60
    option = Radio.get()

    def execute_action():
        if option == 1:
            hibernate()
        elif option == 2:
            shutdown()
        elif option == 3:
            restart()

    timeEntry.delete(0, END)  # Clear input field after starting the timer
    start_timer(duration_seconds, execute_action)

def stop_countdown():
    """Stops the countdown timer."""
    global stop_timer
    stop_timer = True
    cancel_shutdown()
    Timer.set("Stopped")

# Main window
Main = Tk()
Main.title("Windosleep")
Main.geometry("500x400")
Main.configure(bg='#F8F8FF')
Main.resizable(width=False, height=False)

# Program icon (check if file exists)
icon_path = "icon.png"
if os.path.exists(icon_path):
    Main.iconphoto(False, PhotoImage(file=icon_path))

# Labels
Label1 = Label(Main, text="Select an option:", font=("Ivy 12 bold"), bg="#F8F8FF", fg="red")
Label1.place(x=10, y=1)

Label2 = Label(Main, text="Enter time (minutes):", font=("Ivy 12 bold"), bg="#F8F8FF", fg="red")
Label2.place(x=10, y=250)

Label3 = Label(Main, text="The program will execute the selected action after the timer ends.",
               bg="#F8F8FF", font=("Arial Rounded MT Bold", 10), fg="black")
Label3.place(x=9, y=280)

# Radio buttons
Radio = IntVar()

RadioSave = Radiobutton(Main, text="Hibernate and shut down", variable=Radio, 
                        bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=1)
RadioSave.place(x=9, y=30)

RadioFullOff = Radiobutton(Main, text="Shut down without saving", variable=Radio, 
                           bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=2)
RadioFullOff.place(x=9, y=60)

RadioRestart = Radiobutton(Main, text="Restart", variable=Radio, 
                           bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=3)
RadioRestart.place(x=9, y=90)

# Time input field
timeEntry = ttk.Entry(Main, width=10)
timeEntry.place(x=200, y=250)

# Start and stop buttons
But = ttk.Button(Main, text="Start", width=20, command=select_time)
But.place(x=9, y=340)

StopBut = ttk.Button(Main, text="Cancel", width=20, command=stop_countdown)
StopBut.place(x=200, y=340)

# Timer display
Timer = StringVar()
Timer.set("00:00")
timeLabel = Label(Main, textvariable=Timer, font=("Britannic Bold", 11), bg="#F8F8FF", fg="black")
timeLabel.place(x=9, y=310)

# Run program
Main.mainloop()
