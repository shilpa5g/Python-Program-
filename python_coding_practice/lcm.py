# Python Program to find the L.C.M. 

def compute_lcm(a, b):

   if a > b:
       greater = a
   else:
       greater = b

   while(greater > 0):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("enter the first number: ")) 
num2 = int(input("enter the second number: ")) 

print("The L.C.M. of",num1,"and",num2, "is", compute_lcm(num1, num2))