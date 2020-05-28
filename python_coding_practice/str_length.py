def str_length(string):
	count = 0
	for char in string:
		count += 1
	return count
str1 = input('enter a string: ')
print("length of string is: ")
print(str_length(str1))
