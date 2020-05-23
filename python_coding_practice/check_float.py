def add_numbers(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
         raise TypeError("Inputs must be float")
    return a + b

print("sum of float numbers: ",add_numbers(10.0, 20.2))