# Program to display Armstrong numbers within an interval

lower = 1
upper = 1000

for num in range(lower, upper + 1):

   
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if num == sum:
       print(num)