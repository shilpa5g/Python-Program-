# Display the powers of 2 using anonymous function
terms = int(input("enter the number of terms: "))

result = list(map(lambda a: 2 ** a, range(terms)))

for i in range(terms):
   print("2 raised to power",i,"is",result[i])