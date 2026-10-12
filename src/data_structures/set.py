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

'''
A set is an unordered collection of unique, hashable items.
1. No order, no index.
2. Can add/remove items, but items must be immutable.
3. No duplicates.
'''

# Duplicates are ignored
print({"apple", "banana", "apple"})

# True == 1 and False == 0, so only one of each is kept
print({True, 1, True, 1})
print({False, 0, False, 0})

# 1. add() - add an item
s = {1, 88, 34, 22, 90}
s.add(5)
print(s)

# 2. remove() - remove an item, KeyError if not found
s.remove(1)
print(s)

# 3. discard() - remove an item, no error if not found
s.discard(0)
print(s)

# Set operations (return a new set)
s8 = {1, 3, 6}
s9 = {6, 9, 11}

# 4. union() - all items from both
print(s8.union(s9))                 # {1, 3, 6, 9, 11}

# 5. intersection() - items in both
print(s8.intersection(s9))          # {6}

# 6. difference() - items in s8 but not in s9
print(s8.difference(s9))            # {1, 3}

# 7. symmetric_difference() - items in either, but not both
print(s8.symmetric_difference(s9))  # {1, 3, 9, 11}

# 8. issubset() - every item of s10 is in s11
s10 = {9, 11}
s11 = {6, 9, 11}
print(s10.issubset(s11))            # True

# 9. isdisjoint() - no common items
print(s10.isdisjoint(s11))          # False

# 10. update() - add items from another set (in place)
s10 = {1, 2, 3}
s10.update({3, 4, 5})
print(s10)                          # {1, 2, 3, 4, 5}

# 11. copy() - shallow copy
s_copy = s10.copy()
s10.add(99)
print(s_copy)                       # unchanged

# 12. len() and membership: O(1) lookup, the main reason to use sets
print(len(s10))
print(3 in s10)