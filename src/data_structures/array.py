import numpy as np

'''
1. np.append(arr, value)
2. np.concatenate((arr1, arr2))
3. np.insert(arr, index, value)
4. np.delete(arr, index)
5. np.where(arr == value)[0]
6. np.count_nonzero(arr == value)
7. arr[::-1] / np.flip(arr)
8. np.empty(0, dtype=arr.dtype)
9. arr.copy()
10. arr.shape / arr.size / arr.dtype / arr.nbytes
11. arr.tolist()
'''

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

# 1. np.append(arr, value)
# 2. np.concatenate((arr1, arr2))
# 3. np.insert(arr, index, value)
# 4. np.delete(arr, index)
# 5. np.where(arr == value)[0]
# 6. np.count_nonzero(arr == value)
# 7. arr[::-1] / np.flip(arr)
# 8. np.empty(0, dtype=arr.dtype)
# 9. arr.copy()
# 10. arr.shape / arr.size / arr.dtype / arr.nbytes
# 11. arr.tolist()