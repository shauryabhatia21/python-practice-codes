import mysql.connector as m1

con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
if con.is_connected():
    print('Yes connected')
    eno=input('enter your enrollnment number')
    qry="delete from student where eno={}".format(eno)
    cursor=con.cursor()
    cursor.execute(qry)
    if cursor.rowcount>0:
        print("record deleted")
    else:
        print("record not found")
    con.commit()
    con.close()
else:
    print('not connected')
