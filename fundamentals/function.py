'''
function is a block of code which only runs when it is called. 
when called, it may or may not return data. 
the core idea of function is to avoid repetition. 
'''

# function with no parameter 
def my_function():
    print("I am a function")
my_function()

# function with return and parameter 
def greet(name): 
    return f"Hello {name}, Welcome to Learn Python Project."

print(greet("Sujon"))
result = greet("Ryan")
print(result)

# function with no return 
def hobby(mylist):
    for i in mylist: 
        print(i)

hobby(["football", "cricket", "art", "music"])

# why we need function? let's consider we want to convert fahrenheit to celsius. each time we want to do it we will have to 
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9 
print(celsius1)

temp2 = 90
celsius2 = (temp2 - 32) * 5 / 9 
print(celsius2)

# this is not efficient, and simply not flexible enough. now consider below 
def fahrenheit_to_celcius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2) # we can use round(statement, limit) to round how many number we want after decimal 

# now we can call the function with any temp we would like and get different result without repeting ourself for each case. 
print(fahrenheit_to_celcius(33))
print(fahrenheit_to_celcius(88))
print(fahrenheit_to_celcius(120))

# if we want a function with no body so we can use it for later purpose we can simply use the keyword pass  for example 
def use_later(): 
    pass 
use_later() # won't give us error but we we had simply def use_later(): it will return error     


# function with default parameter value, if a function with has parameter is called without any argument we can assign a default value so the function does not return an error
def my_function_two(my_name = "Unknown"):
    print("Hello", my_name)
# now if we call the function without any argument it will return "Hello Unknown"
my_function_two()    
my_function_two("Sujon") 

# Keyword Arguments (often shorthand for kwargs): we can use key = value style to call a function with argument for exmaple 
my_function_two(my_name = "Will") 

# Positional arguments: when we call a function without specifying with key = value arguments are treated as ordered from left to right 
def my_function_three(animal, name, /): # using / after parameter specify that a function is solely positional function and does not allow kwargs
    print("I have a", animal)
    print("My", animal + " name is", name) # we can use + here cause all types is string 
my_function_three("dog", "Siki")    

# In python when we pass arguments on function we can pass any data type. Such as we can send a dictionary type, list or tuple in the same function 
# passing a dictionary(hashmap)
def my_function_four(person):
    print("My name is", person["name"],".")
    print("I am ", person["age"], " year old.") # can not use + to concatenate cause types are different 
person_details = {"name": "Emik", "age": 45}
my_function_four(person_details)    

# we can use *, to specify that a function is only keyword arguments function 
def my_function_five(*, name):
    print("My name is " + name)
my_function_five(name = "Sukal")   # note: if we only pass "Sukal" the function will return an error 

# Combining positional-only and keyword-only arguments 
def my_function_six(a, b, / , *, c, d):
    return a + b + c + d 
print(my_function_six(10, 20, c = 30, d = 40))    


''' If we do not know how many arguments will be passed into our function, we can add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:
'''
def my_function_seven(*args): 
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
my_function_seven("Emia", "Jasper", "Shelly", "Kiat")    

# args is usefull when we want to creat a flexible function such as calculate sum of all numbers that are given 
def sum(*nums):
    total = 0
    for n in nums:
        total += n
    return total    
print(sum(66, 77, 7745, 550))   



'''
Arbitrary Keyword Arguments - **kwargs
If we do not know how many keyword arguments will be passed into our function, we can add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:
The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
'''
def my_function_eight(**person):
    print("Wanted person last name is " + person["lname"])
my_function_eight(fname = "Usaf", lname = "Ali", mname = "Akbar")    

def my_function_nine(**kwargs): 
    print("Type:", type(kwargs))
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("All data:", kwargs)
my_function_nine(name = "Kaak", age = 30, city = "Manchester")    
person_data = {"name": "Ali", "age": 59}
my_function_nine(**person_data)

'''
Unpacking Lists with *
If we have values stored in a list, we can use * to unpack them into individual arguments:
'''
def my_function_ten(a, b, c):
    return a + b + c
numbers = [1, 3, 4]
result = my_function_ten(*numbers) # same as my_function(1, 3, 4)
print(result)    