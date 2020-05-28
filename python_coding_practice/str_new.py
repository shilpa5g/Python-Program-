def end(string):
	if len(string) < 2:
		return ""

	return string[:2] + string[-2:]
str1 = input("enter string: ")
print("new string: ")
print(end(str1))