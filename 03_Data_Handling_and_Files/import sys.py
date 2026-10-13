import sys
student=[]
while True:
    print('***main menue***')
    print('1.add a student')
    print('2.rename student')
    print('3.serch student')
    print('4.modify student')
    print('5.display all student')
    print('6.exit')
    ch=int(input('enter your choise ='))
    match ch:
        case 1:
            print('='*75)
            eno=int(input('enter your enrollment no ='))
            name=input('enter student name =')
            course=input('enter course name =')
            fee=int(input('enter fees is ='))
            a1=[eno,name,course,fee]
            student.append(a1)
            print("Student add successfully")
            print('='*75)
        case 2:
            name=input('enter student name =')
            print("Student name change successfully")
        case 3:
            print(a1)
            print('all student name printed')
        case 6:
            print('the data has been stored')
            print('THANK YOU FOR VISIT')
            sys.exit(0) 