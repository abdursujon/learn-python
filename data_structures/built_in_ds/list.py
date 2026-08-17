items = []
items2 = ["Apple", "Orange", "Coffee"]
items3 = [12, 66.8, "Sugar", 7j]

# 1. append: add an element at the end
items.append(66)
items.append(44)
print(items)

# 2. extend: can be used to add multiple items to the end
items.extend([89, 55])
print(items)

# 3. insert(index, item) use to add item in an index we would like
items.insert(2, 23)
print(items)

# 4. remove(item) 
items.remove(23)
print(items)

#5. pop() remove last item or pop(index)
items.pop()
print(items)
items.pop(1)
print(items)

# 6. index()
print(items.index(66))

# 7. count(item) count how many occurance of an item is in the list
print(items.count(66))

# 8. sort() in achending and decending
items.sort()
print(items)
items.sort(reverse=True)
print(items)

# 9. copy() copy one list to another
copy_items = items.copy()
copy_items.append(77)
print(copy_items) 

# 10. len() to check how many items we have in the list
print(len(items))

# 11. clear()
items.clear()
print(items)