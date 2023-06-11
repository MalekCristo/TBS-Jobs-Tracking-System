import tkinter.font as font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os

def Check ():
    idd= int(id.get())
    pas= passw.get()
    if (idd==1) & (pas=='12345'):
        os.system('Admin.py')
    else:
        messagebox.showinfo('Error','Something went wrong')


window = Tk()
window.title("Welcome")
window.config(bg='cadet blue')
window.geometry("1350x850+0+0")
wel = Label(window, text="Welcome", font=('Times',70))
wel.config(background="cadet blue")
wel.place(x=500, y=130, )
wel1 = Label(window, text="please insert your ",font=('Times',65))
wel1.config(background="cadet blue")
wel1.place(x=370, y=230 )
wel1 = Label(window, text="ID and password below",font=('Times',65))
wel1.config(background="cadet blue")
wel1.place(x=260, y=330 )
id = Entry(window, width=40)
id.place(x=550, y=450)
passw = Entry(window, width=40)
passw.place(x=550, y=520)
submit = Button(window, text="submit", width=40, command=Check)
submit.place(x=580, y=590)
submit.configure(bg='Ghost white', height=1, width=10, font=('Times', 11))
window.mainloop()