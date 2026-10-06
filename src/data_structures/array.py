import numpy as np

# create an array with data type specified 
num = np.array([90.3, 33.44, 55, 22, 22, 22, 66.2, 66], dtype='float64')
num2D = np.array([[90.3, 33.44, 55, 66.2, 66], [90.3, 33.44, 55, 66.2, 66]])
num3D = np.array(
    [[[1, 2, 3] ,
      [3, 5, 6]], 
     
     [[7, 8, 9], 
      [10, 11, 12]]
    ]
)
print(num)
print(num2D)
print(num3D)

# 1. append() - Add element (returns new array)
# 2. concatenate() - Add multiple elements (like extend)
# 3. insert() - Insert at position
# 4. remove first occurrence of a value (no remove(), find its index then delete)
# 5. pop() - Remove and return last element
# 6. pop(index) - Remove at specified index
# 7. index() - Find position (first match)
# 8. np.count_nonzero(variable == value_wanted) - Count occurrences
count = np.count_nonzero(num == 22)
print(count)
if count > 3:
    print("More than 3 occurence of 22 found")
else: 
    print("<= 3 occurance of 22 found")
# 9. reverse() - Reverse array
# 10. remove all elements - empty array of same type
# 11. copy() - Copy (real copy, not a view)
# 12. info - shape, size, dtype, bytes used
# 13. tofile() - Write to file
# 14. fromfile() - Read from file (must give the same dtype)
# 15. tobytes() - Convert to bytes
# 16. frombuffer() - Read from bytes (like frombytes)
# 17. tolist() - Convert to list
