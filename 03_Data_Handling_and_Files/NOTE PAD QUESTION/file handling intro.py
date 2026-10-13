import os

if os.path.isfile("myfile.txt"):
    f1=open("myfile.txt","r")
    n=f1.read()
    print(n)
else:
    print("file not exist")

'''
open() is used to open the file
file can be opened in different modes
r #read mode
w #write mode
a #append mode
b #binary mode

rb #read and binary mode
wb #write and binary mode

ab #append and binary mode

r+b #read and write both first read and then write in binary mode
w+b #write and read first write and then read in binary mode

read()#is use to read from the file and it will give string as an output
read(n)#will read n number of characters from the file
readline()#will read one line at a time and will give string as an output
readlines()#will read all the lines and will give list of lines as an output
'''
