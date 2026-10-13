def genmember():
        import librarydemo
        import mysql.connector as m1
        con=m1.connect(host='localhost',database='ots',user='root',password='Shaurya1@')
        import membershipno
        import smtplib
        from datetime import datetime
        from datetime import date,timedelta
        while True:
                print('****[MEMBERS MENUE]****')
                print('1.ADD MEMBER')
                print('2.DLETE MEMBER')
                print('3.CHANGE NAME')
                print('4.DISPLAY ALL RECORDS')
                print('5.SEARCH MEMBER')
                print('6.RETURN TO THE MAIN MENUE')
                print('-'*75)
                ch=int(input('ENTER YOUR CHOISE:'))
                print('-'*75)
                match ch:
                    case 1:
                            mem=membershipno.genAcno()
                            name=input('ENTER YOUR NAME:')
                            date1=date.today()
                            print('JOINING DATE',date1)
                            sender_email = "pythonprograms124@gmail.com"
                            password = "hbpp esqo cwnl nqfc" 
                            receiver_email= input("ENTER RECIVER EMAIL: ")
                            print('YOUR MEMBERSHIP ID IS :',mem)
                            subject = "THANK YOU FOR JOINING IN LIBRARY"
                            message = f"""Thank you for being a valuable customer in our library.
                            - HERE ARE YOUR REGISTRATION DETAILS:
                            - REGISTERED NAME: {name}
                            - DATE OF JOINING: {date1}
                            - REGISTERED EMAIL ADDRESS: {receiver_email}"""
                            text = f"Subject: {subject}\n\n{message}"
                            try:
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                print("SENDING GMAIL...")
                                server.starttls() 
                                server.login(sender_email, password)
                                server.sendmail(sender_email, receiver_email, text)
                                print(f"EMAIL SUCCESFULLY SEND TO:{receiver_email}!")
                            except Exception as e:
                                    print(f"\nFailed to send email. Error: {e}")
                            finally:
                                try:
                                        server.quit()
                                except:
                                    pass
                            qry="insert into library values('{}','{}','{}','{}')".format(mem,name,date1,receiver_email)
                            cursor=con.cursor()
                            cursor.execute(qry)
                            if cursor.rowcount>0:
                                    print("record added")
                                    print('-'*75)
                            else:
                                    print("record not added")
                                    print('-'*75)
                    case 2:
                            mem=input('ENTER YOUR MEMBERSHIP ID:')
                            qry="delete from library where membership='{}'".format(mem)
                            cursor=con.cursor()
                            cursor.execute(qry)
                            if cursor.rowcount>0:
                                    print("record deleted")
                                    print('-'*75)
                            else:
                                    print("record not found")
                                    print('-'*75)
                    case 3:
                            acc=input('ENTER YOUR MEMBERSHIP ID:')
                            name=input('enter new name')
                            qry="update library set name='{}' where memberhip='{}'".format(name,acc)
                            cursor=con.cursor()
                            cursor.execute(qry)
                            con.commit()
                            if cursor.rowcount>0:
                                    print("record updated")
                            else:
                                    print("record not updated")
                    case 4:
                            qry="select * from library"
                            cursor=con.cursor()
                            cursor.execute(qry)
                            rows=cursor.fetchall()
                            for i in rows:
                                print('-'*75)
                                print('MEMBERSHIP ID:',i[0])
                                print('NAME:',i[1])
                                print('DATE OF JOINING:',i[2])
                                print('REGESTERED EMAIL ID:',i[3])
                                print('-'*75)
                    case 5:
                            mem=input('ENTER YOUR MEMBERSHIP ID:')
                            qry="select * from library where membership='{}'".format(mem)
                            cursor=con.cursor()
                            cursor.execute(qry)
                            rows=cursor.fetchall()
                            for i in rows:
                                print('-'*75)
                                print('MEMBERSHIP ID:',i[0])
                                print('NAME:',i[1])
                                print('DATE OF JOINING:',i[2])
                                print('REGESTERED EMAIL ID:',i[3])
                                print('-'*75)
                    case 6:
                            con.commit()
                            con.close()
                            a=librarydemo.genlibrary1()
                            print(a)
        else:
            print('not connected')
        return member1

