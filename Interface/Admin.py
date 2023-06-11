# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os
def Control():
    os.system('Control.py')
def Info():
    os.system('Info.py')
def search():
    os.system('search.py')

def Stat():
    os.system('Stat.py')

window=Tk()

#SET TITLE
window.title('Admin info ')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# STYLE THE TITLE Student database
Title=Label(window, text='Administration Management System', bd=1, relief=GROOVE ,font=('times new roman',35,'bold'),bg="Ghost White",fg='cadet Blue')
Title.pack(side=TOP,fill=X) #TITLE POSITION


frame=Frame(window,bg='Ghost white',height=1000,width=500)
frame.place(x=450,y=100)


bt=Button(frame,text='Info',command=Info,width=20,bg='light blue')
bt.grid(column=0,row=0)

bt1=Button(frame,text='Search',width=20,bg='light blue',command=search)
bt1.grid(row=0,column=1)

bt2=Button(frame,text='Statistics',command=Stat,width=20,bg='light blue')
bt2.grid(row=0,column=2)

bt3=Button(frame,text='Control',command=Control,width=20,bg='light blue')
bt3.grid(row=0,column=3)



window.mainloop()
