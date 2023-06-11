
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os

#open other file
def Add():
    os.system('Add.py')
# testing  function
def submit():

    # take values from the form and put em into variables
    #Student table
    Sid = int(S_id.get())
    Aid = int(1)
    Sname = S_name.get()
    Slast = S_last.get()
    age = int(S_age.get())
    ph = phone.get()
    email= em.get()
    addr= add.get()
    G= combo_gender.get()

    #Career table
    Cid = C_id.get()
    Csit = C_situation.get()
    Cdom = C_dom.get()
    Chir = C_hir.get()
    Cleav = C_leav.get()
    Ccity=C_city.get()
    Csal=C_sal.get()
    Csearch=C_search.get()

    #domain Table
    Did=D_id.get()
    Duni=D_uni.get()
    Ddispl = D_displ.get()
    Dmaj = D_maj.get()
    Dmin = D_min.get()
    Dsec =D_sec.get()
    Dstart=D_start.get()
    Dgrad=D_grad.get()

    #Internship Table
    Iid=I_id.get()
    Inum=int(I_num.get())
    Ihost=I_host.get()
    Iperiod=I_period.get()

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
            cur.callproc('insert_info', (Sid,Aid, Sname, Slast, age, G, email, addr, ph,Did
                                     , Duni, Ddispl, Dmaj, Dmin, Dsec, Dstart, Dgrad,Cid,Csit,Cdom,Chir,Cleav,Ccity,Csal,Csearch,
                                     Iid,Inum,Ihost,int(Iperiod)))
            print('Values Inserted')
            messagebox.showinfo("Success", "Values inserted")
    except Exception as err:
        messagebox.showinfo("Error", err)

def update():
    # take values from the form and put em into variables
    # Student table
    Sid = S_id.get()
    Sname = S_name.get()
    Slast = S_last.get()
    age = S_age.get()
    ph = phone.get()
    email = em.get()
    addr = add.get()
    G = combo_gender.get()

    # Career table
    Cid = C_id.get()
    Csit = C_situation.get()
    Cdom = C_dom.get()
    Chir = C_hir.get()
    Cleav = C_leav.get()
    Ccity = C_city.get()
    Csal = C_sal.get()
    Csearch = C_search.get()

    # domain Table
    Did = D_id.get()
    Duni = D_uni.get()
    Ddispl = D_displ.get()
    Dmaj = D_maj.get()
    Dmin = D_min.get()
    Dsec = D_sec.get()
    Dstart = D_start.get()
    Dgrad = D_grad.get()

    # Internship Table
    Iid = I_id.get()
    Inum = I_num.get()
    Ihost = I_host.get()
    Iperiod = I_period.get()


    try:
            # create connection
            conn = cx_Oracle.connect('SYSTEM/SYSTEM@//localhost:1521/xe')
            print('Connection to database established')
    except Exception as err:
            print('Connection failed', err)
        # create cursor to be able to execute queries stored within variables
    cur = conn.cursor()

    ##update Student
    if Sid != "":
        cur.callproc('update_student',(Sid,Sname,Slast,int(age),G,email,addr,int(ph)))
        messagebox.showinfo("Success", "Student Updated")
    ##update diploma
    if Did!="":
        cur.callproc('update_diploma', (Did, Duni, Ddispl, Dmaj, Dmin, Dsec, Dstart, Dgrad))
        messagebox.showinfo("Success", "Diploma Updated")
    ## update Career
    if Cid!="":
        cur.callproc('update_career', (Cid, Csit, Cdom, Chir, Cleav, Ccity, Csal, Csearch))
        messagebox.showinfo("Success", "Career Updated")

    ##update Internship
    if Iid!="":
        cur.callproc('update_internship', (Iid, int(Inum), Ihost, int(Iperiod)))
        messagebox.showinfo("Success", "Internship Updated")



def delete():
    # take values from the form and put em into variables
    # Student id

    Sid = S_id.get()
    # Career id
    Cid = C_id.get()
    # domain id
    Did = D_id.get()
    # Internship id
    Iid = I_id.get()

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
            if Sid != "":
                curs.callproc('delete_student', (int(Sid),))
                messagebox.showinfo('success','student deleted')
            if Did != "":
                curs.callproc('delete_diploma', (Did,))
                messagebox.showinfo('success', 'diploma deleted')

            if Cid !="" :
                curs.callproc('delete_career', (Cid,))
                messagebox.showinfo('success', 'career deleted')

            if Iid !="" :
                curs.callproc('delete_internship', (Iid,))
                messagebox.showinfo('success', 'internship deleted')
    except Exception as err:
        print('error', err)



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


def search():

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
window.title('Student Database')

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# CREATE FRAMES
#Frame 1
DataEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DataEntry.place(x=5,y=70, width=480,height=700)

# STYLE THE TITLE Student database
Title=Label(window, text='Student Database', bd=1, relief=GROOVE ,font=('times new roman',35,'bold'),bg="Ghost White",fg='cadet Blue')
Title.pack(side=TOP,fill=X) #TITLE POSITION



# labels for the entry boxes
#Student
S_id_label = Label(DataEntry, text="ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_id_label.grid(row=0, column=0)
S_name_label = Label(DataEntry, text="First Name : ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_name_label.grid(row=1, column=0)
S_last_label = Label(DataEntry, text="Last name : ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_last_label.grid(row=2, column=0)
S_age_label = Label(DataEntry, text="Age: ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_age_label.grid(row=3, column=0)
Gender_label = Label(DataEntry, text="Gender:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
Gender_label.grid(row=4, column=0)

em_label = Label(DataEntry, text="Email : ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
em_label.grid(row=5, column=0)
add_label = Label(DataEntry, text="Address: ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
add_label.grid(row=6, column=0)
phone_label = Label(DataEntry, text="Phone number: ",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
phone_label.grid(row=7, column=0)

#Diploma
D_id_label=Label(DataEntry, text="Diploma ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_id_label.grid(row=8, column=0)

D_uni_label=Label(DataEntry, text="University:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_uni_label.grid(row=9, column=0)

D_displ_label=Label(DataEntry, text="Diploma:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_displ_label.grid(row=10, column=0)

D_maj_label=Label(DataEntry, text="Major",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_maj_label.grid(row=11, column=0)

D_min_label=Label(DataEntry, text="Minor",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_min_label.grid(row=12, column=0)

D_sec_label=Label(DataEntry, text="Second Maj/Min",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_sec_label.grid(row=13, column=0)

D_start_label=Label(DataEntry, text="Starting Date",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_start_label.grid(row=14, column=0)

D_grad_label=Label(DataEntry, text="Graduation Date",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_grad_label.grid(row=15, column=0)

#Career
C_id_label = Label(DataEntry, text="Career ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_id_label.grid(row=0, column=2)

C_situation_label = Label(DataEntry, text="Situation:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_situation_label.grid(row=1, column=2)

C_dom_label = Label(DataEntry, text="Study/work field:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_dom_label.grid(row=2, column=2)

C_hir_label = Label(DataEntry, text="Hiring Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_hir_label.grid(row=3, column=2)

C_leav_label = Label(DataEntry, text="Leaving Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_leav_label.grid(row=4, column=2)

C_city_label = Label(DataEntry, text="Work or Study Location:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_city_label.grid(row=5, column=2)

C_sal_label = Label(DataEntry, text="Salary:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_sal_label.grid(row=6, column=2)

C_search_label = Label(DataEntry, text="Search Mean:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_search_label.grid(row=7, column=2)


#Internship
I_id_label = Label(DataEntry,text="Internship ID",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_id_label.grid(row=8, column=2)

I_num_label = Label(DataEntry, text="Nbre of internships:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_num_label.grid(row=9, column=2)

I_host_label = Label(DataEntry, text="Host Organization:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_host_label.grid(row=10, column=2)

I_period_label =Label(DataEntry, text="Internship Period:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_period_label.grid(row=11, column=2)




# creating text boxes for input on the GUI
S_id = Entry(DataEntry, width=15)
S_id.grid(row=0,column=1,pady=2)
S_name = Entry(DataEntry, width=15)
S_name.grid(row=1, column=1,pady=2)
#
S_last = Entry(DataEntry, width=15)
S_last.grid(row=2, column=1,pady=2)

#
S_age = Entry(DataEntry, width=15)
S_age.grid(row=3, column=1,pady=2)

#
combo_gender=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
combo_gender['values']=('M','F')
combo_gender.grid(row=4, column=1, padx=5, pady=2)

#
em = Entry(DataEntry, width=15)
em.grid(row=5, column=1,pady=2)

#
add = Entry(DataEntry, width=15)
add.grid(row=6, column=1,pady=2)

#
phone = Entry(DataEntry, width=15)
phone.grid(row=7, column=1,pady=2)

#Diploma
D_id=Entry(DataEntry, width=15)
D_id.grid(row=8, column=1)

D_uni=Entry(DataEntry, width=15)
D_uni.grid(row=9, column=1)

D_displ=Entry(DataEntry, width=15)
D_displ.grid(row=10, column=1)

D_maj=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
D_maj['values']=('BA','Finance','Marketing','IT','Accounting','IPE')
D_maj.grid(row=11, column=1, padx=5, pady=2)

D_min=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
D_min['values']=('BA','Finance','Marketing','IT','Accounting','IPE')
D_min.grid(row=12, column=1, padx=5, pady=2)

D_sec=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
D_sec['values']=('BA','Finance','Marketing','IT','Accounting','IPE')
D_sec.grid(row=13, column=1, padx=5, pady=3)


D_start=Entry(DataEntry, width=15)
D_start.grid(row=14, column=1)

D_grad=Entry(DataEntry, width=15)
D_grad.grid(row=15, column=1)

#Career
C_id = Entry(DataEntry, width=15)
C_id.grid(row=0, column=3,pady=2)
#


C_situation=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
C_situation['values']=('Employee','Part time employee','Alternate','Business Owner','Master Student', 'PHD Student','MBA Student','Other')
C_situation.grid(row=1, column=3, padx=5, pady=3)


C_dom = Entry(DataEntry, width=15)
C_dom.grid(row=2, column=3,pady=2)

C_hir = Entry(DataEntry, width=15)
C_hir.grid(row=3, column=3,pady=2)

C_leav = Entry(DataEntry, width=15)
C_leav.grid(row=4, column=3,pady=2)

C_city = Entry(DataEntry, width=15)
C_city.grid(row=5, column=3,pady=2)

C_sal=ttk.Combobox(DataEntry,font=('times new roman',10,'bold'), state='readonly',width=10)
C_sal['values']=('Below 1000','1000-1500','1500-2000','2500-3000','3000-4000','4000-5000','Above 5000')
C_sal.grid(row=6, column=3, padx=5, pady=2)


C_search = Entry(DataEntry, width=15)
C_search.grid(row=7, column=3,pady=2)

#Internship
I_id = Entry(DataEntry, width=15)
I_id.grid(row=8, column=3)

I_num= Entry(DataEntry, width=15)
I_num.grid(row=9, column=3)

I_host = Entry(DataEntry, width=15)
I_host.grid(row=10, column=3)

I_period=Entry(DataEntry, width=15)
I_period.grid(row=11, column=3)


# Creation of the insert button
insert = Button(DataEntry, text="Insert", bg='light blue', command=submit)
insert.grid(row=16, column=0, columnspan=2, padx=20, ipadx=10,pady=10)

update = Button(DataEntry, text="Update",bg='light blue', command=update)
update.grid(row=16, column=1, columnspan=2, padx=20, ipadx=10,pady=10)

delete = Button(DataEntry, text="Delete",bg='light blue', command=delete)
delete.grid(row=16, column=2, columnspan=2, padx=20, ipadx=10,pady=10)

Add = Button(DataEntry, text="Add More Info", bg='light blue',command=Add)
Add.grid(row=17, column=1, columnspan=2, padx=20, ipadx=10,pady=10)


#Frame2 #showing info
Details=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
Details.place(x=500,y=70, width=880,height=700)

#search text
lbl_search=Label(Details, text='Search by', bg='Ghost white',fg='blue', font=("times new york",18,"bold"))
lbl_search.grid(row=0,column=0,pady=10,sticky="w")

#Criteria to choose from

combo_search=ttk.Combobox(Details,font=("times new york",15,"bold"),width=8,state='readonly')
combo_search["values"]=("fname","lname","age","sex","email","university","major","minor","grad_date","host_organization","situation","domain","hiring_date","salary","searchMean")
combo_search.grid(row=0,column=1,padx=5,pady=5)

#text
txt_search= Entry(Details,font=("times new york",15),bd=5,width=20,relief=GROOVE )
txt_search.grid(row=0, column=2,padx=2, pady=5, sticky="w")
#search btn
searchb = Button(Details, text="Search",bg='light blue', command=search)
searchb.grid(row=0, column=3, padx=20, ipadx=10,pady=10)
#show all btn
showall = Button(Details, text="Show all", bg='light blue',command=showall)
showall.grid(row=0, column=4, padx=20, ipadx=10,pady=10)

#Frame of the table
Tab=Frame(Details,bd=4,relief=RIDGE,bg='green')
Tab.place(x=10,y=70,width=760,height=500)

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
Student_table.column("fname",width=100)
Student_table.column("lname",width=100)
Student_table.column("age",width=100)
Student_table.column("gender",width=100)
Student_table.column("email",width=100)
Student_table.column("university",width=100)
Student_table.column("diploma",width=100)
Student_table.column("major",width=100)
Student_table.column("minor",width=100)
Student_table.column("second maj/min",width=100)
Student_table.column("start date univ",width=100)
Student_table.column("grad_date",width=100)
Student_table.column("host_organization",width=100)
Student_table.column("period",width=100)
Student_table.column("Situation",width=100)
Student_table.column("domain",width=100)
Student_table.column("hiring_date",width=10)
Student_table.column("salary",width=100)
Student_table.column("searchMean",width=100)
Student_table.pack(fill=BOTH,expand=1)
window.mainloop()
