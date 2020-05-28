def str_change(string):
	return string[-1] + string[1:-1] + string[0]

str1 = input("enter a string: ")
print(str_change(str1))