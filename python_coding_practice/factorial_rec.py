def factorial(n):
	if n <= 1:
		return n
	else:
		return n * factorial(n-1)

num = int(input("enter the number to find factorial: "))

if num < 0:
	print("factorial does not exit, please enter a positive number.")
elif num == 0:
	print("factorial of 0 is 1.")
else:
	print("the factorial of",num, "= ", factorial(num))