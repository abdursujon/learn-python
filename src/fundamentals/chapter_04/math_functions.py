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
