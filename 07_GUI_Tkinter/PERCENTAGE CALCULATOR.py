from tkinter import *
root = Tk()
root.title("FIRST WINDOW")
root.minsize(500, 700)
root.maxsize(500, 700)

# Input variables
num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()

# Separate output variables so they don't overwrite each other
sum_result = StringVar()
pct_result = StringVar()

# Functions for calculations
def calculate_sum():
    total = num1.get() + num2.get() + num3.get() + num4.get() + num5.get()
    sum_result.set(f"YOUR SUM IS: {total}")

def calculate_percentage():
    total = num1.get() + num2.get() + num3.get() + num4.get() + num5.get()
    percentage = total / 5
    pct_result.set(f"YOUR PERCENTAGE IS: {percentage}%")

#ADDING LABELS:
Label(root, text='ENTER FIRST NUMBER', font=("BOLD", 12)).pack()
Entry(root, textvariable=num1).pack()
Label(root, text='ENTER SECOND NUMBER', font=("BOLD", 12)).pack()
Entry(root, textvariable=num2).pack()
Label(root, text='ENTER THIRD NUMBER', font=("BOLD", 12)).pack()
Entry(root, textvariable=num3).pack()
Label(root, text='ENTER FOURTH NUMBER', font=("BOLD", 12)).pack()
Entry(root, textvariable=num4).pack()
Label(root, text='ENTER FIFTH NUMBER', font=("BOLD", 12)).pack()
Entry(root, textvariable=num5).pack()
Button(root, text="SUM", font=('BOLD', 8), command=calculate_sum).pack(pady=5)
Label(root, font=("BOLD", 12), textvariable=sum_result).pack()
Button(root, text="PERCENTAGE", font=('BOLD', 8), command=calculate_percentage).pack(pady=5)
Label(root, font=("BOLD", 12), textvariable=pct_result).pack()
root.mainloop()
