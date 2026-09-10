'''
Lambda functions are small anonymous functions, meaning they do not have a defined name.
These are small, short-lived functions used to pass simple logic to another function.
- Contain only one expression.
- Result of that expression is returned automatically (no return keyword needed)
'''

'''
Explanation:
'cost' store the int value
'price_with_vat' is a lambda function that takes an argument
a and returns total price with 20% VAT added.
price_with_vat(cost) call applies the lambda to cost, and returns expected value
format of lambda: function name = lambda keyword + argument : expression
'''
cost = 90
price_with_vat = lambda a : a + (a * 20) / 100
print(price_with_vat(cost))

# Use cases
# 1. Condition checking
check_num = lambda x: "Positive" if x > 0 else "Negative"  if x < 0 else "Zero"
num = int(input("Enter your favourite integer number: "))
print(check_num(num))

# 2. list comprehension: Lambda can be combined with list
# comprehensions to apply the same operation to multiple values in a compact way.
mul = [lambda n=x: n * 2 for x in range(1, 11)]
for i in mul:
    print(i())

# 3. Returning multiple results: Although a lambda can contain only one expression, it can still return multiple results by combining them into a tuple.
calc = lambda x, y: (x + y, x - y, x * y, x / y)
print(calc(2, 3))

# 4. filter(): This function uses a lambda expression to select elements from a list that satisfy a given condition, such as keeping only even numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))

# 5. map(): This function applies a lambda expression to each element and returns a map object. It can be converted to a list using list().
double = map(lambda x: x * 2, nums)
print(list(double))

# 6. reduce(): This function repeatedly applies a lambda expression to elements of a list to combine them into a single result.
from functools import reduce
nums = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, nums)
print(mul)
