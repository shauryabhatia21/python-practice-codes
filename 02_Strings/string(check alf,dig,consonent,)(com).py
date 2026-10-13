x=input('enter your input')
v='aeiouAEIOU'
c=0
a1=0
alf=0
dig=0
'''for a in x:
    if a in v:
        c=c+1
    else:
        a1=a1+1
for b in x:
    if b.isalpha():
        alf=alf+1
    elif b.isdigit():
        dig=dig+1'''
for i in x:
    if i.isalpha():
        alf+=1
        if i in v:
            a1+=1
        else:
            c+=1
    elif i.isdigit():
        dig+=1
print("No. of vowels are" ,a1)
print("No. of conconent are" ,c)
print("No. of alphabets are" ,alf)
print("No. of digits are" ,dig)





