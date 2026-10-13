def genissue1():
    import mysql.connector as m1
    con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
    import sys
    import smtplib
    import issueid
    import mytoken
    import librarydemo
    from datetime import datetime
    from datetime import date,timedelta
    while True:
        if con.is_connected():
            print('[****ISSUE TAB****]')
            print('1.ISSUE NEW BOOK')
            print('2 RETURN BOOK')
            print('3.SEARCH MEMBER')
            print('4.SHOW ALL DATA')
            print('5.DELETE MEMBER')
            print('6.RETURN TO MAIN MENUE')
            print('-'*75)
            ch=int(input('ENTER YOUR CHOISE:'))
            print('-'*75)
            match ch:
                case 1:
                    date=date.today()
                    mem=input('enter member id:')
                    id=input('enter book id:')
                    qry="select * from library where membership='{}'".format(mem)
                    cursor=con.cursor()
                    cursor.execute(qry)
                    rows=cursor.fetchall()
                    for i in rows:
                        if i[0]==mem:
                            qry="select * from books where id='{}'".format(id)
                            cursor=con.cursor()
                            cursor.execute(qry)
                            rows=cursor.fetchall()
                            for z in rows:
                                if z[0]==id:
                                    t=40
                                else:
                                    print('you have enter wrong book id')
                        else:
                            print('you have enter wrong member id')
                    if t==40:
                        new=int(input('ENTER DAYS TO BORROW:'))
                        print('BOOKING DATE:',date)
                        ten=timedelta(days=new)
                        newdate=date+ten
                        print('YOUR DUE DATE WILL BE:',newdate)
                        r=(f'₹{new*10}')
                        m=(f'RS{new*10}')
                        print('YOUR TOTAL COST WILL BE:',r)
                        token=mytoken.gentoken()
                        print('YOUR TOKEN NUMBER:',token)
                        u=30
                    if u==30:
                        qry="select * from library"
                        cursor=con.cursor()
                        cursor.execute(qry)
                        rows=cursor.fetchall()
                        for i in rows:
                            ki=i[3]
                            p=10
                    if p==10:
                        sender_email = "pythonprograms124@gmail.com"
                        password = "hbpp esqo cwnl nqfc" 
                        receiver_email=i[3]
                        subject = "THANK YOU FOR BEING CUSTOMER IN OUR LIBRARY"
                        message = f"""YOU BORROW BOOK FROM OUR LIBRARY.
                        - HERE ARE YOUR DETAILS:
                        - MEMBERSHIP ID: {mem}
                        - BOOK ID: {id}
                        - BOOKING DATE: {date}
                        - DUE DATE: {newdate}
                        - REGISTERED EMAIL ADDRESS: {receiver_email}
                        - COST: {m}
                        - TOKEN NUMBER: {token}"""
                        text = f"Subject: {subject}\n\n{message}"
                        try:
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls() 
                            server.login(sender_email, password)
                            server.sendmail(sender_email, receiver_email, text)
                            print(f"EMAIL SUCCESFULLY SEND TO:{receiver_email}!")
                        except Exception as e:
                                print(f"Failed to send email. Error: {e}")
                        finally:
                            try:
                                server.quit()
                            except:
                                pass
                    qry="insert into issue values('{}','{}','{}','{}','{}','{}','{}')".format(date,mem,id,newdate,ki,token,r)
                    cursor=con.cursor()
                    cursor.execute(qry)
                    if cursor.rowcount>0:
                        print("[record added]")
                    else:
                        print("[record not added]")
                case 2:
                    date1=date.today()
                    mem=input('ENTER YOUR TOKEN NUMBER: ')
                    qry= "select * from issue where cost='{}'".format(mem)
                    cursor = con.cursor()
                    cursor.execute(qry)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found for the entered Token Number.")
                    else:
                        for i in rows:
                            booking=i[0]
                            due=i[3]
                            amount=i[6]
                            print('_'*75)
                            print('TODAY CURRENT DATE IS:',date1)
                            print('YOUR BOOKING DATE IS:',booking)
                            print('YOUR DUE DATE IS:',due)
                            print('YOUR BOOKING AMOUNT IS:',amount)
                            object1=datetime.strptime(due,"%Y-%m-%d").date()
                            if date1>object1:
                                overdue=(date1-due).days
                                fine=10*overdue
                                total=amount+fine
                                print('_'*75)
                                print(f'YOUR RECORD IS OVERDUE BY{overdue}DAYS.')
                            else:
                                fine=0
                                total=amount
                                print('_'*75)
                                print('[BOOK RETURNED ON TIME]')
                            print('YOUR TOTAL FINE:',fine)
                            print('YOUR TOTAL AMOUNT TO BE PAID:',amount)
                            print('_'*75)
                            print('1.AMOUNT PAID')
                            print('2.AMOUNT NOT PAID')
                            ch=int(input('Enter your choice (1 or 2):'))
                            if ch==1:
                                qry = "delete from issue where cost='{}'".format(mem)
                                cursor.execute(qry)
                                con.commit()
                                print("Transaction completed and record updated successfully!")
                            else:
                                print("Transaction cancelled. Record not cleared.")
                case 3:
                    mem=input('ENTER YOUR TOKEN NUMBER:')
                    qry="select * from issue where cost='{}'".format(mem)
                    cursor=con.cursor()
                    cursor.execute(qry)
                    rows=cursor.fetchall()
                    for i in rows:
                        print('-'*75)
                        print('BOOKING DATE:',i[0])
                        print('MEMBERSHIP NUMBER:',i[1])
                        print('BOOK ID:',i[2])
                        print('DUE DATE:',i[3])
                        print('REGISTER EMAIL ID:',i[4])
                        print('COST:',i[6])
                        print('TOKEN NUMBER:',i[5])
                        print('-'*75)
                case 4:
                    qry="select * from issue"
                    cursor=con.cursor()
                    cursor.execute(qry)
                    rows=cursor.fetchall()
                    for i in rows:
                        print('-'*75)
                        print('BOOKING DATE:',i[0])
                        print('MEMBERSHIP NUMBER:',i[1])
                        print('BOOK ID:',i[2])
                        print('DUE DATE:',i[3])
                        print('REGISTER EMAIL ID:',i[4])
                        print('COST:',i[6])
                        print('TOKEN NUMBER:',i[5])
                        print('-'*75)
                case 5:
                     mem=input('ENTER YOUR TOKEN NUMBER:')
                     qry="delete from issue where cost='{}'".format(mem)
                     cursor=con.cursor()
                     cursor.execute(qry)
                     if cursor.rowcount>0:
                         print("record deleted")
                         print('-'*75)
                     else:
                         print("record not found")
                         print('-'*75)
                case 6:
                    con.commit()
                    con.close()
                    a=librarydemo.genlibrary1()
                    print(a)

