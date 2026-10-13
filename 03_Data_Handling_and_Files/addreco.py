import mysql.connector as m1
con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
if con.is_connected():
    print('Yes connected')
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
else:
    print('not connected')
