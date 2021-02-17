num=65
ch=chr(num)
i=int(input("Enter a number: "))
while i>=0:
    j=1
    while j<=i:
        num=num+1
        print(ch,end=" ")
        j=j+1
    print()
    i=i-1
