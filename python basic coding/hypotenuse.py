from math import sqrt
print("enter the height and base of the triangle: ")
a,b = int(input("height: ")),int(input("base: "))
c = sqrt(a*a + b*b)
print("hypotenuse of the triangle is: ",c)