num=[10,51,2,18,4,31,13,5,23,64,29]
print("list elements are: ",end="\n")
for i in num:
    print(i,end=" ")
    print()
find=int(input("Enter element to search: "))
flag=0
for i in num:
    if i==find:
        flag=1
        break
if flag==1:
    print("Element found at position",num.index(find))
else:
    print("Element not found")
