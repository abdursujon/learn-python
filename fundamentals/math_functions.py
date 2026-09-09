import math 
# print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 
'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print("=========== Constants ===============")
print(f"π (pi): {math.pi}")
print(f"e: {math.e}")
print(f"τ: {math.tau}")
print(f"positive infinity (∞): {math.inf}")
undefined_number = 0 * math.inf # nan means not a number which is undefined or invalid 
print(f"not a number (nan): {undefined_number}\n")


print("=========== Rounding and Absolute  ===============") 

# round to next nearest integer, always away from zero 
nearest_int = math.ceil(56.3) 

# round down to nearest integer, always toward negative infinity 
round_down_nearest_int = math.floor(56.3) 

# truncate: remove the decimal part entirely 
remove_decimal = math.trunc(56.3) 

 # floating point absolute, always returns abs with float type 
floating_point_abs = math.fabs(-56.3)

# integer sqaure root, float type does not work 
integer_square_root = math.isqrt(56) 

print(f"nearest_int: {nearest_int}, round_down_nearest_int: {round_down_nearest_int}",
     f"remove_decimal: {remove_decimal}, floating_point_abs: {floating_point_abs},"
     f"integer_square_root: {integer_square_root}\n")

print("=========== Roots and Special Values ===============")

# cube root 
cube_root = math.cbrt(64)
print("cube_root:", cube_root)

# hypotenuse of a triagnle: √(a² + b²)
hypotenuse = math.hypot(3, 4)
print("hypotenuse: ", hypotenuse)

# Euclidean distance is the straight line distance between two points in space: distance = √((x₂ - x₁)² + (y₂ - y₁)²)
euclidean_distance = math.dist([0, 0], [5, 8]) # [x1, y1], [x2, y2]
print("euclidean distance:", euclidean_distance)

print("\n=========== Factorial and Combinatorics ===============") 
print("factorial: ", math.factorial(5))

people = ["Nick", "Mitten", "Micheal", "Angelo", "Garner"]
# Choose 2 from 5 where order doesn't matter
# how many combination possible if we organise the data in pair 
print("combination of two people, pair possible:", math.comb(len(people), 2))
# if 50 peoplle handshake each other how many handshake has happend 
print("handshake: ", math.comb(50, 2))

# Choose 2 from 5 where order does matter
print("combination of two people when order does matter count:", math.perm(len(people), 2))

print("\n=========== Flaoting point operations ===============") 
print(math.fmod(7,3)) # floating point remainder(1.0)

# which multiple of y(in this case 4) is closest to x(in this case 7). IEEE standard, minimizes absolute value
print(math.remainder(7, 4)) # 4 * 1 = 4, 7 - 4 = 3. Then 4 * 2 = 8, 7 - 8 = -1. Therefore the remainder is -1 

# accurate sum of float points 
print(math.fsum([0.001, 0.88, 0.0001]))

# product of all elements given 
nums = [1, 2, 3, 4, 5]
print(math.prod(nums))

# sum product with two list 
print(math.sumprod([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])) # (1 * 6 + 2 * 7 + .. + 5 * 10)

# is finite number
print(math.isfinite(42 / 42))

# is infinite number
infinite_num = 1 / 1e-308
print(math.isinf(infinite_num))
print(math.isinf(math.inf))

# is undefined (nan : not a number)
print(math.isnan(0 * math.inf))

print("\n=========== Trigonometric Functions ===============")
print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.tan(math.pi / 5))
print(math.asin(1))
print(math.acos(0))
print(math.atan(1))
print(math.atan2(1, 2))

print("\n=========== Hyperbolic functions ===============")
print(math.sinh(0))
print(math.cosh(0))
print(math.tanh(0))
print(math.asinh(0))
print(math.acosh(1))
print(math.atanh(0))

print("\n=========== Expoential and Logarithmic ===============")
# e = 2.71828 here exp means exponential where we compute the natural exponential of function eˣ 
print(math.exp(1))

# 2ˣ
print(math.exp2(4)) # 2ˣ = 2^4 = 16

# eˣ − 1: math.expm1 exists for numerical accuracy when x is very small 
# computing eˣ - 1 directly would lose precision due to floating-point rounding, but expm1 avoids that.
print(math.expm1(1))

print(math.log(math.e))
print("log10:", math.log10(100))
print("log2:", math.log2(100))
print("log1p:", math.log1p(0.5))
print("x^y:", math.pow(2, 3))
print("sqare root:", math.sqrt(64))