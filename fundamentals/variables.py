# A variable is a container which stores a value with a name 

# Creating variable 

# String (text)
name = "Sujon"
city = "Manchester"

# Integer (a whole number)
savings = 100

# Flaot (decimal number)
height = 5.10 

# Boolean 
is_rich = False
is_student = True

## Now we can use each variable for example we can print them on terminal
print(name)
print(is_student)

# We can also reassign different value to a variable for example 
name = "Ryan"
print(name) # will print Ryan instead of Sujon

# If you are feeling lazy u can also do multiple assignment at the same time for example 
x, y, z = 19, 23.4, 44.6

# We can use f-string (formatted string literal) to print all of them at the same time 
print(f"{x} {y} {z}")

## Or we can convert integer to string by 
print("x is: " + str(x) +  " y is: " + str(y) + " z is: " + str(z))

# Variable naming rules 
first_name = "Su"
firstName = "Su" # camelCase 
firstname = "Su" # all lowercase 
_firstname = "Su" 
height2 = 7.7
print(height2)

# Invalid namings are 
## 2age (can not start with number)
## first-name (can not use hyphen)
## first name (no space)
## for (can not use reserved word such as for, while)
