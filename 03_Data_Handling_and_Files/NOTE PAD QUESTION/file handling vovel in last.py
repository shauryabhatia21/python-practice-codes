import os
c=0
v='aeiouAEIOU'
os.path.isfile("testing1.txt")
f1=open("testing1.txt","r")
n=(f1.read().split())
print(n)
for a in n:
    if (a[-1]) in v:
        c=c+1
        f1.close
print("No. of vowels are" ,c)
    
