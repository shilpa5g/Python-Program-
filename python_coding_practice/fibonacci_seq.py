# Program to display the Fibonacci sequence up to Nth term using loop

terms = int(input("enter the last terms of the series: "))

n1 = 1
n2 = 1
count = 0

if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1, end = ', ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1