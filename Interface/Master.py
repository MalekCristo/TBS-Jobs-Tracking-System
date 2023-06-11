
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os


window=Tk()

#SET TITLE
window.title('Master Degree')

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

lbl=Label(DataEntry, text='Percentage of Master Students', bg='Ghost white',fg='green', font=("times new york",15))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Percentage %",""))

Student_table.heading("Percentage %",text="Percentage %")
Student_table.heading("",text="")



Student_table['show']='headings'
Student_table.column("Percentage %",width=10)
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
    x = curs.callfunc('Master_students', float, (1,))
    Student_table.insert('', END, values=round(x))
except Exception as err:
    print('error', err)



#Frame 2
DataEntry2=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry2.place(x=360,y=5, width=350,height=200)

#Frame of the table
Tab2=Frame(DataEntry2,bd=4,relief=RIDGE,bg='green')
Tab2.place(x=10,y=30,width=300,height=150)

lbl2=Label(DataEntry2, text='Number Of Master Students Per Gender', bg='Ghost white',fg='green', font=("times new york",13))
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
    curs.execute("select sex,COUNT(Stud3) from  Student, Career WHERE Student.noStudent=Career.Stud3 AND situation='Master Student' GROUP BY sex")
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

lbl3=Label(DataEntry3, text='Master Students in TBS %', bg='Ghost white',fg='green', font=("times new york",15))
lbl3.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table3=ttk.Treeview(Tab3,column=("Percentage",""))

Student_table3.heading("Percentage",text="Percentage")
Student_table3.heading("",text="")



Student_table3['show']='headings'
Student_table3.column("Percentage",width=10)
Student_table3.column("",width=10)

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
    y = curs.callfunc('Master_students_tbs', float, (1,))
    Student_table3.insert('', END, values=round(y))
except Exception as err:
    print('error', err)



#Frame 5

DataEntry5=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry5.place(x=5,y=230, width=350,height=200)

#Frame of the table
Tab5=Frame(DataEntry5,bd=4,relief=RIDGE,bg='green')
Tab5.place(x=10,y=30,width=300,height=150)

lbl5=Label(DataEntry5, text='Masters At TBS And Registered students in each', bg='Ghost white',fg='green', font=("times new york",12))
lbl5.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table5=ttk.Treeview(Tab5,column=("Master","Total Number","Major","Gender"))

Student_table5.heading("Master",text="Master")
Student_table5.heading("Total Number",text="Total Number")
Student_table5.heading("Major",text="Major")
Student_table5.heading("Gender",text="Gender")

Student_table5['show']='headings'
Student_table5.column("Master",width=10)
Student_table5.column("Total Number",width=10)
Student_table5.column("Major",width=10)
Student_table5.column("Gender",width=10)
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
    curs.execute("Select Distinct(domain), COUNT(IDcareer),major,sex FROM  Career, Diploma,Student WHERE Student.noStudent=Career.Stud3 AND Career.Stud3=Diploma.Stud1 AND situation='Master Student' AND (city='TBS'  OR city='Tunis Business School' OR UPPER(city)='BEN AROUS' ) GROUP BY domain,major,sex ")
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

lbl6=Label(DataEntry6, text='Masters in Tunisia But Not in TBS %', bg='Ghost white',fg='green', font=("times new york",13))
lbl6.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table6=ttk.Treeview(Tab6,column=("Percentage",""))

Student_table6.heading("Percentage",text="Percentage")
Student_table6.heading("",text="")




Student_table6['show']='headings'
Student_table6.column("Percentage",width=10)
Student_table6.column("",width=10)


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
    z=curs.callfunc('Master_students_tun', float, (1,))
    Student_table6.insert('', END, values=round(z))
except Exception as err:
    print('error', err)

#Frame 7

DataEntry7=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry7.place(x=720,y=230, width=350,height=200)

#Frame of the table
Tab7=Frame(DataEntry7,bd=4,relief=RIDGE,bg='green')
Tab7.place(x=10,y=30,width=300,height=150)

lbl7=Label(DataEntry7, text='Masters in Tunisia TBSers Apply For', bg='Ghost white',fg='green', font=("times new york",13))
lbl7.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table7=ttk.Treeview(Tab7,column=("Masters","Major","Number","Location"))


Student_table7.heading("Masters",text="Masters")
Student_table7.heading("Major",text="Major")
Student_table7.heading("Number",text="Number")
Student_table7.heading("Location",text="Location")

Student_table7['show']='headings'
Student_table7.column("Masters",width=10)
Student_table7.column("Major",width=10)
Student_table7.column("Number",width=10)
Student_table7.column("Location",width=10)


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

    curs.execute("Select DISTINCT(domain),major,COUNT(Stud1),city FROM  Career, Diploma WHERE Career.Stud3=Diploma.Stud1 AND situation='Master Student' AND (city LIKE '%Carthage%' OR UPPER(city) LIKE '%TUNIS%' OR city LIKE '%tunisia%')  GROUP BY domain,major,city")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table7.insert('', END, values=row)


except Exception as err:
    print('error', err)

#Frame 8

DataEntry8=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry8.place(x=5,y=440, width=350,height=200)

#Frame of the table
Tab8=Frame(DataEntry8,bd=4,relief=RIDGE,bg='green')
Tab8.place(x=10,y=30,width=300,height=150)

lbl8=Label(DataEntry8, text='Masters Abroad %', bg='Ghost white',fg='green', font=("times new york",13))
lbl8.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table8=ttk.Treeview(Tab8,column=("Percentage",""))


Student_table8.heading("Percentage",text="Percentage")
Student_table8.heading("",text="")




Student_table8['show']='headings'
Student_table8.column("Percentage",width=10)
Student_table8.column("",width=10)


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
    t = curs.callfunc('Master_students_abroad', float, (1,))
    Student_table8.insert('', END, values=round(t))

except Exception as err:
    print('error', err)


#Frame 9

DataEntry9=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry9.place(x=360,y=440, width=350,height=200)

#Frame of the table
Tab9=Frame(DataEntry9,bd=4,relief=RIDGE,bg='green')
Tab9.place(x=10,y=30,width=300,height=150)

lbl9=Label(DataEntry9, text='Masters Abroad TBSers Apply For', bg='Ghost white',fg='green', font=("times new york",13))
lbl9.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table9=ttk.Treeview(Tab9,column=("Masters","Major","Number","Location"))


Student_table9.heading("Masters",text="Masters")
Student_table9.heading("Major",text="Major")
Student_table9.heading("Number",text="Number")
Student_table9.heading("Location",text="Location")



Student_table9['show']='headings'
Student_table9.column("Masters",width=10)
Student_table9.column("Major",width=10)
Student_table9.column("Number",width=10)
Student_table9.column("Location",width=10)

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
    curs.execute("Select DISTINCT(domain),major,COUNT(Stud1),city FROM  Career, Diploma WHERE Career.Stud3=Diploma.Stud1 AND situation='Master Student' AND city NOT IN ('Tunis', 'tunisia', 'Ben Arous','Ariana','ISG Tunis','TBS','Tunis Business School','Ihec Carthage','Carthage', 'Manouba','hay el ghazela' ) AND city NOT LIKE '%tunisia%' AND city IS NOT NULL  GROUP BY domain,major,city ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table9.insert('', END, values=row)

except Exception as err:
    print('error', err)



#Frame 10

DataEntry10=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry10.place(x=720,y=440, width=350,height=200)

#Frame of the table
Tab10=Frame(DataEntry10,bd=4,relief=RIDGE,bg='green')
Tab10.place(x=10,y=30,width=300,height=150)

lbl10=Label(DataEntry10, text='Number Of Employed Master Students', bg='Ghost white',fg='green', font=("times new york",13))
lbl10.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table10=ttk.Treeview(Tab10,column=("Total Number",""))


Student_table10.heading("Total Number",text="Total Number")
Student_table10.heading("",text="")




Student_table10['show']='headings'
Student_table10.column("Total Number",width=10)
Student_table10.column("",width=10)


Student_table10.pack(fill=BOTH,expand=1)



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
    f=curs.callfunc('working_and_studying', float, (1,))
    Student_table10.insert('', END, values=round(f))

except Exception as err:
    print('error', err)


#Frame 11

DataEntry11=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry11.place(x=1075,y=440, width=260,height=200)

#Frame of the table
Tab11=Frame(DataEntry11,bd=4,relief=RIDGE,bg='green')
Tab11.place(x=10,y=30,width=230,height=150)

lbl11=Label(DataEntry11, text='Employed Master Students Salaries', bg='Ghost white',fg='green', font=("times new york",11))
lbl11.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table11=ttk.Treeview(Tab11,column=("Student","Situation","Salary Range"))

Student_table11.heading("Student",text="Student")
Student_table11.heading("Situation",text="Situation")
Student_table11.heading("Salary Range",text="Salary Range")




Student_table11['show']='headings'
Student_table11.column("Student",width=10)
Student_table11.column("Situation",width=10)
Student_table11.column("Salary Range",width=10)


Student_table11.pack(fill=BOTH,expand=1)



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
    curs.execute("SELECT distinct(Stud3),situation,salary FROM Career , Diploma WHERE Career.Stud3=Diploma.Stud1 AND salary IS NOT NULL AND (situation='Master Student' AND hiring_date IS NOT NULL) OR situation='Alternate' OR situation='Part time employee' ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table11.insert('', END, values=row)
except Exception as err:
    print('error', err)

window.mainloop()
