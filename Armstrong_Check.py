num=int(input("Enter 3-digit number: "))
f=num
sum=0
while(f>0):
    a=f%10
    f=int(f/10)
    sum=sum+(a**3)
if(sum==num):
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
