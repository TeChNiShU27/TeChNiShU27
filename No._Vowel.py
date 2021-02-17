word=str(input("Enter a word: "))
count=0
for letter in word:
    if letter in ('a', 'e', 'i', 'o', 'u'):
        count=count+1
print(count)
