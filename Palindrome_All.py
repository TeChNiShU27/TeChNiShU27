my_str=str(input("Enter a Word: "))
my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")
