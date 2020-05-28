def remove_odd(string):
	result = ''
	for i in range(len(string)):
		if i % 2 == 0:
			result = result + string[i]
	return result

str1 = input("enter a string: ")
print(remove_odd(str1))