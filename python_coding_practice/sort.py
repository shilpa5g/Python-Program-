string = input("Enter a string: ")


words = string.split()

words.sort()

print("The sorted words are:")
for w in words:
   print(w)