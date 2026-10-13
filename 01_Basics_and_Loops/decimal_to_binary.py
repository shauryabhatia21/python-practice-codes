num = int(input("Enter a decimal number:"))

if num == 0:
    print("Binary:0")
else:
    n=num
    binary=""
    while n > 0:
        binary = str(n%2)+binary
        n=n//2                     
    print("Binary:",binary)
