'''
frozenset: frozen is is immutable meaning we can not add or remove elements after it has been created
Use casees: 
1. Use as dictionary keys (set can't be use as dictionary keys but frozen works)
2. If we need immutable set 
'''
fs = frozenset([1, 3, 8])
print(fs)

d = {frozenset([1, 3]): "items one"} # we can do this 
# but we can not use list or set as key in dictionary for example 
# d = {[1, 3]: "List items one"} is invalid
# d = {{1, 3]}: "Set items one"} is invalid
print(d)
print(type(d))

# Read only method works as normal like set such as 
fs2 = fs.copy()
print(fs2)
print(1 in fs2)
print(len(fs2))

# set operation works normally 
fs3 = {9, 11}
fs4 = {6, 9, 11}
print(fs3.issubset(fs4))   # Check if s1 is subset of s2  or s1 <= s2
print(fs3.issuperset(fs4))  # Check if s1 is superset of s2  or s1 >= s2
print(fs3.isdisjoint(fs4))  # Check if no common elements

''' Set Operations works normally as well''' 
fs5 = {1, 3, 6}
fs6 = {6, 9, 11}

print(fs5.union(fs6)) # {1, 3, 6, 9, 11}
print(fs5.intersection(fs6)) # {6}
print(fs5.difference(fs6)) # s8 - s9 = {1, 3} elements remainded in second set does not count
print(fs5.symmetric_difference(fs6)) # s8 - s9 = {1, 3, 9 , 11} elements remainded in second set counts as well

# method clear() works normally 
fs5.clear()
print(fs5)