import numpy as np 
# 1. Create without NumPy (nested lists)
matrix = [[1, 3, 5], 
          [2, 4, 6]]
print(matrix)


# 2. Create from given rows and cols
cols, rows = 5, 4
matrix = []
for i in range(rows):
  row = []
  for j in range(cols):
    row.append(j+1)
  matrix.append(row)
print(matrix)


# 3. Create with list comprehension
cols, rows = 9, 9
matrix = [[i+1 for i in range(cols)] for _ in range(rows)]
print(matrix)


# 4. The aliasing trap with [[0]*cols]*rows
bad_matrix = [[0] * 3] * 3 # if we create matrix like this when we update the matrix for any row, it updates the entire column for each row example is give below 
bad_matrix[0][0] = 9 # this sets each row first column to 9 where we tried to only set first row first column to 9 
print(bad_matrix)
# a solution to above problem is to use list comprehension 
good_matrix = [[0] * 3 for _ in range(3)]
good_matrix[0][0] = 9 # now this only updates the first column of first row 
print(good_matrix) 


# 5. Get the number of rows and cols
matrix = [[i+1 for i in range(4)] for _ in range(4)]
num_rows = len(matrix) # number of rows
num_cols = len(matrix[0]) # number of cols 
print("num_rows", num_rows, "num_cols", num_cols)


# 6. Access and change an element
matrix = [[i+1 for i in range(4)] for _ in range(4)]
print(matrix)
matrix[1][3] = 10 # row = 1 and col = 4 (index 0 based)
print(matrix)


# 7. Get a row or a column
matrix = [[2, 4, 5, 6],
          [3, 9, 2, 4], 
          [8, 29, 2, 9]]
print(matrix[1]) # getting row is easy just a number we want 
# get each value in a column of all row 
# for each one_row in matrix, take one_row[1]
col1 = [one_row[1] for one_row in matrix] 
print(col1)
col0 = []
for one_row in matrix:
  col0.append(one_row[0])
print(col0)


# 8. Loop through a matrix
matrix = [[i+1 for i in range(4)] for _ in range(4)]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    print(matrix[i][j], end = " ")
  print()

  
# 9. Print a matrix neatly
matrix = [[i+1 for i in range(9)] for _ in range(9)]
for row in matrix:
  print(" ".join(str(x) for x in row))

  
# 10. Add two matrices
matrix1 = [[i+1 for i in range(9)] for _ in range(9)]
matrix2 = [[i+1 for i in range(9)] for _ in range(9)]
matrix_total = [
  [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
  for i in range(len(matrix1))
]
print(matrix_total)


# 11. Turn rows into column (Transpose)
matrix = [[1, 2, 3],
          [4, 5, 6]]
# zip(*matrix) same as zip([1, 2, 3], [4, 5, 6])
transpose_matrix = [list(row) for row in zip(*matrix)]
print(transpose_matrix)


# 12. Basic NumPy creation (np.array, np.zeros)
numpy_array = np.array([[1, 3, 4], [4, 5, 2]])
print(numpy_array)
print(numpy_array.shape)
numpy_array_with_zero = np.zeros((9, 9))
print(numpy_array_with_zero)
