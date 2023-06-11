
# importing needed libraries, tkinter for the interface library and cx_Oracle for Oracle
from tkinter import *

from tkinter import messagebox
from tkinter import ttk #to make the combo for gender
import cx_Oracle
import sys
import os



# insert Diploma function
def insert_diploma():
    # take values from the form and put em into variables
    Sid1 = int(S_id1.get())
    Did = D_id.get()
    Duni = D_uni.get()
    Ddispl = D_displ.get()
    Dmaj = D_maj.get()
    Dmin = D_min.get()
    Dsec = D_sec.get()
    Dstart = D_start.get()
    Dgrad = D_grad.get()


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
                cur.callproc('insert_diploma', (Did,Sid1, Duni, Ddispl, Dmaj, Dmin, Dsec, Dstart, Dgrad))
                print('Values Inserted')
                messagebox.showinfo("Success", "Values inserted")

    except Exception as err:
        messagebox.showinfo("Error", err)

#insert Career function
def insert_career():

    # take values from the form and put em into variables
    #Career table
    Sid2 = int(S_id2.get())
    Cid = C_id.get()
    Csit = C_situation.get()
    Cdom = C_dom.get()
    Chir = C_hir.get()
    Cleav = C_leav.get()
    Ccity=C_city.get()
    Csal=C_sal.get()
    Csearch=C_search.get()

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
                #cursor to call procedure
                cur.callproc('insert_career', (Cid, Sid2, Csit, Cdom, Chir, Cleav, Ccity, Csal, Csearch))
                print('Values Inserted')
                messagebox.showinfo("Success", "Values inserted")

    except Exception as err:
        messagebox.showinfo("Error", err)

# insert Diploma function
def insert_internship():
    # take values from the form and put em into variables
    Sid3 = int(S_id3.get())
    Iid = I_id.get()
    Inum = int(I_num.get())
    Ihost = I_host.get()
    Iperiod = int(I_period.get())



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
            cur.callproc('insert_internship', (Iid,Sid3,Inum,Ihost,Iperiod))
            print('Values Inserted')
            messagebox.showinfo("Success", "Values inserted")

    except Exception as err:
        messagebox.showinfo("Error", err)



window=Tk()

#SET TITLE
window.title("Add more info")

#BACKGROUND COLOR
window.config(bg='cadet blue')

#WINDOW SIZE
window.geometry('1350x850+0+0')


# STYLE THE TITLE Student database
Title=Label(window, text='Add More Info', bd=1, relief=GROOVE ,font=('times new roman',35,'bold'),bg="Ghost White",fg='cadet Blue')
Title.pack(side=TOP,fill=X) #TITLE POSITION

# CREATE FRAMES
#Frame 1
DiplomaEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
DiplomaEntry.place(x=20,y=100, width=400,height=320)

# labels for the entry boxes

S_id1_label = Label(DiplomaEntry, text="Your ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_id1_label.grid(row=0, column=0)

D_id_label=Label(DiplomaEntry, text="Diploma ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_id_label.grid(row=8, column=0)

D_uni_label=Label(DiplomaEntry, text="University:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_uni_label.grid(row=9, column=0)

D_displ_label=Label(DiplomaEntry, text="Diploma:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_displ_label.grid(row=10, column=0)

D_maj_label=Label(DiplomaEntry, text="Major:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_maj_label.grid(row=11, column=0)

D_min_label=Label(DiplomaEntry, text="Minor:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_min_label.grid(row=12, column=0)

D_sec_label=Label(DiplomaEntry, text="Second Maj/Min:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_sec_label.grid(row=13, column=0)

D_start_label=Label(DiplomaEntry, text="Starting Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_start_label.grid(row=14, column=0)

D_grad_label=Label(DiplomaEntry, text="Graduation Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
D_grad_label.grid(row=15, column=0)



# creating text boxes for input on the GUI
S_id1 = Entry(DiplomaEntry, width=30)
S_id1.grid(row=0,column=1,pady=5)

#Diploma
D_id=Entry(DiplomaEntry, width=30)
D_id.grid(row=8, column=1,pady=5)

D_uni=Entry(DiplomaEntry, width=30)
D_uni.grid(row=9, column=1,pady=5)

D_displ=Entry(DiplomaEntry, width=30)
D_displ.grid(row=10, column=1,pady=5)

D_maj=ttk.Combobox(DiplomaEntry,font=('times new roman',10,'bold'), state='readonly',width=23)
D_maj['values']=('BA','Finance','Marketing','IT','Accounting')
D_maj.grid(row=11, column=1, padx=5, pady=2)

D_min=ttk.Combobox(DiplomaEntry,font=('times new roman',10,'bold'), state='readonly',width=23)
D_min['values']=('BA','Finance','Marketing','IT','Accounting','IPE')
D_min.grid(row=12, column=1, padx=5, pady=2)

D_sec=ttk.Combobox(DiplomaEntry,font=('times new roman',10,'bold'), state='readonly',width=23)
D_sec['values']=('BA','Finance','Marketing','IT','Accounting','IPE')
D_sec.grid(row=13, column=1, padx=5, pady=3)

D_start=Entry(DiplomaEntry, width=30)
D_start.grid(row=14, column=1,pady=5)

D_grad=Entry(DiplomaEntry, width=30)
D_grad.grid(row=15, column=1,pady=5)

# Creation of the insert button
insert = Button(DiplomaEntry, text="Insert", command=insert_diploma,bg='light blue')
insert.grid(row=16, column=1, columnspan=2, padx=30, ipadx=30,pady=10)

Add1_label = Label(DiplomaEntry, text="Add Diploma",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
Add1_label.grid(row=17, column=1)

#Frame 2
CareerEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
CareerEntry.place(x=480,y=100, width=400,height=320)


# labels for the entry boxes

S_id2_label = Label(CareerEntry, text="Your ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_id2_label.grid(row=0, column=0)

C_id_label = Label(CareerEntry, text="Career ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_id_label.grid(row=1, column=0)



C_situation_label = Label(CareerEntry, text="Situation:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_situation_label.grid(row=2, column=0)

C_dom_label = Label(CareerEntry, text="Domain:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_dom_label.grid(row=3, column=0)

C_hir_label = Label(CareerEntry, text="Hiring Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_hir_label.grid(row=4, column=0)

C_leav_label = Label(CareerEntry, text="Leaving Date:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_leav_label.grid(row=5, column=0)

C_city_label = Label(CareerEntry, text="City:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_city_label.grid(row=6, column=0)

C_sal_label = Label(CareerEntry, text="Salary:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_sal_label.grid(row=7, column=0)

C_search_label = Label(CareerEntry, text="Search Mean:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
C_search_label.grid(row=8, column=0)


# creating text boxes for input on the GUI
S_id2 = Entry(CareerEntry, width=30)
S_id2.grid(row=0,column=1,pady=5)

#Career
C_id = Entry(CareerEntry, width=30)
C_id.grid(row=1, column=1,pady=5)
#

C_situation=ttk.Combobox(CareerEntry,font=('times new roman',10,'bold'), state='readonly',width=23)
C_situation['values']=('Employee','Business Owner','Master Student', 'PHD Student','MBA Student','Other')
C_situation.grid(row=2, column=1, padx=5, pady=3)

C_dom = Entry(CareerEntry, width=30)
C_dom.grid(row=3, column=1,pady=5)

C_hir = Entry(CareerEntry, width=30)
C_hir.grid(row=4, column=1,pady=5)
C_leav = Entry(CareerEntry, width=30)
C_leav.grid(row=5, column=1,pady=5)

C_city = Entry(CareerEntry, width=30)
C_city.grid(row=6, column=1,pady=5)

C_sal=ttk.Combobox(CareerEntry,font=('times new roman',10,'bold'), state='readonly',width=23)
C_sal['values']=('Below 1000','1000-1500','1500-2000','2500-3000','3000-4000','4000-5000','Above 5000')
C_sal.grid(row=7, column=1, padx=5, pady=2)

C_search = Entry(CareerEntry, width=30)
C_search.grid(row=8, column=1,pady=5)


# Creation of the insert button
insertc = Button(CareerEntry, text="Insert", command=insert_career,bg='light blue')
insertc.grid(row=9, column=1, columnspan=2, padx=30, ipadx=30,pady=10)

Add2_label = Label(CareerEntry, text="Add Career",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
Add2_label.grid(row=10, column=1)

#Frame 3
IntEntry=Frame(window,bg='Ghost White', relief=GROOVE, borderwidth=5 )
IntEntry.place(x=920,y=100, width=400,height=320)

# labels for the entry boxes

S_id3_label = Label(IntEntry, text="Your ID:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
S_id3_label.grid(row=0, column=0)

I_id_label = Label(IntEntry,text="Internship ID",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_id_label.grid(row=1, column=0)

I_num_label = Label(IntEntry, text="Nbre of internships:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_num_label.grid(row=2, column=0)

I_host_label = Label(IntEntry, text="Host Organization:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_host_label.grid(row=3, column=0)

I_period_label =Label(IntEntry, text="Internship Period:",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
I_period_label.grid(row=4, column=0)

# creating text boxes for input on the GUI
S_id3 = Entry(IntEntry, width=30)
S_id3.grid(row=0,column=1,pady=7)

I_id = Entry(IntEntry, width=30)
I_id.grid(row=1, column=1,pady=7)

I_num= Entry(IntEntry, width=30)
I_num.grid(row=2, column=1,pady=7)

I_host = Entry(IntEntry, width=30)
I_host.grid(row=3, column=1,pady=7)

I_period=Entry(IntEntry, width=30)
I_period.grid(row=4, column=1,pady=7)


# Creation of the insert button
inserti = Button(IntEntry, text="Insert", command=insert_internship,bg='light blue')
inserti.grid(row=9, column=1, columnspan=2, padx=30, ipadx=30,pady=10)

Add3_label = Label(IntEntry, text="Add Internship",font=('times new roman',10,'bold'),bg="Ghost White",fg='cadet Blue')
Add3_label.grid(row=10, column=1)



window.mainloop()
