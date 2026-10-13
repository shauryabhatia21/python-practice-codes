import mysql.connector as m1

con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
if con.is_connected():
    print('Yes connected')
    eno=int(input('enter your enrollnment number'))
    ncourse=input('enter new course')
    qry="update student set coruse='{}' where eno={}".format(ncourse,eno)
    cursor=con.cursor()
    cursor.execute(qry)
    if cursor.rowcount>0:
        print("record updated")
    else:
        print("record not updated")
    con.commit()
    con.close()
else:
    print('not connected')
