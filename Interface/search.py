
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
def showall():

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
            " select fname,lname,age,sex,email,university,dip,major,minor,sec_maj_min,start_date,grad_date,host_organization,period,situation,domain,hiring_date,salary,searchMean from Student,Career,Diploma,Internship  where  Student.noStudent=Career.Stud3 AND Student.noStudent=Internship.Stud2 AND Student.noStudent=Diploma.Stud1" )
        rows = curs.fetchall()
        if len(rows) != 0:
            for row in rows:
                Student_table.insert('', END,values=row)
        else: messagebox.showinfo("Error","Data not found")


    except Exception as err:
        print('error', err)


def search2():

    # take values from search bar and put em into variables

    criterion=combo_search.get()
    text=txt_search.get()
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
            "select fname,lname,age,sex,email,university,dip,major,minor,sec_maj_min,start_date,grad_date,host_organization,period,situation,domain,hiring_date,salary,searchMean from Student,Career,Internship,Diploma  where " + str(criterion) + " LIKE '%" + str(text) + "%' AND Student.noStudent=Career.Stud3 AND Student.noStudent=Internship.Stud2 AND Student.noStudent=Diploma.Stud1")
        rows = curs.fetchall()
        if len(rows) != 0:
            for row in rows:
                Student_table.insert('', END,values=row)
        else: messagebox.showinfo("Error","Data not found")


    except Exception as err:
        print('error', err)



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

f=Frame(window,bg='Ghost white',height=1000,width=500)
f.place(x=450,y=100)


bt=Button(f,text='Info',command=Info,width=20,bg='light blue')
bt.grid(column=0,row=0)

bt1=Button(f,text='Search',width=20,bg='light blue',command=search)
bt1.grid(row=0,column=1)

bt2=Button(f,text='Statistics',command=Stat,width=20,bg='light blue')
bt2.grid(row=0,column=2)

frame=Frame(window,bg='Ghost white')
frame.place(x=150,y=150,height=500,width=900)




#search text
lbl_search=Label(frame, text='Search by', bg='Ghost white',fg='blue', font=("times new york",18,"bold"))
lbl_search.grid(row=0,column=0,pady=10)

#Criteria to choose from

combo_search=ttk.Combobox(frame,font=("times new york",15,"bold"),width=8,state='readonly')
combo_search["values"]=("fname","lname","age","sex","email","university","major","minor","grad_date","host_organization","situation","domain","hiring_date","salary","searchMean")
combo_search.grid(row=0,column=1,padx=5,pady=5)

#text
txt_search= Entry(frame,font=("times new york",15),bd=5,width=20,relief=GROOVE )
txt_search.grid(row=0, column=2,padx=2, pady=5, sticky="w")
#search btn
searchb = Button(frame, text="Search", command=search2)
searchb.grid(row=0, column=3, padx=20, ipadx=10,pady=10)
#show all btn
showall = Button(frame, text="Show all", command=showall)
showall.grid(row=0, column=4, padx=20, ipadx=10,pady=10)

#Frame of the table
Tab=Frame(frame,bd=4,relief=RIDGE,bg='green')
Tab.place(x=10,y=70,width=800,height=350)

#Define table columns
Student_table=ttk.Treeview(Tab,column=("fname","lname","age","gender","email","university","diploma","major","minor","second maj/min","start date univ","grad_date","host_organization","period","Situation","domain","hiring_date","salary","searchMean"))


Student_table.heading("fname",text="fname")
Student_table.heading("lname",text="lname")
Student_table.heading("age",text="age")
Student_table.heading("gender",text="gender")
Student_table.heading("email",text="email")
Student_table.heading("university",text="university")
Student_table.heading("diploma",text="diploma")
Student_table.heading("major",text="major")
Student_table.heading("minor",text="minor")
Student_table.heading("second maj/min",text="second maj/min")
Student_table.heading("start date univ",text="start date univ")
Student_table.heading("grad_date",text="grad_date")
Student_table.heading("host_organization",text="host_organization")
Student_table.heading("period",text="period")
Student_table.heading("Situation",text="Situation")
Student_table.heading("domain",text="domain")
Student_table.heading("hiring_date",text="hiring_date")
Student_table.heading("salary",text="salary")
Student_table.heading("searchMean",text="searchMean")

Student_table['show']='headings'
Student_table.column("fname",width=80)
Student_table.column("lname",width=80)
Student_table.column("age",width=80)
Student_table.column("gender",width=80)
Student_table.column("email",width=80)
Student_table.column("university",width=80)
Student_table.column("diploma",width=80)
Student_table.column("major",width=80)
Student_table.column("minor",width=80)
Student_table.column("second maj/min",width=80)
Student_table.column("start date univ",width=80)
Student_table.column("grad_date",width=80)
Student_table.column("host_organization",width=80)
Student_table.column("period",width=80)
Student_table.column("Situation",width=80)
Student_table.column("domain",width=80)
Student_table.column("hiring_date",width=80)
Student_table.column("salary",width=80)
Student_table.column("searchMean",width=80)
Student_table.pack(fill=BOTH,expand=1)

window.mainloop()
