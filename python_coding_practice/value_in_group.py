#program to check whether a specified value is contained in a group of values

def value_of_group(data, n):
	for value in data:
		if n == value:
		    return True
		
	return False
group = [1, 3, 5, 7, 8, 16]
num = int(input("enter a number: "))
print(value_of_group(group, num))