string=input("Enter a string: ")
length=len(string)
print("Original string: ",string)
string_2=""
for a in range(0, length):
    if a%2==0:
        string_2+=string[a]
    else:
        string+=string[a].capitalize()+" "   
print(string_2)
