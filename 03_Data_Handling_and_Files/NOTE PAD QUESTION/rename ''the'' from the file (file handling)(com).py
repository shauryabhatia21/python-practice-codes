import os
k=0
v=['the','THE','The']
f1=open("testing1.txt","r")
n=f1.read().split()
k=''
for a in n:
    if a not in v:
        k=a+' '
f2=open("testing1.txt","w")
f2.write(k)
print(k)
f2.close()



