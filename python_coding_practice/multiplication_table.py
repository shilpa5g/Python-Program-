num = int(input("enter a number to display multiplication table: "))

for i in range(1, 11):
   print("{} X {} = {}".format(num, i, num*i))