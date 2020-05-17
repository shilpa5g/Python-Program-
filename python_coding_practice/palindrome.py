# Program to check if a string is palindrome or not

string = str(input("enter a string: "))

rev_str = reversed(string)


if list(string) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")