import random 

# len() - length
s = "My name is Sujon"
print(len(s))

# max() - maximum value
l = [1, 33, 44, 122, 33]
print(max(l))
print(max(3, 7))

# min() - minimum value
l = [1, 33, 44, 122, 33]
print(min(l))
print(min(4, 22))

# sum() - total
l = [1, 33, 44, 122, 33]
print(sum(l))

# enumerate() - index + value
fruits = ["apple", "banana", "cherry"]
for index, name in enumerate(fruits):
    print(index, name)

# zip() - combine lists
names = ["Tiger", "Fox", "Snake"]
countries = ["Bangladesh", "England", "India"]
for name, country in zip(names, countries):
    print(name, country) 

# map() - apply a lambda expression to all given element 
l = [1, 33, 44, 122, 33]
mul = list(map(lambda x: x * 2, l))
print(mul)

# filter(exp, arg) - keep matching elements
l = [1, 33, 44, 122, 33]
odd = list(filter(lambda x: x % 2 != 0, l))
print(odd)

# sorted(arg) 
nums = [-10, 3, 11, 33]
nums = sorted(nums)
print(nums)