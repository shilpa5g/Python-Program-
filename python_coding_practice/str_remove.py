def remove(string, n):
	part1 = string[:n]
	part2 = string[n+1:]

	return part1 + part2

str1 = input("enter a string: ")
num = int(input("enter the number of index: "))
print(remove(str1, num))