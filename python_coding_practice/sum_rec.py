def sum(n):
	if n <= 1:
		return n
	else:
		return n + sum(n-1)

num = int(input("enter the last terms of the series: "))

if num < 0:
	print("please enter a positive number.")
else:
	print("the sum is: ", sum(num))