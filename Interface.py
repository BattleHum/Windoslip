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



def timert(time_sec):
    while time_sec:
        mins, sec = divmod(time_sec, 60)
        time_format = '{:02d}:{:02d}'.format(mins, sec)
        print(time_format)
        time.sleep(1)
        time_sec -= 1
    print("Timer ended")

def select_time():
    if not Radio.get():  # if not click radiobutton
        messagebox.showerror(message="You must entry variant shutdown!")
    elif not Combo1.get():  # if not selected time
        messagebox.showerror(message="You have not selected a time for the timer!")
    else:
        variant = Radio.get()
        if variant == 1:
            if combolist[0]:
                timert(300)
            if combolist[1]:
                timert(600)
            saveprogress()
        elif variant == 2:
            fullOff()
        elif variant == 3:
            restart()


# Start window
Main = tkinter.Tk()
Main.title("Windosleep")
Main.geometry("500x400")
Main.iconphoto(False, tkinter.PhotoImage(file='images/icon.png'))
Main.configure(bg='#F8F8FF')
Main.resizable(width=False, height=False)

# Labels
Label1 = Label(text="Select settings", font=("Ivy 12 bold"), bg="#F8F8FF", fg="#FF0000")
Label1.place(x=10, y=1)


Label2 = Label(text="Set your time", font=("Ivy 12 bold"), bg="#F8F8FF", fg="#FF0000")
Label2.place(x=10, y=250)

# Base radiobutton
Radio = tkinter.IntVar()

RadioSave = Radiobutton(text="Save the process and turn off the computer", variable=Radio, bg="#F8F8FF", value=1, )
RadioSave.place(x=9, y=30)

RadioFullOff = Radiobutton(text="Do not save the process and turn off the computer", variable=Radio, bg="#F8F8FF", value=2)
RadioFullOff.place(x=9, y=60)

RadioRestart = Radiobutton(text="Restart windows", variable=Radio, bg="#F8F8FF", value=3)
RadioRestart.place(x=9, y=90)

# Combobox minutes
combolist = ["5 minutes", "10 minutes", "15 minutes", "20 minutes", "25 minutes", "30 minutes", "1 hours", "2 hours", "3 hours"]
Combo1 = ttk.Combobox(values=combolist)
Combo1.place(x=13, y=300)

# Base button
But = Button(text="Start", width=20, background="red", fg="white", command=select_time)
But.place(x=9, y=340)

# But stop
#Butstop = Button(text="Abort stutdown", width=20, background="grey", fg="white", command=notshutdown)
#Butstop.place(x=9, y=360)
# Label from time
LabelTime = tkinter.StringVar()
LabelT = Label(Main, textvariable=LabelTime)
LabelT.place(x=180, y=300)


# Frames
Frame1 = Frame(Main, width=1000, background="black")
Frame1.place(x=0, y=180)




Main.mainloop()