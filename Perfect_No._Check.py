i=1
s=0
num=int(input("Enter a numer: "))
while i<num:  #for i in range(1,n):
    if num%i==0:
        s+=i
    i=i+1
if s==num:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
