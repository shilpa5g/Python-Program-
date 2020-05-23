#program to find factor of a number

def factor(a):
	print("the factor of",a,"is: ")
	for i in range(1, a + 1):
		if (a % i == 0):
			print(i, end = ", ")

number = int(input("enter a nuber to find factors: "))
print(factor(number))


