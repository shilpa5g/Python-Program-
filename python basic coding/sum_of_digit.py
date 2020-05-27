num = int(input("enter a number: "))
sum = 0
while num > 0:
    n = num % 10
    sum += n
    num //= 10
print("sum of the digit: ",sum)