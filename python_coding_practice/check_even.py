def check(n):
	if (n % 2) == 0:
		print(n,"is an even number.")
	else:
		print(n,"is an odd number.")

num = int(input("enter a number: "))
print(check(num))