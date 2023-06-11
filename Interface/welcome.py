import tkinter.font as font
from tkinter import *
import sys
import os
#create Font object

def ad():
    os.system('First_page.py')
def stud():
    os.system('Student_interface.py')


window = Tk()
window.title("Welcome")
window.config(bg='cadet blue')
window.geometry("1350x850+0+0")
wel = Label(window, text="Welcome", font=('Times',70))
wel.config(background="cadet blue")
wel.place(x=510, y=180, )
wel1 = Label(window, text="log in as",font=('Times',65))
wel1.config(background="cadet blue")
wel1.place(x=540, y=280 )
admin = Button(window, text="Admin",command=ad)
admin.place(x=610, y=410)
Student = Button(window, text="Student", command=stud)
Student.place(x=710, y=410)
admin.configure(bg='Ghost white', height=3, width=10, font=('Times', 11))
Student.configure(bg='Ghost white', height=3, width=10, font=('Times', 11))
window.mainloop()