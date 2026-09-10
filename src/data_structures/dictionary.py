'''
Dictionary data structure is used to store data in key:value pairs.
1. It is ordered.
2. Item can be change after stored.
3. It does not allow duplicate key:value pair 
It has 11 methods which we can use to manipulate the stored data. 
'''

dictionary_example = {"football": 1863, "cricket": 1598, "basketball": 1891} 

# Adding key:value to a dictionary standard way 
fruits = ["apple", "banana", "orange", "cherry"]
d1 = {}
key = 1
for f in range(len(fruits)):
    d1[key] = fruits[f]
    key += 1
print(d1)


# 1. copy() - Shallow copy means it only copy what exits now, it won't register any update that is made into original map 
d2 = d1.copy()
d1[5] = "Pinapple"
print(d1)
print(d2) # d2 is unchanged


# 2. fromkeys() - Create dict from keys
d3 = dict.fromkeys(["apple", "banana", "orange", "cherry"], 0)
print(d3)
# on purpose of this method is that we can use it to count items, we can start with 0 then count elements 
fruits = ["apple", "banana", "orange", "cherry", "banana", "orange", "cherry"]
for f in fruits: 
    if f in d3:
        d3[f] += 1
print(d3)


# 3. get() - Get value (no error if missing)
for i in d3: 
    print(d3.get(i))

# 4. items() - Return key-value pairs
print(d3.items())

# 5. keys() - Return all keys
print(d3.keys())

# 6. values() - Return all values
print(d3.values())

# 7. pop() - Remove and return value of a key (returns error if does not exits)
print(d3.pop("apple"))

# 8. popitem() - Remove and return last item (if dictionary is empty, popitem will return error)
print(d3.popitem())

# 9. setdefault() - Get value of a key, set value if missing
print(d3)
d3.setdefault("apple", 4) # will add key apple and value 4
d3.setdefault("orange", 4) # won't change anything because the key "orange" already exists
print(d3)

# 10. update() - Add/update from another dict
d4 = {}
d4.update(d3)
print(d4) # d4 and d3 has same key:values 

# 11. clear() - Remove all items
d4.clear()
d3.clear()
print(d3)
print(d4)