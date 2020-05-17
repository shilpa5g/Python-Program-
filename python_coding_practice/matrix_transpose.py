x =  [[2,  5, 9],
     [12, 34, 6],
     [13, 6, 8]]


result =  [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):

     	result[i][j] = x[j][i] 
for r in result:
    print(r)
