num=65
n=int(input("Enter a number:"))
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(num)
        print(ch,end=" ")
    num=num+1
    print("\r")
    
