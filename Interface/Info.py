
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os
def Info():
    os.system('Info.py')
def search():
    os.system('search.py')

def Stat():
    os.system('Stat.py')

def submit():
    # take values from the form and put em into variables
    Aid= int(A_id.get())
    Afname = str(A_fname.get())
    Alname = str(A_lname.get())

    try:
        # create connection
        conn = cx_Oracle.connect('SYSTEM/SYSTEM@//localhost:1521/xe')
        print('Connection to database established')
    except Exception as err:
        print('Connection failed', err)
    # create cursor to be able to execute queries stored within variables
    cur = conn.cursor()
    # calling function and inputting
    try:
        # cursor to call procedure
        cur.callproc('insert_admin', (Aid, Afname, Alname))
        print('Values Inserted')
        messagebox.showinfo("success", "Values inserted")
    except Exception as err:
        messagebox.showinfo("Failure", err)

def update():
    # take values from the form and put em into variables
    # Student table
    Aid = A_id.get()
    Afname = A_fname.get()
    Alast = A_lname.get()

    try:
            # create connection
            conn = cx_Oracle.connect('SYSTEM/SYSTEM@//localhost:1521/xe')
            print('Connection to database established')
    except Exception as err:
            print('Connection failed', err)
        # create cursor to be able to execute queries stored within variables
    cur = conn.cursor()

    ##update Student
    if Aid != "":
        cur.callproc('update_admin',(int(Aid),Afname,Alast))
        messagebox.showinfo("success","admin updated")



def delete():
    # take values from the form and put em into variables
    # Student id

    Aid = A_id.get()

    try:
        # create connection
        conn = cx_Oracle.connect('SYSTEM/SYSTEM@//localhost:1521/xe')
        print('Connection to database established')
    except Exception as err:
        print('Connection failed', err)
    # create cursor to be able to execute queries stored within variables
    curs = conn.cursor()
    # calling function and inputting
    try:
            if Aid != "":
                curs.callproc('delete_admin', (int(Aid),))
                messagebox.showinfo("success","admin deleted")
    except Exception as err:
        print('error', err)
        messagebox.showinfo("failure",err)

window=Tk()

#SET TITLE
window.title('Administration ')

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





F2=Frame(window,bg="Ghost white",width=500)
F2.place(x=450,y=200)

# labels for the entry boxes
A_id_label = Label(F2, text="ID:",fg='cadet blue',bg='ghost white')
A_id_label.grid(row=0, column=0)
A_fname_label = Label(F2, text="First name:",fg='cadet blue',bg='ghost white')
A_fname_label.grid(row=1, column=0)
A_lname_label = Label(F2, text="Last name : ",fg='cadet blue',bg='ghost white')
A_lname_label.grid(row=2, column=0)


# creating text boxes for input on the GUI
A_id = Entry(F2, width=30)
# grid places the entry box on the interface in a specific position
A_id.grid(row=0, column=1,pady=20)
# creating text boxes for input on the GUI
A_fname = Entry(F2, width=30)
# grid places the entry box on the interface in a specific position
A_fname.grid(row=1, column=1,pady=20)
#
A_lname = Entry(F2, width=30)
A_lname.grid(row=2, column=1,pady=20)

# Creation of the insert button
insert = Button(F2, text="Insert ", command=submit,fg='white',bg='cadet blue')
insert.grid(row=6, column=0,  padx=10, ipadx=30)
# Creation of the update button
up = Button(F2, text="Update", command=update,fg='white',bg='cadet blue')
up.grid(row=6, column=1, padx=10, ipadx=30)
# Creation of the delete button
dele = Button(F2, text="Delete", command=delete,fg='white',bg='cadet blue')
dele.grid(row=6, column=2, padx=10, ipadx=30)
window.mainloop()
