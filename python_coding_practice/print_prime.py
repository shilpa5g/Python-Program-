#program to print prime numbers between an interval

lower_value = 1
upper_value = 100

print("Prime numbers between {} and {} are:".format(lower_value, upper_value))

for n in range(lower_value, upper_value + 1):
   
   if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n , end = ", ")