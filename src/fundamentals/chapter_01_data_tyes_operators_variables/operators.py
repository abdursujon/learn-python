'''Python has total 7 different type of operators. Below all operator is explained with examples'''

print("====Total 7 Arithmetic Operators====")
x = 1918
y = 1153

'''Addition'''
# reverse x 
rev_x = int(str(x)[::-1]) # [::-1] reverse the string 
# reverse y
rev_y = float(str(y)[::-1])
sum = int(rev_x + rev_y)
print(sum)

'''Subtraction'''
sub = x - y 
print(sub)

'''Multiplication'''
mul = x * y 
print(mul)

'''Division'''
div = round(x / y, 2) 
print(div)

'''Exponentiation'''
small_y = int(y / 1000)
expo = x**small_y
print(expo)

'''Modulus'''
modu = x % y
print(modu)

''' Floor Division'''
floor_div = x // y
print(floor_div)

print()
print("====Total 14 Assignment operators====")
# equal operator 
x = 5
print(x)

# plus equal 
x += 5
print(x)

# - equal 
x -= 5
print(x)

# devide equal 
x /= 5
print(x) # 5/5 = 1

# modulus equal 
x %= 2
print(x) # 1 % 2 = 1

# floor division equal 
x //= 3
print(x) # 1 // 3, 3 goes 0 times on 1

# exponential equal 
x = 10
x **=2 # sam as x = x ** 2
print(x)

# Bitwise AND assignment operator 
x = 12
y = 5
x &=y # same as x = x & y 

# Bitwise OR operator 
x |= y # same as x = x | y 

# Bitwise XOR operator 
x ^= y # same as x = x ^ y, if both 0 or both 1, result is 0, otherwise 1

# Btiwise Right Shift Assignment Operator 
x = 2 # in bits 0000 0010 
x >>=2 # shift two times gives 0000 0000 which is 0
print(x)

# Bitwise Left Shift Assignment Operator 
x = 2 # 0000 0010
x <<=2 # 0000 1000 which is 8
print(x)

# Walrus Assignment Operator. It assigns values to variables as part of a larger expression
numbers = [1, 2, 3, 4, 5]
# walrus assignment allow us to create the count variable right away with less verbose and assign the value 5 
if (count := len(numbers) > 3):
  print("Numbers list has more than length 3")

i = 300
while i > 0:
  if(allowed := i * i > 5000):
    print("Number is becoming too large")
    break

print()
print("====Total 6 Comparison operators====")
x = 100
y = 200
print(x == y) # false 
print(x != y) # true 
print(x > y) # false 
print(x < y) # true 
print(x >= y) # false
print(x <= y) # true 

print()
print("====Total 3 Logical operators====")
# AND operator, returns true if all condition are true else false 
x = 200
y = 100
if x < 300 and y > 50:
  print("x and y condition met.")

# OR opeartor, if any condition is ture, returns true, otherwise false 
if x >= 200 or y > 100:
  print("at least x or y condition is true")

# NOT operator, reverse the result, if True, becomes False and False > True 
even = [2, 4, 6, 8]
if x not in even: # if x in even is False, NOT makes it True 
  even.append(x)
print(even)

print()
print("====Total 2 Identity operators====")
# is: returns True if both variable are the same object 
fruit = ["apple", "mango"]
fruit2 = fruit
snack = ["chocklate", "kitkat"]
print(fruit is snack)
print(fruit is fruit2)

# is not: returns True if both variables are not the same object 
print(fruit is not fruit2) # false 
print(fruit is not snack) # true 

print()
print("====Total 2 Membership operators====")
# in: returns true if found 
num = [2, 3, 4, 121, 33, 44]
x = 33
if x in num:
  print("x found in num list")

# not in: returns true if not in 
y = 66
if y not in num:
  print("y not foud in num list")

print()
print("====Total 6 Bitwise operators====")
x = 3 & 2 # AND
print(x) 

x = 3 | 2 # OR
print(x)

x = 3 ^ 2 # XOR 
print(x)

x = ~4  # NOT (invert all the bits so 1 becomes 0, 0 becomes 1)
print(x)

# Zero fill left shift: Shift left by pushing zeros in from the right and let the leftmost bits fall off
x = 10<<2 # 10 is 0000 1010 after left shift 2 times it becomes 0010 1000 which is 40
print(x)

# Zero fill right shift 
x = 10>>2 # 10 is 0000 1010 after right shift 2 times it becomes 0000 0010 which is 2
print(x)