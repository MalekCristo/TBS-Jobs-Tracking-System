
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os


def clear():
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

        curs.callproc("del_stud",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

def clear2():
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

        curs.callproc("del_dip",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

def clear3():
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

        curs.callproc("del_career",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)


def clear4():
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

        curs.callproc("del_internship",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

def clear5():
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

        curs.callproc("up_stud",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)
def clear6():
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

        curs.callproc("up_dip",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

def clear8():
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

        curs.callproc("up_internship",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

def clear9():
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

        curs.callproc("up_career",(1,))
        messagebox.showinfo('success', 'values deleted')
    except Exception as err:
        print('error', err)

window=Tk()

#SET TITLE
window.title('Control Tables')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# CREATE FRAMES
#Frame 1
DataEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry.place(x=5,y=5, width=350,height=350)

#Frame of the table
Tab=Frame(DataEntry,bd=4,relief=RIDGE,bg='green')
Tab.place(x=10,y=70,width=300,height=250)

lbl=Label(DataEntry, text='Deleted Students', bg='Ghost white',fg='green', font=("times new york",18))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Sysdate","ID","first_name","last_name"))

Student_table.heading("Sysdate",text="Sysdate")
Student_table.heading("ID",text="ID")
Student_table.heading("first_name",text="first_name")
Student_table.heading("last_name",text="last_name")


Student_table['show']='headings'
Student_table.column("Sysdate",width=10)
Student_table.column("ID",width=10)
Student_table.column("first_name",width=10)
Student_table.column("last_name",width=10)

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
    curs.execute("select * FROM del_info_stud ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table.insert('', END, values=row)


except Exception as err:
    print('error', err)


clear = Button(DataEntry, text="Clear", bg='light blue',command=clear)
clear.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)


#Frame 2
DataEntry2=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry2.place(x=360,y=5, width=350,height=350)

#Frame of the table
Tab2=Frame(DataEntry2,bd=4,relief=RIDGE,bg='green')
Tab2.place(x=10,y=70,width=300,height=250)

lbl2=Label(DataEntry2, text='Deleted Diplomas', bg='Ghost white',fg='green', font=("times new york",18))
lbl2.grid(row=0,column=1,sticky="w")
#Define table columns
Diploma_table=ttk.Treeview(Tab2,column=("Sysdate","ID","student_ID","Diploma"))

Diploma_table.heading("Sysdate",text="Sysdate")
Diploma_table.heading("ID",text="ID")
Diploma_table.heading("student_ID",text="student_ID")
Diploma_table.heading("Diploma",text="Diploma")


Diploma_table['show']='headings'
Diploma_table.column("Sysdate",width=10)
Diploma_table.column("ID",width=10)
Diploma_table.column("student_ID",width=10)
Diploma_table.column("Diploma",width=10)

Diploma_table.pack(fill=BOTH,expand=1)

clear2 = Button(DataEntry2, text="Clear", bg='light blue',command=clear2)
clear2.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)

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
    curs.execute("select * FROM del_info_dip ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Diploma_table.insert('', END, values=row)


except Exception as err:
    print('error', err)




#Frame 3
DataEntry3=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry3.place(x=710,y=5, width=350,height=350)

#Frame of the table
Tab3=Frame(DataEntry3,bd=4,relief=RIDGE,bg='green')
Tab3.place(x=5,y=70,width=300,height=250)

lbl3=Label(DataEntry3, text='Deleted Careers', bg='Ghost white',fg='green', font=("times new york",18))
lbl3.grid(row=0,column=1,sticky="w")
#Define table columns
Career_table=ttk.Treeview(Tab3,column=("Sysdate","ID","student_ID","Situation","Domain"))

Career_table.heading("Sysdate",text="Sysdate")
Career_table.heading("ID",text="ID")
Career_table.heading("student_ID",text="student_ID")
Career_table.heading("Situation",text="Situation")
Career_table.heading("Domain",text="Domain")

Career_table['show']='headings'
Career_table.column("Sysdate",width=10)
Career_table.column("ID",width=10)
Career_table.column("student_ID",width=10)
Career_table.column("Situation",width=10)
Career_table.column("Domain",width=10)

Career_table.pack(fill=BOTH,expand=1)



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
    curs.execute("select * FROM del_info_career ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Career_table.insert('', END, values=row)


except Exception as err:
    print('error', err)

clear3 = Button(DataEntry3, text="Clear", bg='light blue',command=clear3)
clear3.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)


#Frame 7
DataEntry7=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry7.place(x=1050,y=5, width=350,height=350)

#Frame of the table
Tab7=Frame(DataEntry7,bd=4,relief=RIDGE,bg='green')
Tab7.place(x=5,y=70,width=300,height=250)

lbl7=Label(DataEntry7, text='Deleted Internships', bg='Ghost white',fg='green', font=("times new york",18))
lbl7.grid(row=0,column=1,sticky="w")
#Define table columns
Internship_table=ttk.Treeview(Tab7,column=("Sysdate","ID","student_ID","Host"))

Internship_table.heading("Sysdate",text="Sysdate")
Internship_table.heading("ID",text="ID")
Internship_table.heading("student_ID",text="student_ID")
Internship_table.heading("Host",text="Host")


Internship_table['show']='headings'
Internship_table.column("Sysdate",width=10)
Internship_table.column("ID",width=10)
Internship_table.column("student_ID",width=10)
Internship_table.column("Host",width=10)


Internship_table.pack(fill=BOTH,expand=1)



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
    curs.execute("select * FROM del_info_internship ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Internship_table.insert('', END, values=row)


except Exception as err:
    print('error', err)

clear7 = Button(DataEntry7, text="Clear", bg='light blue',command=clear4)
clear7.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)


#Frame 4
DataEntry4=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry4.place(x=5,y=360, width=350,height=350)

#Frame of the table
Tab4=Frame(DataEntry4,bd=4,relief=RIDGE,bg='green')
Tab4.place(x=10,y=70,width=300,height=250)

lbl4=Label(DataEntry4, text='Updated Students', bg='Ghost white',fg='green', font=("times new york",18))
lbl4.grid(row=0,column=1,sticky="w")
#Define table columns
upstud_table=ttk.Treeview(Tab4,column=("Sysdate","ID","first_name","last_name","gender","age","email","address","phone"))

upstud_table.heading("Sysdate",text="Sysdate")
upstud_table.heading("ID",text="ID")
upstud_table.heading("first_name",text="first_name")
upstud_table.heading("last_name",text="last_name")
upstud_table.heading("gender",text="gender")
upstud_table.heading("age",text="age")
upstud_table.heading("email",text="email")
upstud_table.heading("address",text="address")
upstud_table.heading("phone",text="phone")

upstud_table['show']='headings'
upstud_table.column("Sysdate",width=10)
upstud_table.column("ID",width=10)
upstud_table.column("first_name",width=10)
upstud_table.column("last_name",width=10)
upstud_table.column("gender",width=10)
upstud_table.column("age",width=10)
upstud_table.column("email",width=10)
upstud_table.column("address",width=10)
upstud_table.column("phone",width=10)

upstud_table.pack(fill=BOTH,expand=1)



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
    curs.execute("select * FROM up_info_stud ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            upstud_table.insert('', END, values=row)


except Exception as err:
    print('error', err)


clear4 = Button(DataEntry4, text="Clear", bg='light blue',command=clear5)
clear4.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)

#Frame 5
DataEntry5=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry5.place(x=360,y=360, width=350,height=350)

#Frame of the table
Tab5=Frame(DataEntry5,bd=4,relief=RIDGE,bg='green')
Tab5.place(x=10,y=70,width=300,height=250)

lbl5=Label(DataEntry5, text='Updated Diplomas', bg='Ghost white',fg='green', font=("times new york",18))
lbl5.grid(row=0,column=1,sticky="w")
#Define table columns
updip_table=ttk.Treeview(Tab5,column=("Sysdate","ID","student_ID","Diploma","university","major","minor","secmajmin","start","grad"))

updip_table.heading("Sysdate",text="Sysdate")
updip_table.heading("ID",text="ID")
updip_table.heading("student_ID",text="student_ID")
updip_table.heading("Diploma",text="Diploma")
updip_table.heading("major",text="major")
updip_table.heading("minor",text="minor")
updip_table.heading("secmajmin",text="secmajmin")
updip_table.heading("start",text="start")
updip_table.heading("grad",text="grad")

updip_table['show']='headings'
updip_table.column("Sysdate",width=10)
updip_table.column("ID",width=10)
updip_table.column("student_ID",width=10)
updip_table.column("Diploma",width=10)
updip_table.column("major",width=10)
updip_table.column("minor",width=10)
updip_table.column("secmajmin",width=10)
updip_table.column("start",width=10)
updip_table.column("grad",width=10)


updip_table.pack(fill=BOTH,expand=1)

#Clear button
clear5 = Button(DataEntry5, text="Clear", bg='light blue',command=clear6)
clear5.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)

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
    curs.execute("select * FROM up_info_dip ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            updip_table.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 6
DataEntry6=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry6.place(x=710,y=360, width=350,height=350)

#Frame of the table
Tab6=Frame(DataEntry6,bd=4,relief=RIDGE,bg='green')
Tab6.place(x=5,y=70,width=300,height=250)

lbl6=Label(DataEntry6, text='Updated Careers', bg='Ghost white',fg='green', font=("times new york",18))
lbl6.grid(row=0,column=1,sticky="w")
#Define table columns
upcareer_table=ttk.Treeview(Tab6,column=("Sysdate","ID","student_ID","Situation","Domain","hiring_date","leaving_date","city","salary","searchmean"))

upcareer_table.heading("Sysdate",text="Sysdate")
upcareer_table.heading("ID",text="ID")
upcareer_table.heading("student_ID",text="student_ID")
upcareer_table.heading("Situation",text="Situation")
upcareer_table.heading("Domain",text="Domain")
upcareer_table.heading("hiring_date",text="hiring_date")
upcareer_table.heading("leaving_date",text="leaving_date")
upcareer_table.heading("city",text="city")
upcareer_table.heading("searchmean",text="searchmean")


upcareer_table['show']='headings'
upcareer_table.column("Sysdate",width=10)
upcareer_table.column("ID",width=10)
upcareer_table.column("student_ID",width=10)
upcareer_table.column("Situation",width=10)
upcareer_table.column("Domain",width=10)
upcareer_table.column("hiring_date",width=10)
upcareer_table.column("leaving_date",width=10)
upcareer_table.column("city",width=10)
upcareer_table.column("searchmean",width=10)

upcareer_table.pack(fill=BOTH,expand=1)



clear6 = Button(DataEntry6, text="Clear", bg='light blue', command=clear9)
clear6.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)
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
    curs.execute("select * FROM up_info_career ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            upcareer_table.insert('', END, values=row)


except Exception as err:
    print('error', err)




#Frame 7
DataEntry8=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry8.place(x=1050,y=360, width=350,height=350)

#Frame of the table
Tab8=Frame(DataEntry8,bd=4,relief=RIDGE,bg='green')
Tab8.place(x=5,y=70,width=300,height=250)

lbl8=Label(DataEntry8, text='Updated Internships', bg='Ghost white',fg='green', font=("times new york",18))
lbl8.grid(row=0,column=1,sticky="w")
#Define table columns
upint_table=ttk.Treeview(Tab8,column=("Sysdate","ID","student_ID","number_int","Host","period"))

upint_table.heading("Sysdate",text="Sysdate")
upint_table.heading("ID",text="ID")
upint_table.heading("student_ID",text="student_ID")
upint_table.heading("number_int",text="number_int")
upint_table.heading("Host",text="Host")
upint_table.heading("period",text="period")

upint_table['show']='headings'
upint_table.column("Sysdate",width=10)
upint_table.column("ID",width=10)
upint_table.column("student_ID",width=10)
upint_table.column("number_int",width=10)
upint_table.column("Host",width=10)
upint_table.column("period",width=10)

upint_table.pack(fill=BOTH,expand=1)



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
    curs.execute("select * FROM up_info_internship ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            upint_table.insert('', END, values=row)


except Exception as err:
    print('error', err)

clear8 = Button(DataEntry8, text="Clear", bg='light blue',command=clear8)
clear8.grid(row=0, column=3, columnspan=2, padx=20, ipadx=10,pady=10)





window.mainloop()