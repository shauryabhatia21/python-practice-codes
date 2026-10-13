x='itskills'
#01234567
print(x)
print(x[0])#i
print(x[-1])#s

for i in range(0,len(x)):
    print(x[i])

for  a in x:
    print(a)

# String Methods Reference:
# upper()      - will convert the string into upper case
# lower()      - will convert the string into lower case
# capitalize() - will do the first letter capital of the sentence
# title()      - will do the first letter of each word into capital
# isalpha()    - will give true if string is alphabet
# isdigit()    - will give true if string is digit
# islower()    - will give true if string is in lower case
# isupper()    - will give true if string is in upper case
# isspace()    - will give true if string is space
# isalnum()    - will give true if either the string is alphabet or numeric

x='itskills traing'
print(x.upper())
print(x.lower())
print(x.title())
print(x.capitalize())
