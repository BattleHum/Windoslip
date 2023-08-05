from tkinter import *
from tkinter import ttk, messagebox
import time
import tkinter

def select_time():
    if not Radio.get():
        messagebox.showerror(message="You must entry variant shutdown!")
    elif not Combo1.get():
        messagebox.showerror(message="You have not selected a time for the timer!")
    else:
        time = Combo1.get()
        LabelTime.set(f"The function will work through {time}")
        timer()

def timer():
    pass



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

# Combobox minutes
combolist = ["5 minutes", "10 minutes", "15 minutes", "20 minutes", "25 minutes", "30 minutes", "1 hours", "2 hours", "3 hours"]
Combo1 = ttk.Combobox()
Combo1["values"] = (combolist)
Combo1.current(0)
Combo1.place(x=13, y=300)

# Base button
But = Button(text="Start", width=20, background="red", fg="black", command=select_time)
But.place(x=9, y=340)

# Label from time
LabelTime = tkinter.StringVar()
LabelT = Label(Main, textvariable=LabelTime)
LabelT.place(x=200, y=300)

# Label from tiber
LabelTimer = tkinter.StringVar()
LabelTimer1 = Label(Main, textvariable=LabelTimer)
LabelTimer1.place(x=250, y=320)

# Frames
Frame1 = Frame(Main, width=1000,  background="black")
Frame1.place(x=0, y=180)




Main.mainloop()