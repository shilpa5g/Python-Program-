# program to get the n copies of the given string

def string_copy(str , n):
	result = ""
	for i in range(n):
		result = result + str
	return result

str1 = input("enter a string: ")
copies = int(input("enter the number of copies: "))
print(string_copy(str1 ,copies))

