print("program to check a number is prime or not.")

num = int(input("please enter a positive number: "))

if (num == 1):
	print("1 is neither prime nor composite number.")

elif(num > 1):
	for i in range(2, int(num/2)):
		if(num % i) == 0:
			print(num,"is not a prime number.")
			break

		else:
			print(num,"is a prime number.")
			break