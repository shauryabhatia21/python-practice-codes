#import the function:
from tkinter import *
root=Tk()

def sumNumber():
    x=num1.get()+num2.get()
    result.set("sum is"+str(x))
    
num1=IntVar()
num2=IntVar()
result=StringVar()
#window size:
root.title("First Winidow")
root.minsize(500,700)
root.maxsize(500,700)

#add labels:
lblnum1=Label(root,text='ENTER FIRST NUMBER',font=("BOLD",12)).pack()
txtnum1=Entry(root,textvariable=num1).pack()
lblnum2=Label(root,text='ENTER SECOND NUMBER',font=("BOLD",12)).pack()
txtnum2=Entry(root,textvariable=num2).pack()

#adding button:
btnsum=Button(root,text="SUM", font=('BOLD',8),command=sumNumber).pack()

lblnum3=Label(root,text="YOUR ANSWER:",font=("BOLD",12),textvariable=result).pack()


root.mainloop()



