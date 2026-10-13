'''
1. d.copy()
2. dict.fromkeys(keys, value)
3. d.get(key) / d.get(key, default)
4. d.items()
5. d.keys()
6. d.values()
7. d.pop(key)
8. d.popitem()
9. d.setdefault(key, default)
10. d.update(other_dict)
11. d.clear()

Dictionary data structure is used to store data in key:value pairs.
1. It is ordered.
2. Item can be change after stored.
3. It does not allow duplicate key 
'''

items_map = {}

# *** adding items in dict ***
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
items = ["apple", "orange", "buscuit", "chocklate", "cereal", "milk", "egg", "butter", "banana", "sugar"]
for id, item in zip(ids, items):
  items_map[id] = item 
print(items_map)
# delete a key 
del items_map[10]
print(items_map)
# looping dict 
count_how_many_id = 0
add_id = 0
for item in items_map:
  count_how_many_id += 1
  add_id += item
print(count_how_many_id)
print(add_id)
# check if key exist 
nums = [9, 12, 13, 1, 2]
for n in nums:
  if n in items_map:
    print("True")
  else:
    print("False")
    
# 1. d.copy()
items_map_two = items_map.copy()
items_map_two[11] = "bun"
items_map_two[12] = "bread"
print(items_map_two)

# 2. dict.fromkeys(keys, value) we can use this to pass keys with all default value such as empty string, or just zero 
items_map_three = dict.fromkeys(ids, "")
print(items_map_three)
# now we can use that map to add values 
for id, item in zip(ids, items):
  items_map_three[id] = item
print(items_map_three)

# 3. d.get(key) / d.get(key, default)
print(items_map.get(12))
print(items_map.get(12, 0))
print(items_map.get(3))

# 4. d.items()
for key, value in items_map.items():
  if key == 10:
    items_map[key] = "coffee"
  if items_map[key] == "butter":
    items_map[key] = "potato"
print(items_map)

# 5. d.keys()
for key in items_map.keys():
  if key == 5:
    items_map[key] = "protein bar"
print(items_map)
ids.sort(reverse=True)
items_map = dict(zip(ids, items_map.values()))
print(items_map)

# 6. d.values()
for k, v in zip(items_map.keys(), items_map.values()):
  items_map[k] = v[::-1]
print(items_map)
for k, v in zip(items_map.keys(), items_map.values()):
  items_map[k] = "".join(reversed(v))
print(items_map)
  
# 7. d.pop(key) remove item of a dict by key 
items_map.pop(10)
print(items_map)

# 8. d.popitem() removes last inserted item 
items_map.popitem()
print(items_map)

# 9. d.setdefault(key, default)
ids.sort()
items_map_four = {}
for i in ids:
  items_map_four.setdefault(i, "")
print(items_map_four)

# 10. d.update(other_dict)
items_map_four.update(items_map)
print(items_map_four)

# 11. d.clear()
items_map.clear()
print(items_map)