values = input("enter some numbers with comma-seprated: ")

list = values.split(",")
tuple = tuple(list)
set = set(list)

print("list : ", list)
print("tuple : ", tuple)
print("set : ", set)