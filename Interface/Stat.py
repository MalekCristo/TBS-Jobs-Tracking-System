
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os

def general():
    os.system('General.py')
def Master():
    os.system('Master.py')
def jobs():
    os.system('Jobs.py')
def salaries():
    os.system('Salaries.py')
def internship():
    os.system('Internships.py')

window=Tk()

#SET TITLE
window.title('Statistics ')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# STYLE THE TITLE Student database
Title=Label(window, text='Choose Topic For statistics', bd=1, relief=GROOVE ,font=('times new roman',35,'bold'),bg="Ghost White",fg='cadet Blue')
Title.pack(side=TOP,fill=X) #TITLE POSITION

#Frame 1
DataEntry=Frame(window,bg='Cadet Blue', relief=GROOVE, borderwidth=5 )
DataEntry.place(x=500,y=200, width=350,height=350)

General_info = Button(DataEntry, text="General Info", bg='light blue',command=general, width=40)
General_info.grid(row=0, column=0, columnspan=2, padx=20, ipadx=10,pady=25)

Internship_off = Button(DataEntry, text="Internship Offers", bg='light blue',command=internship, width=40)
Internship_off.grid(row=1, column=0, columnspan=2, padx=20, ipadx=10,pady=22)

Job_off = Button(DataEntry, text="Job Offers", bg='light blue',command=jobs, width=40)
Job_off.grid(row=2, column=0, columnspan=2, padx=20, ipadx=10,pady=22)

Salaries = Button(DataEntry, text="Salaries", bg='light blue',command=salaries, width=40)
Salaries.grid(row=3, column=0, columnspan=2, padx=20, ipadx=10,pady=22)

Master_stu = Button(DataEntry, text="Master", bg='light blue',command=Master, width=40)
Master_stu.grid(row=4, column=0, columnspan=2, padx=20, ipadx=10,pady=22)




window.mainloop()
