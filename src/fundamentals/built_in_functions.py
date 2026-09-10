import random 

# len() - length
s = "My name is Sujon"
print(len(s))

# max() - maximum value
l = [1, 33, 44, 122, 33]
print(max(l))

# min() - minimum value
l = [1, 33, 44, 122, 33]
print(min(l))

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

# filter() - keep matching elements
l = [1, 33, 44, 122, 33]
odd = list(filter(lambda x: x % 2 != 0, l))
print(odd)

# random built in function 

# 1. random float 0 to 1 
print(random.random())

# 2. random integer between a and b inclusive 
print(random.randint(1, 200))

# 3. Pick a random element from a list 
coutries = ["Bangladesh", "Italy", "England", "India"]
print(random.choice(countries))

# 4. shuffle list 
num = [1, 2, 3, 4, 5]
random.shuffle(num)
print(num)

# 5. Pick k random elements
num = [1, 2, 3, 4, 5, 88, 1, 333, 44]
print(random.sample(num, 5))