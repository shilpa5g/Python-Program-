# Python program to find H.C.F 

def compute_hcf(a, b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("enter the first number: ")) 
num2 = int(input("enter the second number: ")) 

print("The H.C.F. is", compute_hcf(num1, num2))