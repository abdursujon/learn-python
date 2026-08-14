def checkNumber(a, b):
    if a > b: 
        print("a is greater than b")
    elif a == b: 
        print("a is equal to b")
    else: 
        print("b is greater than a")

checkNumber(78, 66)
checkNumber(66, 66)
checkNumber(6, 66)

# Shorthand if 
a, b, c = 9, 90, 78
if a > b: print("a is greater than b")

# Nested if 
if a < b: 
    print("a is less than b")
    if a < 20: 
        print("a is also less than 20")
    if c > 50: 
        pass
    if c == 78:
        print(f"c is {c}")    

# Shorthand if.. else
print("A") if a > b else print("B") 

# Assign a value with if else  
bigger = a if a > b else b
print("bigger number between a and b is: ", bigger)

# Multiple condition in one line 
print("A") if a > b else print("=") if a == b else print("B")

# Ternary operator 
age = 78
status = "adult" if age >= 18 else "minor"
print(status)