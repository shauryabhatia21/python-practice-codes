import sys
import issuemain
import librarymain
import membermain
import sys
while True:
        print('***[LIBRARY MAIN MENUE]****')
        print('1.OPEN MEMBERS TAB')
        print('2.OPEN BOOKS TAB')
        print('3.OPEN BOOK ISSUE TAB ')
        print('4.EXIT')
        print('-'*75)
        ch=int(input('ENTER YOUR CHOISE:'))
        match ch:
            case 1:
                print('-'*75)
                a=membermain.genmember()
                print(a)
                print('-'*75)
            case 2:
                print('-'*75)
                a=librarymain.genlibrary()
                print(a)
                print('-'*75)
            case 3:
                print('-'*75)
                a=issuemain.genissue1()
                print(a)
                print('-'*75)
            case 4:
                print('*'*75)
                print('YOUR DATA HAS BEEN STORED')
                print('*'*75)
                sys.exit()
