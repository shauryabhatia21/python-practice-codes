import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

import pandas as pd
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
#ADD A RECORD:

ROLLNO=int(input('ENTER YOUR ROLL NO'))
NAME=input('ENTER YOUR NAME')
COURSE=input('ENTER YOUR course')
FEES=int(input('ENTER YOUR FEES'))
df=pd.DataFrame(d1)
df.loc[len(df)]=[ROLLNO,NAME,COURSE,FEES]
print(df)

#SEARCH RECORD:

Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO]
if result.empty:
    print('no record found')
else:
    print("result found")

#REMOVE DATA:



#REMOVE FROM LOC:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df.loc[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#SEARCH SPECIFIC DATA:
Rno=int(input('ENTER YOUR ROLL NO'))
result=df[df['ROLLNO']==RNO,['NAME','COURSE']]
if result.empty:
    print('no record found')
else:
    df=df[df[RNO]!=rno]
result=df.loc[:,['NAME','COURSE']]
print(result)

#MAIN MENUE:
d1={'ROLLNO':[1,2,3,4],'NAME':['shaurya','harsh','arnav','abhay'],'COURSE':['c','c++','java','web'],'FEES':[500,4500,569,789]}
df=pd.DataFrame(d1)
print(df)
while True:
    print('1.ADD STUDENT')
    print('2.REMOVE STUDENT')
    print('3.search student')
    print('4.search student by a given double critriea')
    print('5.display all record by specific coloum')
    print('6.display all records from specific index to given index')
    print('7.display all records from specific index to given index and ')
    print('8.deleate the ecord by drop method')
    print('9.modify course of a particular coloum')
    print('10.modify course of many student')
    print('11.to add a new coloum fees')
    print('12. to add a new coloum fees with a spefic value')
    print('13. to add a new coloum fees with a different value')
    print('14. to add a new coloum fees and set the value of particular colomn')
    print('15.display all')
    print('16. exit')








    




    











             

