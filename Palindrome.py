orig=int(input("Enter a Number: "))
num=orig
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
if orig==rev:
    print(orig,"It is Palindrome")
else:
    print(orig,"is not Palindrome")
