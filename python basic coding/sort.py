n1,n2,n3 = int(input("n1: ")),int(input("n2: ")),int(input("n3: "))
a = min(n1,n2,n3)
c = max(n1,n2,n3)
b = ((n1+n2+n3)-a-c)
print("sorted form: ",a,b,c)