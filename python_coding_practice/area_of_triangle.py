#this program to find the area of triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

 # semi-perimeter denoted by 's'
s = (a + b + c) / 2
print("the semi-perimeter of the triangle is: ", s)
 
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("the area of the triangle is: ", area)