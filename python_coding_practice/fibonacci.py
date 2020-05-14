def fib(n):
    if n <= 1:
        return n
    else:
        return(fib (n - 1) + fib(n - 2))

terms = int(input("enter the number of terms of the series: "))
if terms <= 0:
    print("please enter postive number........")
else:
    print("fibonacci sequence : ")
    for i in range(terms):
        print(fib(i))
