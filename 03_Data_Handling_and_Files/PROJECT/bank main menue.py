import mysql.connector as m1
import sys
while True:
    con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
    if con.is_connected():
        print('**** bank main menue****')
        print('1.add customer')
        print('2.delete customer')
        print('3.chnge account type')
        print('4.display all records')
        print('5.search customer')
        print('6.Exit')
        ch=int(input('enteryour choise'))
        match ch:
            case 1:
                acc=input('enter your account number')
                name=input('enter your name')
                typ=input('enter your account type')
                bal=int(input('enter your balance'))
                qry="insert into customer values({},'{}','{}',{})".format(acc,name,typ,bal)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record added")
                else:
                    print("record not added")
                con.commit()
                con.close()
            case 2:
                eno=int(input('enter your account number'))
                qry="delete from customer where acc={}".format(acc)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record deleted")
                else:
                    print("record not found")
                con.commit()
                con.close()
            case 3:
                acc=int(input('enter your account number'))
                type=input('enter new account type')
                qry="update customer set type='{}' where acc={}".format(acc,type)
                cursor=con.cursor()
                cursor.execute(qry)
                if cursor.rowcount>0:
                    print("record updated")
                else:
                    print("record not updated")
                con.commit()
                con.close()
            case 4:
                qry="select * from customer"
                cursor=con.cursor()
                cursor.execute(qry)
                rows=cursor.fetchall()
                for i in rows:
                    print('-'*75)
                    print('enrollnment is',i[0])
                    print('name is',i[1])
                    print('account type is',i[2])
                    print('name is',i[3])
                    print('-'*75)
                con.commit()
                con.close()
            case 5:
                eno=int(input('enter your eno'))
                qry="select * from customer where acc={}".format(acc)
                cursor=con.cursor()
                cursor.execute(qry)
                rows=cursor.fetchall()
                for i in rows:
                    print('-'*75)
                    print('account number is',i[0])
                    print('name is',i[1])
                    print('type is',i[2])
                    print('bal is',i[3])
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

