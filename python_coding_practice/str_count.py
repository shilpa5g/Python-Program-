def str_count(string):
	dict = {}
	for n in string:
		keys = dict.keys()
		if n in keys:
			dict[n] += 1
		else:
			dict[n] = 1
	return dict
hello = input("enter string: ")
print(str_count(hello))
