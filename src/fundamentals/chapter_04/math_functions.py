import math 
# print(dir(math))
# All available methods 
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 
'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print("qube root of 64:", math.cbrt(64))
print("cei of 6.01:", math.ceil(6.01)) # ceil means make it the higher number for any case 
print("200 people handsake each other, how many handshake:", math.comb(200,2))  
print("e to the power 8 is : ", math.e**8)
print("exponential of e to the given power 4: ", math.exp(4))
# flaoting point absolute 
print("flaoting point absolute of -1999.88: ", math.fabs(-1999.88))
print("factorial of 5!:", math.factorial(5))
# floor always remove anything decimal 
print("floor of 88.9: ", math.floor(88.9))
# accurate sum of float number list 
print("accurate some of a float list:", math.fsum([88.999, 0.3333, 0.2222, 19.3]))
print("natural log of 64:", math.log(64))
print("hypotenuse of a traingle given width and height 3 and 4:", math.hypot(3, 4))
print("e value is:", math.e)
print("pi value is:", math.pi)
print("power value of 2 to the power 8:", math.pow(2, 8))
print("power value of 2 to the power 8:", 2**8)
print("product of a give list:", math.prod([1, 2, 3, 4, 5]))
print("sqrt of 64:", math.sqrt(64))
list1 = [1, 3, 4, 8]
list2 = [2, 3, 4, 9]
print("add product of list1, and list2:", math.sumprod(list1, list2))


# ====== Some Practical Examples ====== 
# 1. Total revenue (price × quantity, summed) using one function.
prices = [12.99, 4.50, 7.25, 19.99] # price per item
quantity = [3, 10, 4, 2] # quantity sold 
# method 1: verbose: 
sum = 0
for i in range(len(prices)):
  curr = prices[i] * quantity[i]
  sum += curr
# method 2 with math.sumprod()
total_revenue = math.sumprod(prices, quantity) 
print(total_revenue, sum)

# 2. A floor plan that is 30m wide and 40m long. Find the diagonal distance across it.
floor_diagonal_dist = math.hypot(30, 40)
print(floor_diagonal_dist)

# 3. A cube-shaped storage box with a volume of 343 m³. Find its side length.
print(math.cbrt(343))

# 4. Boxes hold 12 items each. Find how many boxes are needed to pack 499 items.
print("number of box", math.ceil(499/12))

# 5. 15 workers must be paired into teams of 2. Find how many different pairs are possible.
# traditional mathematical way 
n = 15
possible_pair = int(n * (n-1)/2)
print(possible_pair)
# by math functino 
print(math.comb(15,2))

# 6. In how many different orders can 6 delivery trucks leave?
truck_leave_possible_order = math.factorial(6)
print(truck_leave_possible_order)

# 7. A circular loading zone has a radius of 7.5m. Find its area, rounded down to a whole number.
r = math.pow(7.5, 2)
print(math.floor(math.pi * r))

# 8. A stock adjustment of -342.75 was recorded. Print its absolute value.
print(math.fabs(-342.75))

# 9. Given parcel weight [0.1, 0.2, 0.3, 0.4, 0.15], measure total weight of these parcels accurately: 
weight = [0.1, 0.2, 0.3, 0.4, 0.15]
print(math.fsum(weight))

# 10. Sales grow continuously at a rate of 0.05 per year. Find the growth factor after 10 years (e^x, where x = rate × years).
print(math.exp(0.05 * 10))
