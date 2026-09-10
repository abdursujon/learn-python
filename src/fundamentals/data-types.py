# Python has 8 different categories of data types. They are are built in to the program and can be used without any import.

# 1. Text Type: str
x = "I love coding."
print(type(x))

# 2. Numeric Types: int, float, complex
x = 55
print(type(x))
x = 55.6 
print(type(x))
x = 10 + 55j # j is the imaginary unit, defined as j = √(-1) Or equivalently: j² = -1
print(type(x))

# 3. Sequence Types: list, tuple, range

# list: list is a mutable collection of data which can hold different type of data at the same time and change size dynamically. java equivalent of list is arraylist.
x = [1, 3, 4, "orange", "Banana", 66.6, 9j]
print(x[0]) # access by index 
x.append(99.44) # add item 
x[3] = 66 # modify an item by index 
print(len(x)) # length of the list 
print(x)
print(type(x))

# for each loop to print all item of the list 
for i in x:
    print(i)

# traditional index base loop to print all list item 
for i in range(len(x)):
    print(x[i])

# for loop with enumerate() which pairs each item with its index.
for i, item in enumerate(x):
    print(i, item)

'''
tuple: an ordered, immutable collection of items enclosed in parentheses 
key characteristics are: ordered, immutable, any type of data, and index based 
'''
y = ("Apple", "Orange", 77j, 99.5, 90)
# can not do y[0] = 88 (not mutable)
for i, item in enumerate(y): 
    print(i, item)

'''
range: generates a sequence of numbers 
it can be used as range(start, stop, step)
'''    
print(list(range(6))) # create a number list from 0 to 5 (0 index base)
print(list(range(6, 10))) # range(start, stop) by doing this we can allow range to create list from a start and stop point we would like 
print(list(range(0, 11, 2))) # range(start, stop, step) the additional step we can use to incement however u like, in this case by 2

# 4. Mapping Type: dict (in details is covered in data structure section of the project)
map = {}
list_of_item = [1, 3, 4, "orange", "Banana", 66.6, 9j]
for i in range(len(list_of_item)):
    map[i] = list_of_item[i]
print(map)

# 5. Set Types: set, frozenset

# set: unique collection of item wraped around in curly brace which are not ordered so can be access by index 
set_of_item = {"11", 88, 99, 99} ## won't consider second 99 
set_of_item.add(66) # is mutable and we can add item 
print(set_of_item)

#frozenset: a set which is not mutable 
set_of_item = frozenset({"11", 88, 99, 99})
# can not do : set_of_item.add(66)

# 6. Boolean Type: bool 
is_student = True
is_working = False
print(is_student, is_working)

# 7. Binary Types: bytes, bytearray, memoryview
'''bytes: store ASCHII value of data which are used in some cases such as storing binary data(image, audio, video), 
network communication, File I/O in binary mode, encode/ decode. byte is not mutable, meaning we can do data[0] = 66 (change A to B in this case)
'''
data = b"Apple"
print(data[0]) # print aschii value of A 

'''bytearray: is mutable and can be change after creation
''' 
data = bytearray(b"Hell")
data[0] = 99 # Hell becomes cell 
print(data)
data.append(115)
print(data)

''' 
memoryview: memoryview provides efficient access to bytes without copying data.
why memoryview type exist: When we access bytes repeatedly, memoryview avoids making copies (memory efficient):
data[i]     # Python overhead: check bounds, convert to int, return
view[i]     # Direct memory pointer: grab byte and return
'''
data = bytearray(b"Hell")
view = memoryview(data)
print(view)
print(view[0])

# 8. None Type: NoneType: used in function that does not return anything, or something which has no value, or checks if something exists 
x2 = None
print(type(x2))
print(x2)