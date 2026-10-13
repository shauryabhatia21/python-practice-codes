from Books_module import *
from members_module import *
from issue_module import *
import sys
def mainMenu():
    while True:
        print('1.Go to book menue')
        print('2.Go to member menue')
        print('3.Go to issue/return menue')
        print('4.Go to report menue')
        print('5.Exit')
        ch=int(input('enter your choise'))
        if ch==1:
            booksMenu()
        elif ch==2:
            members_module()
        elif ch==3:
            issue_module()
        elif ch==4:
            pass
        elif ch==5:
            sys.exit



