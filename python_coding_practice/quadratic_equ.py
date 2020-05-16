# program to Solve the quadratic equation 
import cmath
print("equation - 2X^2 + 3X + 10 = 0")
a = 2
b = 3
c = 10

print("discriminant = b^2 - 4ac")
# discriminant = disc
disc = (b**2) - (4*a*c)
print("discriminant = ", disc)

root1 = (-b + cmath.sqrt(disc)) / (2*a)
root2 = (-b - cmath.sqrt(disc)) / (2*a)

print("The solution are {} and {}.".format(root1,root2))