
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os


window=Tk()

#SET TITLE
window.title('Salaries Info')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# CREATE FRAMES
#Frame 1
DataEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry.place(x=450,y=180, width=500,height=300)

#Frame of the table
Tab=Frame(DataEntry,bd=4,relief=RIDGE,bg='green')
Tab.place(x=10,y=30,width=450,height=250)

lbl=Label(DataEntry, text='Salary Ranges By Situation', bg='Ghost white',fg='green', font=("times new york",15))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Situation","Salary Range","Major"))

Student_table.heading("Situation",text="Situation")
Student_table.heading("Salary Range",text="Salary Range")
Student_table.heading("Major",text="Major")


Student_table['show']='headings'
Student_table.column("Situation",width=10)
Student_table.column("Salary Range",width=10)
Student_table.column("Major",width=10)
Student_table.pack(fill=BOTH,expand=1)



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
    curs.execute("select situation,salary,major  from Career, Diploma WHERE Career.Stud3=Diploma.Stud1 ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table.insert('', END, values=row)

except Exception as err:
    print('error', err)






window.mainloop()
