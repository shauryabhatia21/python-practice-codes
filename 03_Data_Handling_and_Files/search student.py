import mysql.connector as m1

con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
if con.is_connected():
    print('Yes connected')
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
else:
    print('not connected')
