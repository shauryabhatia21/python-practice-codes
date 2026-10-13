import os
c=0
v='the'
os.path.isfile("testing1.txt")
f1=open("testing1.txt","r")
n=(f1.read().split())
print(n)
for a in n:
    if a in v:
        c=c+1
print("No. of the = " ,c)

