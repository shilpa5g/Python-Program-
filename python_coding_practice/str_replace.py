def mix_up(str1, str2):
	new_str1 = str2[:-1] + str1[-1]
	new_str2 = str1[:-1] + str2[-1]

	return new_str1 +" "+new_str2

print(mix_up('worlo', 'helld'))