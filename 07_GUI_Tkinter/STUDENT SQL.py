from tkinter import *
import mysql.connector as m1
con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')

def addRec():
    if con.is_connected():
        eno1=eno.get()
        name1=name.get()
        course1=course.get()
        fees1=fees.get()
        qry="insert into student values({},'{}','{}',{})".format(eno1,name1,course1,fees1)
        cursor=con.cursor()
        cursor.execute(qry)
        if cursor.rowcount>0:
            print("record added")
            print('-'*75)
        else:
            print("record not added")
            print('-'*75)
        con.commit()
        con.close()
    else:
        print('connetion error')

root=Tk()
eno=IntVar()    
name=StringVar()
course=StringVar()
fees=IntVar()

root.title("SCHOOL WINDOW")
root.minsize(600,800)
root.maxsize(600,800)

lbleno=Label(root,text="ENTER YOUR ENROLLNMENT NUMBER",font=("BOLD",12)).pack()
txteno=Entry(root,textvariable=eno).pack()


lblname=Label(root,text='ENTER YOUR NAME',font=("BOLD",12)).pack()
txtname=Entry(root,textvariable=name).pack()
lblcourse=Label(root,text='ENTER COURSE NAME',font=("BOLD",12)).pack()
txtcourse=Entry(root,textvariable=course).pack()
lblfees=Label(root,text='ENTER YOUR FEES',font=("BOLD",12)).pack()
txtfees=Entry(root,textvariable=fees).pack()


bt1=Button(root,text="save", font=('BOLD',8),command=addRec).pack()



                                                                                                                                                                                                                                                                                                                                                                                                                                                        

root.mainloop()



