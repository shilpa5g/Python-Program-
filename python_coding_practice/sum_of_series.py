# program to find Sum of natural numbers up to given range
terms = int(input("Enter the last term of the series: "))

if terms < 0:
   print("please enter a positive number.")
else:
   sum = 0
  
   for i in range(1, terms+1):
       sum +=i 

   print('sum of series = ',sum)