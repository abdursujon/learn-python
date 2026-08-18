from array import array 
import copy 
'''array types
'i' = integer
'f' = float 
'd' = double 
'b' = signed type  
'''

# create array("type", [values])
a = array('d', [98.7, 44.7, 22, 11, 11.0])
print(a)

# array methods in python

# 1. append() - Add element
a.append(33.4)
print(a)

# 2. extend() - Add multiple elements
a.extend([5, 3, 1])
print(a)

# 3. insert() - Insert at position
a.insert(0, 99.4)
print(a)

# 4. remove() - Remove first occurrence
a.remove(33.4)
print(a)

# 5. pop() - Remove and return element
a.remove(99.4)
print(a)

# 6. pop(index) - Remove at specified index
a.pop(1)
print(a)

# 7. index() - Find position
print(a.index(22.0))

# 8. count() - Count occurrences
print(a.count(11.0))

# 9. reverse() - Reverse array
a.reverse()
print(a)

# 10. del array[:] - Remove all elements
del a[:]
print(a)

# 11. copy() - Shallow copy
a = array('i', [1, 34, 22, 14, 55])
a2 = copy.copy(a)
print(a2)

a3 = array('i', a) # second way to copy one array to another 
print(a3)

# 12. buffer_info() - Get info
print(a.buffer_info())  # (address, length) **

# 13. fromfile() - Read from file
a1 = array('i', [993, 33, 122, 334, 666])
print(a1)
with open('data.bin', 'wb') as f: 
    a1.tofile(f)

# 14. tofile() - Write to file
a2 = array('i')
with open('data.bin', 'rb') as f: 
    a2.fromfile(f, 5)
print(a2)

# 15. tobytes() - Convert to bytes
print(a2.tobytes())
b = a2.tobytes()

# 16. frombytes() - Read from bytes
a4 = array('i')
a4.frombytes(b)
print(a4)

# 17. tolist() - Convert to list
a = array('i', [4, 5, 6, 33])
array_to_list = a.tolist()
print(array_to_list)