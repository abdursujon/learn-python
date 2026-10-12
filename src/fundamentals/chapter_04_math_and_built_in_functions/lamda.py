from functools import reduce

'''
Lambda functions are small anonymous functions (no defined name).
They are used to pass simple logic to another function.
- Contain only one expression.
- The result is returned automatically (no return keyword).

Format: name = lambda arguments: expression
'''

# ===== Basics =====
# cost is an int, price_with_vat takes a and returns a with 20% VAT added
cost = 90
price_with_vat = lambda a: a + (a * 20) / 100
print(price_with_vat(cost))  # 108.0

add = lambda a, b: a + b
print(add(1, 4))  # 5

# ===== Use cases =====
# 1. Condition checking
check_num = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check_num(int(input("Enter an integer: "))))

# 2. List of lambdas (n=x binds the current x to each lambda)
doubles = [lambda n=x: n * 2 for x in range(1, 11)]
for fn in doubles:
    print(fn())

# 3. Returning multiple results: combine them into a tuple
calc = lambda x, y: (x + y, x - y, x * y, x / y)
print(calc(2, 3))  # (5, -1, 6, 0.666...)

# 4. filter() - keep elements that satisfy a condition
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
print(list(filter(lambda x: x % 2 == 0, nums)))  # even
print(list(filter(lambda x: x % 2 != 0, nums)))  # odd

# 5. map() - apply a lambda to each element
print(list(map(lambda x: x * 2, nums)))
print(list(map(lambda x: x * x, nums)))

# 6. reduce() - combine all elements into a single result
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 24

# 7. sorted() with key
numbers = [1, 2, 3, 4, 5, 6, 7, 8, -10, -2, -565]
print(sorted(numbers, key=lambda x: abs(x)))  # by absolute value

data = [(1, 3), (2, 1), (4, 2)]
print(sorted(data, key=lambda x: x[1]))  # by second element

# ===== Practice =====
# 1. Lambda that takes a number and returns its square
sq = lambda x: x ** 2
print(sq(5))  # 25

# 2. Lambda that takes two numbers and returns the larger one
lg = lambda x, y: max(x, y)
print(lg(3, 7))  # 7

# 3. Sort words by length
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=lambda x: len(x)))

# 4. Keep only even numbers using filter
nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, nums)))

# 5. Pair with the smallest second element
pairs = [(1, 5), (2, 3), (3, 4)]
print(min(pairs, key=lambda x: x[1]))  # (2, 3)

# 6. Pair with the largest second element
print(max(pairs, key=lambda x: x[1]))  # (1, 5)