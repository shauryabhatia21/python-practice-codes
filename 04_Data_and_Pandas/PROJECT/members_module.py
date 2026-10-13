import random
import pandas as pd
def memberMenu():
    try:
        member_df=pd.read_csv('members.csv')
    except Exception as e:
        members={'MEM_ID':['STS123','STS234','STS243'],
                'NAME':['ARSH','RAGHAV','TANMAY'],
                'DOJ':['12/2/23','2/4/25','17/6/24'],
                'STATUS':['ACTIVE','ACTIVE','ACTIVE'] }
        members_df=pd.DataFrame(members)
        members_df.to_csv('members.csv',index=False)
    def genMid():
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=random.randint(0,9)
        return 'STS'+str(a)+str(b)+str(c)
    while True:
        print('1.Add member')
        print('2.Remove member')
        print('3.Modify member')
        print('4.Search member')
        print('5.Display all member')
        print('6.Goto main menu')
        choice=int(input('Enter your choice'))
        if choice==1:
            m_id=genMid()
            mname=input('Enter member name')
            mdoj=input('Enter date of joining')
            status=input('Enter status')

            members_df.loc[len(members_df)]=[m_id,mname,mdoj,status]
            members_df.to_csv('members.csv',index=False)
        elif choice==2:
            mid=input('Enter member id to remove')
            members_df=pd.read_csv('members.csv')
            members_df=members_df.loc[members_df['MEM_ID']!=mid]
            members_df.to_csv('members.csv',index=False)
        elif choice==3:
            mid=input('Enter member id to modify : ')
            df=pd.read_csv('members.csv')
            if mid in df['MEM_ID'].values:
                index=df[df['MEM_ID']==mid].index
                print('Leave blanck if no change required')

                mname=input('Enter New member Name:')
                mdoj=input('Enter New daj :')
                status=input('Enter new status:')

                if mname !='':
                    df.loc[index,'NAME']=mname
                if mdoj !='':
                    df.loc[index,'DOJ']=mdoj
                if status !='':
                    df.loc[index,'STATUS']=status
                df.to_csv('members.csv', index=False)
                print('Member modifed succefully')
            else:
                print('MEMBER Id not found.')
        elif choice==4:
            mid=input('Enter member id to search')
            members_df=pd.read_csv('members.csv')

            result=members_df.loc[members_df['MEM_ID']==mid]
            if result.empty:
                print('Member not found')
            else:
                print(result)
        elif choice==5:
            member_df=pd.read_csv('members.csv')
            print(member_df.to_string(index=False))
        elif choice==6:
            return
        else:
            print('Invalid Choice')
