#program to swap two variables
num1 = int(input("enter the value of first variables: "))
num2 = int(input("enter the value of second variables: "))

print("The value of num1 and num2 before swapping: ")
print("num1 = ", num1)
print("num2 = ", num2)

# take a temporary variable 'temp'
temp = num1
num1 = num2
num2 = temp

print("The value of num1 and num2 after swapping: ")
print("num1 = ", num1)
print("num2 = ", num2)