a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
o=input("Enter the operator: ")
if o=='+':
    print(a+b)
elif o=='-':
    print(a-b)
elif o=='*':
    print(a*b)
elif o=='**':
    print(a**b)
elif o=='%':
    print(a%b)
elif o=='/':
    print(a/b)
else:
    print("Invalid option")
