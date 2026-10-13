x=input('enter your input')
new=''
for a in x:
    if a.islower():
        new=new+a.upper()
    elif a.isupper():
        new=new+a.lower()
    else:
        new=new
print(new)
