'''
1. s.add(item)
2. s.remove(item)
3. s.discard(item)
4. s.union(other)          # s | other
5. s.intersection(other)   # s & other
6. s.difference(other)     # s - other
7. s.symmetric_difference(other)  # s ^ other
8. s.issubset(other)
9. s.isdisjoint(other)
10. s.update(other)
11. s.copy()
12. len(s) / item in s
'''

set_one = set()
set_two = set()

# 1. s.add(item)  -> adds one item
i = 0
while i <= 10:
  set_one.add(i**2)
  set_two.add(i**3)
  i+=1
print(set_one)
print(set_two)

# 2. s.remove(item)  -> removes item, KeyError if missing
set_one = list(set_one)
for s in set_one:
  if s > 50:
    set_one.remove(s)
  else:
    continue
set_one = set(set_one)
print(set_one)    

# 3. s.discard(item)  -> removes item, no error if missing
set_one.discard(88)
set_one.discard(9)
print(set_one)

# 4. s.union(other)  # s | other  -> all items from both
set_three = set_one.union(set_two)
print(set_three)

# 5. s.intersection(other)  # s & other  -> items in both
set_three = set_one.intersection(set_two)
print(set_three)
set_four = set_three & set_two
print(set_four)

# 6. s.difference(other)  # s - other  -> items in s not in other
set_four = {0, 1, 64, 4, 36}
set_diff = set_four.difference(set_three)
print(set_diff)

# 7. s.symmetric_difference(other)  # s ^ other  -> items in one set but not both
set_three = {0, 1, 9, 98}
set_four = {0, 1, 64, 4, 36}
print(set_three.symmetric_difference(set_four))

# 8. s.issubset(other)  -> True if all of s is in other
set_three = {0, 1, 36}
set_four = {0, 1, 64, 4, 36}
print(set_three.issubset(set_four))

# 9. s.isdisjoint(other)  -> True if no shared items
set_three = {3, 44,22}
set_four = {0, 1, 4}
print(set_three.isdisjoint(set_four))

# 10. s.update(other)  -> adds all of other into s, in place
set_three.update(set_four)
print(set_three)

# 11. s.copy()  -> shallow copy
set_five = set_four.copy()
print(set_five)

# 12. len(s) / item in s  -> size / membership check
print(len(set_five))
print(5 in set_five)
print(4 in set_five)