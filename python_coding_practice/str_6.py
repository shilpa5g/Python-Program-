def add_str(string):
	length = len(string)

	if length > 2:
		if string[-3:] == 'ing':
		    string += 'ly'
		else:
			string += 'ing'

	return string
str1 = input("enter string: ")
print(add_str(str1))