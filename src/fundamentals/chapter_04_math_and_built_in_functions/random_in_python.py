import random 

# 1. choice(data)
nums = [1, 89, 331, 11]
random_choice = random.choice(nums)
print(random_choice)

# 2. choices(data, limit)
random_choices = random.choices(nums, k=5)
print(random_choices)

# 3. randint(start, end) start and end includes
random_int = random.randint(4, 9)
print(random_int)

# 4. random() - limit > 0 and < 1
random_float = random.random()
print(random_float)
# value is x > 0 and x < 10
random_float = random.random() * 10
print(random_float)

# 5. randrange(start, end) returns a number where start is included and end is excluded
random_range = random.randrange(2, 8)
print(random_range)

# 6.sample(data, limit)
nums = [1, 89, 331, 11]
random_sample = random.sample(nums, k=3)
print(random_sample)

# 7. shuffle(data)
nums = [1, 89, 331, 11]
random.shuffle(nums)
print(nums)