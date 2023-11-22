from copy import deepcopy

matrix = [[1, 2], [3, 4]]
matrix2 = deepcopy(matrix)
matrix2[0][0] = 10
print(matrix)
