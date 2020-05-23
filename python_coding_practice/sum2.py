'''Sum of two given integers.
 However, if the sum is between 15 to 20 it will return 20'''
def sum(x, y):
 	sum = x + y
 	if sum in range(15, 20):
 		return 20
 	else:
 		return sum

num1 = int(input("x : "))
num2 = int(input("y : "))
print(sum(num1, num2))