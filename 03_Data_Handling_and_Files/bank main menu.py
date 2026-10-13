import sys
import accgenerator
customer=[]
while True:
    print('**WELCOME IN KOTAK MAHINDRA BANK**')
    print('1.add account')
    print('2.deposite money')
    print('3.withdraw money')
    print('4.search account')
    print('5.close account')
    print('6.display all data')
    print('7.exit')
    ch=int(input('enter your choise'))
    match ch:
        case 1:
            acc=accgenerator.genAcno()
            print('Your Account Number',acc)
            name=input('Enter Customer Name')
            typ=input('Enter Account Type')
            bal=int(input('Enter Account Balance'))
            a1=[acc,name,typ,bal]
            customer.append(a1)
            print('Data Succesfully Uploaded')
            print('='*75)
        case 2:
            v=int(input('Enter Account Number'))
            for x in customer:
                if v==x[0]:
                    amount=int(input('Enter Amount You Want To Deposit'))
                    x[3]=x[3]+amount
                    print('-'*75)
                    print('Updated Balance is',x[3])
                    print('Account Balance Updated Succesfully')
                    print('='*75)
                    break
            else:
                print('Record Not Found')
                
        case 3:
            v=int(input('Enter Account Number'))
            for x in customer:
                if v==x[0]:
                    amount=int(input('Enter Amount You Want To Withdraw'))
                    x[3]=x[3]-amount
                    print('-'*75)
                    print('Updated Balance Is',x[3])
                    print('Account Balance Updated Succesfully')
                    print('='*75)
                    break
            else:
                print('Record Not Found')
                
        case 4:
            v=int(input('Enter Account Number'))
            for x in customer:
                if v==x[0]:
                    print('Custmer Name',x[1])
                    print('Account Type',x[2])
                    print('Account Balance',x[3])
                    print('All Information Displayed')
                    print('='*75)
                    break
            else:
                print('Record Not Found')
        case 5:
            v=int(input('Enter Account Number'))
            for x in customer:
                if v==x[0]:
                    a1.clear()
                    print('Bank Account Hass Been Closed')
                    print('='*75)
                    break
        case 6:
            for x in customer:
                print('Account Number',x[0])
                print('Name Is',x[1])
                print('Account Type Is',x[2])
                print('balance is',x[3])
                print('All Student Name Printed')
                print('='*75)
                break
        case 7:
            print('The Data Has Been Stored')
            print('THANK YOU FOR VISIT')
            sys.exit(0)
                            
                
                    
                              
                
                
                
                    
                    
                    
                
            
            
        
