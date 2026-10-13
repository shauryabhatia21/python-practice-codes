'''
READING AND writing from csv file
csv stands for command seperaed value

this is file like a text file but more flexible then text file and can be open in different
formats
for readng and writing on csv file,
for reading we need the object of reader
a1=csv.reader(fileobject)

for writing we need the object of writer on csv file
a1=csv.writer(f1)

writerow() will write one row at a time
writerows() will write multiple rows at a time
f1=open("student.csv","w",newline='')#for no line
f1=open("student.csv","w",)#for line 

import csv
def addCsv():
    f1=open("student.csv","w",newline='')
    a1=csv.writer(f1)
    a1.writerow(['Enroll','StudentName','Course','Fee'])
    while True:
        eno=int(input('enter your enrollnment no'))
        name=input('enter your name')
        course=input('enter your course name')
        fee=input('enter your fees')
        reco=[eno,name,course,fee]
        a1.writerow(reco)
        x=input("Do u want to enter more")
        if x=='no':
            f1.close()
            break
addCsv()'''
import csv
def readCsv():
    f1=open("student.csv","r")
    a1=csv.reader(f1)
    for x in a1:
        print('Eno is',x[0])
        print('name is',x[1])
        print('course is',x[2])
        print('fee is',x[1])
        print('='*50)
readCsv()

    

    


