from tkinter import *
from tkinter import messagebox, ttk
import subprocess
import time
import tkinter


def notshutdown():
    subprocess.call(["shutdown", "/a"])
def fullOff():
    subprocess.call(["shutdown", "/s"])
def saveprogress():
    subprocess.call(["shutdown", "/h"])
def restart():
    subprocess.call(["shutdown", "/r"])

def stringvar():
    my_time = 1800
    for my_time in range(my_time, 0, -1):
        seconds = my_time % 60
        minutes = int(my_time / 60) % 60
        timer = (f"{minutes:02}:{seconds:02}")
        Timer.set(timer)
        print(timer)
        time.sleep(1)



def select_time():
    if not Radio.get():  # if not click radiobutton
        messagebox.showerror(message="You must entry variant shutdown!")
    else:
        variant = Radio.get()
        if variant == 1:
            stringvar()
            saveprogress()
        if variant == 2:
            stringvar()
            fullOff()
        if variant == 3:
            stringvar()
            restart()


# Start window
Main = tkinter.Tk()
Main.title("Windosleep")
Main.geometry("500x400")
#Main.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
Main.configure(bg='#F8F8FF')
Main.resizable(width=False, height=False)

# Labels
Label1 = Label(text="Change function", font=("Ivy 12 bold"), bg="#F8F8FF", fg="red")
Label1.place(x=10, y=1)

Label2 = Label(text="Start time", font=("Ivy 12 bold"), bg="#F8F8FF", fg="red")
Label2.place(x=10, y=250)

Label3 = Label(text="This program sets a time - 30 minutes before the function will be executed", bg="#F8F8FF", font=("Arial Rounded MT Bold", 10, ), fg="black")
Label3.place(x=9, y=280)

# Radiobuttons

Radio = IntVar()

RadioSave = Radiobutton(text="Save the process and turn off the computer", variable=Radio, bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=1, )
RadioSave.place(x=9, y=30)

RadioFullOff = Radiobutton(text="Do not save the process and turn off the computer", variable=Radio, bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=2)
RadioFullOff.place(x=9, y=60)

RadioRestart = Radiobutton(text="Restart windows", variable=Radio, bg="#F8F8FF", fg="black", font=("Arial Black", 11), value=3)
RadioRestart.place(x=9, y=90)

# Base button
But = ttk.Button(text="Start", width=20, command=select_time)
But.place(x=9, y=340)


# Label from time
Timer = tkinter.StringVar()
timeLabel = tkinter.Label(Main, textvariable = Timer, font=("Britannic Bold", 11))
timeLabel.place(x=9, y=310)

# Frames
Frame1 = Frame(Main, width=1000, background="black")
Frame1.place(x=0, y=180)


Main.mainloop()