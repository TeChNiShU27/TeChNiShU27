str1=input("Enter line:")
str2="is"
L=str1.split()
cnt=0
for i in L:
    if i==str2:
        cnt+=1
print("Substring is appearing:",cnt)
        
