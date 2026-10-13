import mysql.connector as m1
import sys
while True:
    con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
    if con.is_connected():
        print('****main menue****')
        print('1.add student')
        print('2.delete student')
        print('3.update course student')
        print('4.display all records')
        print('5.search student')
        print('6.Exit')
        ch=int(input('enteryour choise'))
        match ch:
            case 1:
                eno=input('enter your enrollnment number')
                name=input('enter your name')
                course=input('enter your course')
                fee=int(input('enter your fees'))
                qry="insert into student values({},'{}','{}',{})".format(eno,name,course,fee)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record added")
                else:
                    print("record not added")
                con.commit()
                con.close()
            case 2:
                eno=int(input('enter your enrollnment number'))
                qry="delete from student where eno={}".format(eno)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record deleted")
                else:
                    print("record not found")
                con.commit()
                con.close()
            case 3:
                eno=int(input('enter your enrollnment number'))
                name=input('enter new course')
                qry="update student set name='{}' where eno={}".format(name,eno)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record updated")
                else:
                    print("record not updated")
                con.commit()
                con.close()
            case 4:
                qry="select * from student"
                cursor=con.cursor()
                cursor.execute(qry)
                rows=cursor.fetchall()
                for i in rows:
                    print('-'*75)
                    print('enrollnment is',i[0])
                    print('name is',i[1])
                    print('course is',i[2])
                    print('name is',i[3])
                    print('-'*75)
                con.commit()
                con.close()
            case 5:
                eno=int(input('enter your eno'))
                qry="select * from student where eno={}".format(eno)
                cursor=con.cursor()
                cursor.execute(qry)
                rows=cursor.fetchall()
                for i in rows:
                    print('-'*75)
                    print('enrollnment is',i[0])
                    print('name is',i[1])
                    print('course is',i[2])
                    print('name is',i[3])
                    print('-'*75)
                con.commit()
                con.close()
            case 6:
                print('*'*75)
                print('your data has been stored')
                print('*'*75)
                sys.exit()
            
else:
    print('not connected')

