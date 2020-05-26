days = int(input("Input days: ")) 
hours = int(input("Input hours: ")) 
minutes = int(input("Input minutes: ")) 
seconds = int(input("Input seconds: "))

time = days*24*60*60 + hours*60*60 + minutes*60 + seconds

print("The total time: ", time,"seconds.")