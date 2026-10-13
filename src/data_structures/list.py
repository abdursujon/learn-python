'''
1. lst.append(item)
2. lst.extend(iterable)
3. lst.insert(index, item)
4. lst.remove(item)
5. lst.pop() / lst.pop(index)
6. lst.index(item)
7. lst.count(item)
8. lst.sort() / lst.sort(reverse=True)
9. lst.copy()
10. len(lst)
11. lst.clear()
'''

nums = []
# 1. lst.append(item)
i = 0
while i <= 10:
  nums.append(i ** 2)
  i += 1
print(nums)

# 2. lst.extend(otherdata)
nums2 = [i**3 for i in range(0, 10)] 
print(nums2)
nums.extend(nums2)
print(nums)

# 3. lst.insert(index, item)
nums.insert(0, 0)
print(nums)

# 4. lst.remove(item)
nums.remove(0)
print(nums)

# 5. lst.pop() / lst.pop(index)
nums.pop()
print(nums)
nums.pop(0)
print(nums)

# 6. lst.index(item)
print(nums.index(8))

# 7. lst.count(item)
print(nums.count(216))

# 8. lst.sort() / lst.sort(reverse=True)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 9. lst.copy()
nums2 = nums.copy() + nums.copy()
print(nums2)

# 10. len(lst)
print(len(nums2))

# 11. lst.clear()
nums2.clear()
nums.clear()
print(nums)
print(nums2)