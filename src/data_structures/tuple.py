'''tuple
built in methods: 
1. index
2. count
'''
print(dir(tuple))
nums = (1, 2, 3, 3, 4, 2, 2, 45, 3, 1, 2)
count_2 = nums.count(2)
print(nums[2]) # allowed 
# nums[2] = 23 editing not allowed in the same tuple
print(count_2)
index_2 = nums.index(2)
print(index_2)
indexes = [i for i, x in enumerate(nums) if x == 2]
print(indexes)

# 1. Create a tuple with one element and print its type.
t = (3,)
print(type(t))

# 2. Given t = (1, 2, 3), change the second element to 20.
t = (1, 2, 3)
t = t[:1] + (20,) + t[2:]
print(t)

l = list(t)
l[1] = 20
t = tuple(l)
print(t)

# 3. Given t = (1, [2, 3], 4), append 5 to the inner list. Does it work? Why?
t = (1, [2, 3], 4)
l = list(t)
x = l[1]
x.append(5)
t = tuple(l)
print(t)
print(type(t))

# 4. Given t = (1, 2, 3, 4, 5), unpack it in one line into three variables:
#    a    -> first element (1)
#    b    -> second element (2)
#    rest -> all remaining elements (3, 4, 5)
t = (1, 2, 3, 4, 5)
a, b, rest = t[0], t[1], t[2:]
print(a, b, rest)

# 5. Swap two variables x and y in one line without a temp variable.
x = t[0]
y = t[1]
x, y = y, x
print(x, y)

# 6. Given t = (3, 1, 2), return a sorted tuple.
t = (3, 1, 2)
t = sorted(t)
print(t)

# 7. Given a list of tuples [(1, 'b'), (3, 'a'), (2, 'c')], sort it by the second element.
t = [(1, 'b'), (3, 'a'), (2, 'c')] # list consist of tuples 
t = sorted(t, key=lambda x: x[1])
print(t)

# 8. Given t1 = (1, 2) and t2 = (3, 4), produce (1, 2, 3, 4) and (1, 2, 1, 2).
t1 = (1, 2) 
t2 = (3, 4)
t = t1 + t2
print(t)
t = t1 + t1
print(t)

# 9. Can a tuple be a dictionary key? Can a list? Show both.
d = {}
d[t] = 6
l = [2, 3, 4] # can not use list as key in dict in python
l = tuple(l) # convert it to tuple first 
d[l] = 9
print(d.get(t))
print(d.keys())
for k in d.keys():
  if k == t:
    print(k)
  if k == l:
    print(l)
    
# 10. Given nums = (1, 2, 3, 2, 4, 2), return a tuple of the values that appear
# more than once. Each value should appear only once in the result.
# Expected: (2,)
nums = (1, 2, 3, 4, 2, 3, 6, 7)
from collections import Counter
counts = Counter(nums)
print(counts)
result = []
for k in counts.keys():
  if counts[k] > 1:
    result.append(k)
print(result) 
result = tuple(result)
print(result)

# 11. Given t = (1, 2, 3, 4, 5), return the elements in reverse
t = (1, 2, 3, 4, 5)
t = list(t)
t.reverse()
t = tuple(t)
print(t)

# 12. Remove the last element from t = (1, 2, 3, 4) without converting to a list.
t = (1, 2, 3, 4)
print(t[len(t) - 1])