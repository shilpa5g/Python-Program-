vowels = 'aeiou'

string = input(" enter a string: ")
string = string.casefold()
count = {}.fromkeys(vowels,0)

for c in string:
   if c in count:
       count[c] += 1

print(count)
