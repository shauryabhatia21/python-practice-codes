import pickle
import enogenerator1
import os
while True:
    print('***main menue***')
    print('1.Add A customer')
    print('2.Show all Data')
    print('3.Search customer')
    print('4.Remove customer')
    print('5.deposite amount')
    print('5.withdraw amount')
    ch=int(input('enter your choise ='))
    match ch:
        case 1:
            eno=enogenerator1.genAcno()
            name=input('enter customer name =')
            type1=input('enter account type=')
            bal=int(input('enter bal ='))
            a1=[eno,name,type1,bal]
            f1=open('customer.dat','ab')
            print('your accoun number is',eno)
            pickle.dump(a1,f1)
            print('='*75)
            f1.close()
        case 2:
            f1=open('student.dat','rb')
            try:
                while True:
                    a1=pickle.load(f1)
                    print('account number is',1[0])
                    print(' customer Name is ',a1[1])
                    print('account type is ',a1[2])
                    print('balance is ',a1[3])
                    print('='*75)
            except Exception as e:
                pass
        case 3:
            f1=open('customer.dat','rb')
            eno=input('enter your account no')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        print('account no is',a1[0])
                        print('Nameof the customer is ',a1[1])
                        print('account type  is ',a1[2])
                        print('ballance is ',a1[3])
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
            f1=open('customer.dat','rb')
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
                os.remove('customer.dat')
                os.rename('temp.dat','customer.dat')
                print('customer Removed Succesfully')
        case 5:
            f1=open('customer.dat','rb')
            f2=open('temp.dat','wb')
            eno=input('enter your account no')
            amount1=input('enter your amount to deposite')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        a1[3]=a1[3]+amount1
                        pickle.dump(a1,f2)
                        f=1
                        print('updated amount',a1)
                    else:
                        pickle.dump(a1,f2)
            except Exception as e:
                pass
            if f==0:
                print('no record found')
            else:
                f1.close()
                f2.close()
                os.remove('customer.dat')
                os.rename('temp.dat','customer.dat')
        case 6:
            f1=open('customer.dat','rb')
            f2=open('temp.dat','wb')
            eno=input('enter your account no')
            amount1=input('enter your amount to withdraw')
            f=0
            try:
                while True:                    
                    a1=pickle.load(f1)
                    if a1[0]==eno:
                        a1[3]=a1[3]-amount1
                        pickle.dump(a1,f2)
                        f=1
                        print('updated amount',a1)
                    else:
                        pickle.dump(a1,f2)
            except Exception as e:
                pass
            if f==0:
                print('no record found')
            else:
                f1.close()
                f2.close()
                os.remove('customer.dat')
                os.rename('temp.dat','customer.dat')
    
