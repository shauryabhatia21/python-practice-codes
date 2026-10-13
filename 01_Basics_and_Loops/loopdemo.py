
#

# 

# '''
# # for i in range(1,11):
# #     print(i)
# '''
# 1
# 2

# # n=int(input('enter value of n'))
# # for i in range(1,n,1):
# #        print(i,end="   ")

# # table of 5
# # n=int(input('Enter no'))
# # # 5*1=5
# # # 5*2=10
# # # 5*2=15

# # # n*i
# # for i in range(1,11):                            
# #     print(f'{n}X{i}={n*i}')

# # for i in range(1,11):
# #     print(f'{5}*{i}={5*i}')
# # take a no and print the list of the no. by which this no. is divisible
# # n=int(input('enter no'))
# # for i in range(1,11):
# #     if n%i==0:
# #         print(i)
    
# # sum of all natural nos
# # n=int(input('enter value of n'))
# # s=0
# # for i in range(1,n+1):
# #     s=s+i 
# # print('sum is's)


# # s=0
# # 0+1=1
# # 1+2=3
# # 3+3=6
# # 6+4=10
# # s=0
# # s=s+i 
# # take a no and check either the enter is perfect no or not
# # no is said to be perfect if
# # 6=1+2+3

# # n=int(input('enter no'))
# # s=0
# # for i in range(1,n):
    
# #     if n%i==0:
# #         s=s+i
# # if s==n:
# #     print('no is perfect')
# # else:
# #     print('not perfect')


# # take a no and print factorial of the no.
# # n=int(input('enter value of n'))
# # s=1
# # for i in range(1,n+1):
    
# #     s=s*i
    
# # print(f'factorial of is {s}')
# '''

# 1*1=1
# 1*2=2

# '''
# # n=int(input('enter value of n'))
# # s=1
# # for i in range(1,n+1):
# #     s=s*i
# #     print(i,"*",end=" ")
    
# # print(f'={s}')
# # take a no and check either the entered no is prime or not
# # s=0
# # n=int(input('enter value'))
# # for i in range(2,n):
# #     if n%i==0:
# #         print('Not a prime no')
# #         s=1
# #         break 
        
# # if s==0:
# #     print('Prime no')

# '''
# for else loop 
# it is a special type of loop in pyton 
# normally we use the else statement with if condition, but when the else statement is given  with for loop 
# statements given in else block will only be execute, if the loop is not break in the middle 


# # for i in range(1,11):
# #     print(i)
# #     if i%20==0:
# #         break 
# # else:
# #     print('demo of for else')


# n=int(input('enter value'))
# for i in range(2,n):
#     if n%i==0:
#         break
# else:
#     print('no is prime')

#     initialize
# while  condition is true:
#     do stome sep 
#     increment/decrement


# '''        

# # i=1
# # while i<=10:
# #     print(i)
# #     i=i+1
# # table of no.s using while loop

# # n=int(input('enter value of n'))
# # i=1
# # while i<11:
# #     print(f'{n}*{i}={n*i}')
# #     i=1+i
# #factorial of no. using while loop
# # n=int(input('enter value of n'))
# # s=1
# # i=1
# # while i<=n:
# #     s=s*i
# #     i=i+1
# # print(f'factorial is {s}')
# '''
# take a number from the user and print the sum of digits of the number
# 195
# 1+9+5
# 3 step process
# 1. extract digit
# 195%10=5
# 19%10=9
# 1%10=1
# 2. use digit
# 0+5=5
# 5+9=14
# 14+1=15
# 3. reduce no
# 195//10=19
# 19//10=1
# 1//10=0
# '''

# # n=int(input('Enter no'))
# # s=0
# # while n>0:
# #     a=n%10
# #     s=s+a
# #     n=n//10
# # print('sum of digits are',s)

# #sum of only even digits in the no.
# # n=int(input('Enter value of n'))
# # s=0
# # while n>0:
# #     a=n%10
# #     if a%2==0:
# #         s=s+a
# #     n=n//10

# # print('sum of even digits is',s)
# # take a no and check either the enetered no is armstrong no or not
# # no is said to be armstrong if the sum of cube of indiv digit of the no. = no. for eg 153=1^3+5^3+3^3

# # n=int(input('Enter value of n'))
# # s=0
# # p=n
# # while n>0:
# #     a=n%10
# #     s=s+(a**3)
# #     n=n//10
# # if s==p:
# #     print('no is armstrong',s)
# # else:
# #     print('not armastrong',s)

# # reverse of no 195=591
# n=int(input('Enter value of n'))
# s=0
# while n>0: #235>0        23>0     2>0
#     a=n%10  # 235%10=5   23%10=3  2%10=2
#     s=s*10+a # 0*10+5=5   5*10+3=53*10+2=532
#     n=n//10  #235//10=23//10=2//10
# print('Reverse is',s)


# # 135
# # 0*10+1=1
# # 1*10+3=13
# # 13*10+5=135

# # 0*10+digit

 
# take infinite no.s


# count=even=odd=0
# while True:
#    a=int(input('Enter no'))
#    if a<0:
#       break 
#    count+=1
#    if a%2==0:
#       even+=1
#    else:
#       odd+=1
# print(odd,even)
# print('Total no entered are ',count)


'''
nested loop i.e. loop with in loop 
one is called outer loop and another is called inner loop 
inner loop will run for each steop of outer loop 
'''


#n=int(input('enter value of n'))  
# p=n  
# for i in range(1,n+1):
#     n=i
#     s=0
#     while n>0:
#         a=n%10
#         s=s+(a**4)
#         n=n//10
#     if s==i:
#             print(f'{s} is armastrong')

'''
functions in python 
functions are the complete program in itself that works on the concept
of reusability that is write once and use again and again 
sometimes some problems are of repetitive nature, we have two solution
for it 
1. write the solution again and again 
2. write once and use again again 
functions works on second approach
that is write once and use again and again 
syntax of using the functions are 
def functionname(argument):
    body of function 
'''

n=int(input('Enter no'))
s=1
for i in range(1,n+1):
    s=s*i
print('Factorial is',s)
print('gOOD dAY')
print('welome')
n=int(input('Enter no'))
s=1
for i in range(1,n+1):
    s=s*i
print('Factorial is',s)
# '''
# def calFact(n):
#     s=1
#     for i in range(1,n+1):
#         s=s*i
#     print('Factorial is',s)

# x=int(input('eNTER NO'))
# calFact(x)
# print('God Day')
# print('welcome')
# x=int(input('eNTER NO'))
# calFact(x)

# def sumofdigits(n):
  
#   s=0    
#   while n>0:
#     a=n%10
#     s=s+a
#     n=n//10
#   print('sum of digits is',s)
# k=int(input('enter no'))
# sumofdigits(k)    

# def greaterno(a,b):
#     if a>b:
#         print(a,'is greater')
#     elif a==b:
#      print("a=b")
#     else:
#         print(b,'is greater')
# x=int(input('enter no 1'))
# z=int(input('enter no 2'))
# greaterno(x,z)
# f=int(input('enter f'))
# g=int(input('enter g'))
# greaterno(f,g)

# calculator


# def calculate(a,b,c):
#  if c=='+':
#   res=a+b
#   print('sum is ',res)
#  elif c=='-':
#   res=a-b
#   print('a-b=',res)
#  elif c=='*':
#   res=a*b
#   print('product is',res)


# x=int(input('enter x'))
# z=int(input('enter z'))    
# opr=input('Enter operatiron')
# calculate(x,z,opr)

# main  menu
import sys

def sumofdigits(n):
    s=0
    while n>0:
        a=n%10
        s=s+a
        n=n//10
    print('sum of digits',s)
def greatestin3(a,b,c):
    if a>b>c:
        print(a,'is greatest')
    elif a<b<c:
        print(c,"is greatest")
    elif a<b>c:
        print(b,' is greatest')
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print('Not a prime no')
            break
    else:
        print('no is prime')
def reverse(n):
    s=0
    while n>0:
        a=n%10
        s=s*10+a
        n=n//10
    print('reverse of a no is',s)
while True:

    print('Main Menu')
    print('1.sum of digits')
    print('2.Greatest in 3 no.s')
    print('3.Prime no')
    print('4.reverse of no.')
    print('5.exit')
    choice=int(input('enter your choice'))
    if choice==1:
        x=int(input('enter no for sum of digits'))
        sumofdigits(x)
    elif choice==2:
        f=int(input('enter f'))
        g=int(input('enter g'))
        h=int(input('enter h'))  
        greatestin3(f,g,h)       
    elif choice==3:
        x=int(input('enter no to check prime')) 
        prime(x)              

    elif choice==4:
        k=int(input('enter no for reverse'))
        reverse(k)         
    elif choice==5:
        sys.exit(0)





        # {WHILE LOOOP CODES}
# 1.[write factors of the given number]


    













    


         
         
         


    
               

                
