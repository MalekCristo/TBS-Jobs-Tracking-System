
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os


window=Tk()

#SET TITLE
window.title('General Info')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# CREATE FRAMES
#Frame 1
DataEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry.place(x=5,y=5, width=350,height=200)

#Frame of the table
Tab=Frame(DataEntry,bd=4,relief=RIDGE,bg='green')
Tab.place(x=10,y=30,width=300,height=150)

lbl=Label(DataEntry, text='Total Number of Registerd Students', bg='Ghost white',fg='green', font=("times new york",15))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Total Number",""))

Student_table.heading("Total Number",text="Total Number")
Student_table.heading("",text="")



Student_table['show']='headings'
Student_table.column("Total Number",width=10)
Student_table.column("",width=10)

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
    curs.execute("select COUNT(noStudent) from Student")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table.insert('', END, values=row)

except Exception as err:
    print('error', err)



#Frame 2
DataEntry2=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry2.place(x=360,y=5, width=350,height=200)

#Frame of the table
Tab2=Frame(DataEntry2,bd=4,relief=RIDGE,bg='green')
Tab2.place(x=10,y=30,width=300,height=150)

lbl2=Label(DataEntry2, text='Registerd Students Per Gender', bg='Ghost white',fg='green', font=("times new york",15))
lbl2.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table2=ttk.Treeview(Tab2,column=("Gender","Total Number"))

Student_table2.heading("Gender",text="Gender")
Student_table2.heading("Total Number",text="Total Number")




Student_table2['show']='headings'
Student_table2.column("Gender",width=10)
Student_table2.column("Total Number",width=10)


Student_table2.pack(fill=BOTH,expand=1)



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
    curs.execute("select sex,COUNT(noStudent) from  Student GROUP BY sex")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table2.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 3

DataEntry3=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry3.place(x=720,y=5, width=350,height=200)

#Frame of the table
Tab3=Frame(DataEntry3,bd=4,relief=RIDGE,bg='green')
Tab3.place(x=10,y=30,width=300,height=150)

lbl3=Label(DataEntry3, text='Students Per Major', bg='Ghost white',fg='green', font=("times new york",15))
lbl3.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table3=ttk.Treeview(Tab3,column=("Major","Total Number"))

Student_table3.heading("Major",text="Major")
Student_table3.heading("Total Number",text="Total Number")



Student_table3['show']='headings'
Student_table3.column("Major",width=10)
Student_table3.column("Total Number",width=10)

Student_table3.pack(fill=BOTH,expand=1)



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
    curs.execute("select major,COUNT(Stud1) from Diploma GROUP BY major")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table3.insert('', END, values=row)

except Exception as err:
    print('error', err)



#Frame 5

DataEntry5=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry5.place(x=5,y=230, width=350,height=200)

#Frame of the table
Tab5=Frame(DataEntry5,bd=4,relief=RIDGE,bg='green')
Tab5.place(x=10,y=30,width=300,height=150)

lbl5=Label(DataEntry5, text='Students Per Minor', bg='Ghost white',fg='green', font=("times new york",15))
lbl5.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table5=ttk.Treeview(Tab5,column=("Minor","Total Number"))

Student_table5.heading("Minor",text="Minor")
Student_table5.heading("Total Number",text="Total Number")



Student_table5['show']='headings'
Student_table5.column("Minor",width=10)
Student_table5.column("Total Number",width=10)

Student_table5.pack(fill=BOTH,expand=1)



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
    curs.execute("select minor,COUNT(Stud1) from Diploma GROUP BY minor")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table5.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 6

DataEntry6=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry6.place(x=360,y=230, width=350,height=200)

#Frame of the table
Tab6=Frame(DataEntry6,bd=4,relief=RIDGE,bg='green')
Tab6.place(x=10,y=30,width=300,height=150)

lbl6=Label(DataEntry6, text='Major Per Gender', bg='Ghost white',fg='green', font=("times new york",15))
lbl6.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table6=ttk.Treeview(Tab6,column=("Major","Gender","Total Number"))

Student_table6.heading("Major",text="Major")
Student_table6.heading("Gender",text="Gender")
Student_table6.heading("Total Number",text="Total Number")



Student_table6['show']='headings'
Student_table6.column("Major",width=10)
Student_table6.column("Gender",width=10)
Student_table6.column("Total Number",width=10)

Student_table6.pack(fill=BOTH,expand=1)



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
    curs.execute("select major,sex,COUNT(Stud1) from Diploma,Student WHERE Student.noStudent=Diploma.Stud1 GROUP BY major,sex")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table6.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 7

DataEntry7=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry7.place(x=720,y=230, width=350,height=200)

#Frame of the table
Tab7=Frame(DataEntry7,bd=4,relief=RIDGE,bg='green')
Tab7.place(x=10,y=30,width=300,height=150)

lbl7=Label(DataEntry7, text='Late Graduates (more than 4years)', bg='Ghost white',fg='green', font=("times new york",13))
lbl7.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table7=ttk.Treeview(Tab7,column=("Late graduates",""))


Student_table7.heading("Late graduates",text="Late Graduates")
Student_table7.heading("",text="")


Student_table7['show']='headings'
Student_table7.column("Late graduates",width=10)
Student_table7.column("",width=10)

Student_table7.pack(fill=BOTH,expand=1)



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

    x=curs.callfunc('late_grad',float,(1,))
    Student_table7.insert('',END, values=round(x))

except Exception as err:
    print('error', err)

#Frame 8

DataEntry8=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry8.place(x=5,y=440, width=350,height=200)

#Frame of the table
Tab8=Frame(DataEntry8,bd=4,relief=RIDGE,bg='green')
Tab8.place(x=10,y=30,width=300,height=150)

lbl8=Label(DataEntry8, text='Late Graduates By Major AND Gender', bg='Ghost white',fg='green', font=("times new york",13))
lbl8.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table8=ttk.Treeview(Tab8,column=("Major","Gender","Late graduates"))


Student_table8.heading("Major",text="Major")
Student_table8.heading("Gender",text="Gender")
Student_table8.heading("Late graduates",text="Late Graduates")



Student_table8['show']='headings'
Student_table8.column("Major",width=10)
Student_table8.column("Gender",width=10)
Student_table8.column("Late graduates",width=10)


Student_table8.pack(fill=BOTH,expand=1)



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
    curs.execute("Select  major,sex,Count(Stud1) FROM  Diploma,Student WHERE round((grad_date-start_date)/365)>4 AND Student.noStudent=Diploma.noDiploma GROUP BY major,sex")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table8.insert('', END, values=row)

except Exception as err:
    print('error', err)


#Frame 9

DataEntry9=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry9.place(x=360,y=440, width=350,height=200)

#Frame of the table
Tab9=Frame(DataEntry9,bd=4,relief=RIDGE,bg='green')
Tab9.place(x=10,y=30,width=300,height=150)

lbl9=Label(DataEntry9, text='Students Currently Living Abroad ', bg='Ghost white',fg='green', font=("times new york",13))
lbl9.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table9=ttk.Treeview(Tab9,column=("noStudent","Name","City"))


Student_table9.heading("noStudent",text="Student ID")
Student_table9.heading("Name",text="Name")
Student_table9.heading("City",text="City")



Student_table9['show']='headings'
Student_table9.column("noStudent",width=10)
Student_table9.column("Name",width=10)
Student_table9.column("City",width=10)


Student_table9.pack(fill=BOTH,expand=1)



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
    curs.execute("Select  noStudent,fname,Address FROM  Student WHERE (phone_num IS NOT NULL AND length(TO_CHAR(phone_num))>8) OR (Address NOT LIKE '%Tunis%' AND Address NOT LIKE '%Tunisia%' ) ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table9.insert('', END, values=row)

except Exception as err:
    print('error', err)


window.mainloop()
