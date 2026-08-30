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

# 2. list comprehension
# 3. Returning multiple results
# 4. filter()
# 5. map()
# 6. reduce()
