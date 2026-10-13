import sys
import pickle
import os
'''
pickle module is use for reading and writing on binary file
binary files are those files that are directly understanble by the computer
process of writing on binary files are called pickling or serialization
and done through dump()
dump(object,fileobject)

process of reading from binary file is called unpickling or deserializtion
and done through load()
load(fileobject)
'''

import enogenerator1
while True:
    print('***main menue***')
    print('1.Add A Student')
    print('2.Show Data')
    print('3.Search student')
    print('4.Remove student')
    print('5.change student name')
    ch=int(input('enter your choise ='))
    match ch:
        case 1:
            eno=enogenerator1.genAcno()
            name=input('enter student name =')
            course=input('enter course name =')
            fee=int(input('enter fees is ='))
            a1=[eno,name,course,fee]
            f1=open('student.dat','ab')
            pickle.dump(a1,f1)
            print('='*75)
            f1.close()
        case 2:
            f1=open('student.dat','rb')
            try:
                while True:
                    a1=pickle.load(f1)
                    print('Eno is',a1[0])
                    print('Name is ',a1[1])
                    print('Course is ',a1[2])
                    print('Fee is ',a1[3])
                    print('='*75)
            except Exception as e:
                pass
        case 3:
            f1=open('student.dat','rb')
            eno=input('enter your enrollnment no')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        print('Eno is',a1[0])
                        print('Name is ',a1[1])
                        print('Course is ',a1[2])
                        print('Fee is ',a1[3])
                        print('='*75)
                        f=1
                        break
            except Exception as e:
                pass
            if f==0:
                print('no record found')
            else :
                print('record found')

        case 4:
            f1=open('student.dat','rb')
            f2=open('temp.dat','wb')
            eno=input('enter your enrollnment no')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        f=1
                    else:
                        pickle.dump(a1,f2)
            except Exception as e:
                pass
            if f==0:
                print('no record found')
            else:
                f1.close()
                f2.close()
                os.remove('student.dat')
                os.rename('temp.dat','student.dat')
                print('Student Removed Succesfully')
        case 5:
            f1=open('student.dat','rb')
            f2=open('temp.dat','wb')
            eno=input('enter your enrollnment no')
            newname=input('Enter new name')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        a1[1]=newname
                        pickle.dump(a1,f2)
                        f=1
                    else:
                        pickle.dump(a1,f2)
            except Exception as e:
                pass
            if f==0:
                print('no record found')
            else:
                f1.close()
                f2.close()
                os.remove('student.dat')
                os.rename('temp.dat','student.dat')
               

               
