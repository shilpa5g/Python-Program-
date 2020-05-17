x =  [[1, 1, 6],
     [3, 5, 8],
     [4, 6, 9]]

y =  [[2,  5, 9],
     [12, 34, 6],
     [13, 6, 8]]


result =  [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
    	for k in range(len(y)):

     	    result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r)