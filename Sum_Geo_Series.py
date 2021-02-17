n=int(input("Enter max value of series: "))
r=float(input("Enter ratio: "))
a=int(input("Enter the first term: "))
#print("\n Series: \n")
sum=0
for i in range(1,n):
    term=a*(r**i)
    sum=sum+term
print("Sum of the series: ",sum)
