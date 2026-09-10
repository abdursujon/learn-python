'''
tuple: tuple are used to store multiple items in a single variable.
It is ordered and can not be modified after creation. It is effectively a list 
which can not be change after list has been created.
'''

# tuple with round bracket 
tuple_one = ("cricket", "football", "hiking", "chess")

# tuple can be created without bracket as well
tuple_two = 88, 44, 22
print(tuple_two)

# tuple can have item with same value since it is index base 
tuple_three = 55, 53, 44, 55 
print(tuple_three)

# if a tuple only has one item we must add a comma after first item otherwise python won't recognise it
tuple_four = ("single",) 
# not valid tuple_four = ("single")

# tuple has two methods they are count(x) and index(x)
tuple_five = (11, 33, 123, 33, 44, 22, 44)
print(tuple_five.count(33)) # two times 
print(tuple_five.index(22))

