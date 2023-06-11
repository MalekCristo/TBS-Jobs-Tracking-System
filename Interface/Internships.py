
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
            curs.execute(
                "SELECT host_organization, COUNT(Stud2) FROM Diploma,Internship WHERE Internship.Stud2=Diploma.Stud1 AND host_organization IS NOT NULL AND host_organization!='None' AND host_organization!='Senior Project' AND host_organization!='Mini Senior Project' AND major LIKE '%" +str(maj) + "%' GROUP BY host_organization")
            rows = curs.fetchall()
            if len(rows) != 0:
                for row in rows:
                    Student_table6.insert('', END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found")


        except Exception as err:
            print('error', err)
window=Tk()

#SET TITLE
window.title('Internship Info')

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

lbl=Label(DataEntry, text='Percentage of hired Students', bg='Ghost white',fg='green', font=("times new york",13))
lbl.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table=ttk.Treeview(Tab,column=("Average","Minimum","Maximum"))

Student_table.heading("Average",text="Average")
Student_table.heading("Minimum",text="Minimum")
Student_table.heading("Maximum",text="Maximum")



Student_table['show']='headings'
Student_table.column("Average",width=10)
Student_table.column("Minimum",width=10)
Student_table.column("Maximum",width=10)

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
    curs.execute("select ROUND(AVG(num_int)),Min(num_int),Max(num_int) from Internship")
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

lbl2=Label(DataEntry2, text='Students Having Mini/Senior Projects(no PFE)', bg='Ghost white',fg='green', font=("times new york",12))
lbl2.grid(row=0,column=1,sticky="w")

#Define table columns
Student_table2=ttk.Treeview(Tab2,column=("Total Number",""))


Student_table2.heading("Total Number",text="Total Number")
Student_table2.heading("",text="")



Student_table2['show']='headings'
Student_table2.column("Total Number",width=10)
Student_table2.column("",width=10)

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
    curs.execute("select COUNT(Stud2) from Internship WHERE UPPER(host_organization)='SENIOR PROJECT' OR UPPER(host_organization)='MINI SENIOR PROJECT' OR (host_organization IS NULL AND period= 0) OR (UPPER(host_organization)='NONE' AND period= 0) ")
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

lbl3=Label(DataEntry3, text='Students Having End Of Study Internships', bg='Ghost white',fg='green', font=("times new york",13))
lbl3.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table3=ttk.Treeview(Tab3,column=("Total Number","Period"))

Student_table3.heading("Total Number",text="Total Number")
Student_table3.heading("Period",text="Average Period (months)")



Student_table3['show']='headings'
Student_table3.column("Total Number",width=10)
Student_table3.column("Period",width=10)

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
    curs.execute("select COUNT(Stud2) , ROUND(AVG(period)) from Internship WHERE host_organization IS NOT NULL OR  period !=0 AND UPPER(host_organization) != 'NONE' ")
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

lbl5=Label(DataEntry5, text='Internship period by Speciality', bg='Ghost white',fg='green', font=("times new york",13))
lbl5.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table5=ttk.Treeview(Tab5,column=("Major","Average Period(months)"))

Student_table5.heading("Major",text="Speciality")
Student_table5.heading("Average Period(months)",text="Average Period(months)")



Student_table5['show']='headings'
Student_table5.column("Major",width=10)
Student_table5.column("Average Period(months)",width=10)

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
    curs.execute("select major, AVG(period) from Internship,Diploma WHERE  Internship.Stud2=Diploma.Stud1 AND (host_organization IS NOT NULL OR  period !=0) AND (host_organization != 'None') GROUP BY major")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table5.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 6

DataEntry6=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry6.place(x=360,y=230, width=350,height=200)

lbl6=Label(DataEntry6, text='Internship Offers By major', bg='Ghost white',fg='green', font=("times new york",13))
lbl6.grid(row=0,column=0,sticky="w")


#Criteria to choose from

combo_search=ttk.Combobox(DataEntry6,font=("times new york",7,"bold"),width=20,state='readonly')
combo_search["values"]=('BA','Finance','Marketing','IT','Accounting','IPE')
combo_search.grid(row=1,column=0,padx=2)

#search btn

search = Button(DataEntry6, text="Go",bg='light blue', command=search)
search.grid(row=1, column=1, padx=5, ipadx=5)

#Frame of the table
Tab6=Frame(DataEntry6,bd=4,relief=RIDGE,bg='green')
Tab6.place(x=10,y=50,width=300,height=120)

#Define table columns
Student_table6=ttk.Treeview(Tab6,column=("Organizations","Number"))


Student_table6.heading("Organizations",text="Organizations")
Student_table6.heading("Number",text="Number")

Student_table6['show']='headings'
Student_table6.column("Organizations",width=80)
Student_table6.column("Number",width=80)
Student_table6.pack(fill=BOTH,expand=1)

#Frame 7

DataEntry7=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry7.place(x=720,y=230, width=350,height=200)

#Frame of the table
Tab7=Frame(DataEntry7,bd=4,relief=RIDGE,bg='green')
Tab7.place(x=10,y=30,width=300,height=150)

lbl7=Label(DataEntry7, text='Students Hired by The Host Organization After Graduation', bg='Ghost white',fg='green', font=("times new york",10))
lbl7.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table7=ttk.Treeview(Tab7,column=("Student ID","Host Organization"))


Student_table7.heading("Student ID",text="Student ID")
Student_table7.heading("Host Organization",text="Host Organization")


Student_table7['show']='headings'
Student_table7.column("Student ID",width=10)
Student_table7.column("Host Organization",width=10)

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
    curs.execute("Select  Stud2, host_organization FROM  Internship,Career WHERE Internship.Stud2=Career.Stud3 AND host_organization like '%city%'")
    rows = curs.fetchall()

    if len(rows) != 0:
        for row in rows:
            Student_table8.insert('', END, values=row)

except Exception as err:
    print('error', err)

#Frame 8

DataEntry8=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry8.place(x=5,y=440, width=350,height=200)

#Frame of the table
Tab8=Frame(DataEntry8,bd=4,relief=RIDGE,bg='green')
Tab8.place(x=10,y=30,width=300,height=150)

lbl8=Label(DataEntry8, text='Internship Offers By Gender', bg='Ghost white',fg='green', font=("times new york",13))
lbl8.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table8=ttk.Treeview(Tab8,column=("Gender","Number of Internships"))



Student_table8.heading("Gender",text="Gender")
Student_table8.heading("Number of Internships",text="Number of Internships")



Student_table8['show']='headings'
Student_table8.column("Gender",width=10)
Student_table8.column("Number of Internships",width=10)



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
    curs.execute("Select  sex,Count(Stud2) FROM  Internship,Student WHERE Internship.Stud2=Student.noStudent AND (host_organization IS NOT NULL OR  period !=0) AND (host_organization != 'None') GROUP BY sex  ")
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

lbl9=Label(DataEntry9, text='Employment waiting time in relation with number of internships ', bg='Ghost white',fg='green', font=("times new york",9))
lbl9.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table9=ttk.Treeview(Tab9,column=("Student ID","Waiting Time","Number of Internships"))

Student_table9.heading("Student ID",text="Student ID")
Student_table9.heading("Waiting Time",text="Waiting Time")
Student_table9.heading("Number of Internships",text="Number of Internships")




Student_table9['show']='headings'
Student_table9.column("Student ID",width=10)
Student_table9.column("Waiting Time",width=10)
Student_table9.column("Number of Internships",width=10)


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
    curs.execute(
        "Select  Stud2,round((hiring_date-grad_date)/30),num_int FROM  Internship,Student,Career,Diploma WHERE Internship.Stud2=Student.noStudent AND Internship.Stud2=Diploma.Stud1 AND Internship.Stud2=Career.Stud3 AND (host_organization IS NOT NULL OR  period !=0) AND (host_organization != 'None') AND hiring_date IS NOT NULL  ")
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

lbl10=Label(DataEntry10, text='Employment waiting time in relation with Host/Senior Project ', bg='Ghost white',fg='green', font=("times new york",9))
lbl10.grid(row=0,column=1,sticky="w")
#Define table columns
Student_table10=ttk.Treeview(Tab10,column=("Host/Senior Project","Waiting Time"))

Student_table10.heading("Host/Senior Project",text="Host/Senior Project")
Student_table10.heading("Waiting Time",text="Waiting Time")





Student_table10['show']='headings'
Student_table10.column("Host/Senior Project",width=10)
Student_table10.column("Waiting Time",width=10)



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
    curs.execute(
        "Select  host_organization,AVG(round((hiring_date-grad_date)/30)) FROM  Internship,Student,Career,Diploma WHERE Internship.Stud2=Student.noStudent AND Internship.Stud2=Diploma.Stud1 AND Internship.Stud2=Career.Stud3 AND (host_organization IS NOT NULL OR  period !=0) AND (host_organization != 'None') AND hiring_date IS NOT NULL Group By host_organization ")
    rows = curs.fetchall()
    if len(rows) != 0:
        for row in rows:
            Student_table10.insert('', END, values=row)


except Exception as err:
    print('error', err)


window.mainloop()
