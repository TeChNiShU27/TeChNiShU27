x=float(input("Enter value of x: "))
y=int(input("Enter limit: "))
s=0
for i in range (0,x+1):
    fact=1
    for k in range (1,i+1):
        fact=fact*k
    s+=(-x**i)/fact(i)
print(s)
