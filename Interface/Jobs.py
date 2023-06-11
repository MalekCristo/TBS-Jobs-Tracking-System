
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os

def search():
    # take values from search bar and put em into variables

    maj = combo_search.get()
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
        curs.execute("SELECT domain FROM Diploma, Career WHERE Diploma.Stud1=Career.Stud3 AND (situation='Employee' OR situation='Alternate' OR situation='Part time employee' )AND hiring_date IS NOT NULL AND domain != 'None' AND major LIKE '%" + str(maj) + "%'")
        rows = curs.fetchall()
        if len(rows) != 0:
            for row in rows:
                Student_table7.insert('', END, values=row)
        else:
            messagebox.showinfo("Error", "Data not found")


    except Exception as err:
        print('error', err)
window=Tk()

#SET TITLE
window.title('Jobs Info')

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

lbl=Label(DataEntry, text='Percentage of Hired Students', bg='Ghost white',fg='green', font=("times new york",15))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Percentage",""))

Student_table.heading("Percentage",text="Percentage")
Student_table.heading("",text="")



Student_table['show']='headings'
Student_table.column("Percentage",width=10)
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
    x = curs.callfunc('AVG_hired_student', float, (1,))
    Student_table.insert('', END, values=round(x))


except Exception as err:
    print('error', err)


#Frame x
DataEntryx=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntryx.place(x=1070,y=5, width=300,height=200)

#Frame of the table
Tabx=Frame(DataEntryx,bd=4,relief=RIDGE,bg='green')
Tabx.place(x=10,y=30,width=250,height=150)

lblx=Label(DataEntryx, text='Average Hired Students By Speciality And Gender', bg='Ghost white',fg='green', font=("times new york",9))
lblx.grid(row=0,column=1,sticky="w")
#Define table columns
Student_tablex=ttk.Treeview(Tabx,column=("Gender","Speciality","Average"))

Student_tablex.heading("Gender",text="Gender")
Student_tablex.heading("Speciality",text="Speciality")
Student_tablex.heading("Average",text="Average")




Student_tablex['show']='headings'
Student_tablex.column("Gender",width=10)
Student_tablex.column("Speciality",width=10)
Student_tablex.column("Average",width=10)


Student_tablex.pack(fill=BOTH,expand=1)



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
    curs.execute("Select sex, major,COUNT(IDcareer) FROM  Career, Student, Diploma WHERE Student.noStudent=Diploma.Stud1 AND Student.noStudent=Career.Stud3 AND (situation='Employee' OR hiring_date IS NOT NULL) GROUP BY sex,major")
    rows = curs.fetchall()

    if len(rows) != 0:
        for row in rows:
            Student_tablex.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 2
DataEntry2=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry2.place(x=360,y=5, width=350,height=200)

#Frame of the table
Tab2=Frame(DataEntry2,bd=4,relief=RIDGE,bg='green')
Tab2.place(x=10,y=30,width=300,height=150)

lbl2=Label(DataEntry2, text='Number Of Business Owners', bg='Ghost white',fg='green', font=("times new york",15))
lbl2.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table2=ttk.Treeview(Tab2,column=("Gender","Speciality","Total Number"))

Student_table2.heading("Gender",text="Gender")
Student_table2.heading("Speciality",text="Speciality")
Student_table2.heading("Total Number",text="Total Number")




Student_table2['show']='headings'
Student_table2.column("Gender",width=10)
Student_table2.column("Speciality",width=10)
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
    curs.execute("Select sex, major,COUNT(IDcareer) FROM  Career, Student, Diploma WHERE Student.noStudent=Diploma.Stud1 AND Student.noStudent=Career.Stud3 AND situation='Business Owner' GROUP BY sex,major")
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

lbl3=Label(DataEntry3, text='Average Waiting Time Before Getting Hired', bg='Ghost white',fg='green', font=("times new york",11))
lbl3.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table3=ttk.Treeview(Tab3,column=("Average",""))

Student_table3.heading("Average",text="Average(months)")
Student_table3.heading("",text="")



Student_table3['show']='headings'
Student_table3.column("Average",width=10)
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
    y = curs.callfunc('avg_waiting_time', float, (1,))
    Student_table3.insert('', END, values=round(y))
except Exception as err:
    print('error', err)



#Frame 5

DataEntry5=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry5.place(x=5,y=230, width=350,height=200)

#Frame of the table
Tab5=Frame(DataEntry5,bd=4,relief=RIDGE,bg='green')
Tab5.place(x=10,y=30,width=300,height=150)

lbl5=Label(DataEntry5, text='Average Waiting Time By major and Gender', bg='Ghost white',fg='green', font=("times new york",12))
lbl5.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table5=ttk.Treeview(Tab5,column=("Major","gender","Average"))

Student_table5.heading("Major",text="Major")
Student_table5.heading("gender",text="gender")
Student_table5.heading("Average",text="Average")



Student_table5['show']='headings'
Student_table5.column("Major",width=10)
Student_table5.column("gender",width=10)
Student_table5.column("Average",width=10)

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
    curs.execute("Select major, sex, round(AVG((hiring_date-grad_date)/30)) FROM Student, Diploma, Career WHERE Student.noStudent=Diploma.stud1 AND Student.noStudent=Career.stud3 AND  hiring_date IS NOT NULL GROUP BY major, sex")
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

lbl6=Label(DataEntry6, text='Students Hired Even Before Grad', bg='Ghost white',fg='green', font=("times new york",11))
lbl6.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table6=ttk.Treeview(Tab6,column=("Major","Gender","Average"))

Student_table6.heading("Major",text="Major")
Student_table6.heading("Gender",text="Gender")
Student_table6.heading("Average",text="Total Number")



Student_table6['show']='headings'
Student_table6.column("Major",width=10)
Student_table6.column("Gender",width=10)
Student_table6.column("Average",width=10)

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
    curs.execute("Select major, sex,COUNT(noStudent) FROM Student, Diploma, Career WHERE Student.noStudent=Diploma.stud1 AND Student.noStudent=Career.stud3  AND hiring_date IS NOT NULL AND round((hiring_date-grad_date)/30)<0 GROUP BY major,sex")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table6.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 7
DataEntry7=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry7.place(x=720,y=230, width=350,height=200)

lbl7=Label(DataEntry7, text='Working Domains', bg='Ghost white',fg='green', font=("times new york",15))
lbl7.grid(row=0,column=0,sticky="w")


#Criteria to choose from

combo_search=ttk.Combobox(DataEntry7,font=("times new york",7,"bold"),width=20,state='readonly')
combo_search["values"]=('BA','Finance','Marketing','IT','Accounting','IPE')
combo_search.grid(row=1,column=0,padx=2)

#search btn

search = Button(DataEntry7, text="Go",bg='light blue', command=search)
search.grid(row=1, column=1, padx=5, ipadx=5)

#Frame of the table
Tab7=Frame(DataEntry7,bd=4,relief=RIDGE,bg='green')
Tab7.place(x=10,y=50,width=300,height=120)

#Define table columns
Student_table7=ttk.Treeview(Tab7,column=("Domain",""))


Student_table7.heading("Domain",text="Domain")
Student_table7.heading("",text="")

Student_table7['show']='headings'
Student_table7.column("Domain",width=80)
Student_table7.column("",width=80)
Student_table7.pack(fill=BOTH,expand=1)
#Frame 8

DataEntry8=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry8.place(x=5,y=440, width=350,height=200)

#Frame of the table
Tab8=Frame(DataEntry8,bd=4,relief=RIDGE,bg='green')
Tab8.place(x=10,y=30,width=300,height=150)

lbl8=Label(DataEntry8, text='Working Offers', bg='Ghost white',fg='green', font=("times new york",13))
lbl8.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table8=ttk.Treeview(Tab8,column=("Comapny/city","major"))


Student_table8.heading("Comapny/city",text="Comapny/city")
Student_table8.heading("major",text="major")



Student_table8['show']='headings'
Student_table8.column("Comapny/city",width=10)
Student_table8.column("major",width=10)


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
    curs.execute("Select city,major FROM  Diploma, Career WHERE Diploma.stud1=Career.stud3  AND situation='Employee' ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table8.insert('', END, values=row)

except Exception as err:
    print('error', err)


window.mainloop()
