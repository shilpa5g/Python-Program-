#program to check the which number in list is divisible by 15 

number_list = [12, 34, 65, 23, 45, 49, 90, 40]

result = list(filter(lambda x: (x % 15 == 0), number_list))

print("numbers divisible by 15 are: ", result)