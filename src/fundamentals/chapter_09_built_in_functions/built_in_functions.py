# 1. abs() Returns the absolute value of a number
x = -90
x = abs(x)

# 2. all() Returns True if all items in an iterable object are true
l = [0, 0, 1, 1]
s = {1}
t = (True, True, False)
d = {0: "False", 1: "True"}
print(all(l), all(s), all(t), all(d))

num = [1, 1, 1, 0, 0, 1, 0]
try_all = [all(num) for n in num]
print(try_all)

# 3. any() Returns True if any item in an iterable is true
num = [2, 13, 12, 3, 2, 0, 2, 1, 1, 1]
try_any = [any(num) for n in num]
print(try_any)


# 4. bool() Returns the boolean value of an object
item = ["", 0, 1, 1, 0, 2]
try_bool = [bool(i) for i in item]
print(try_bool)

# 5. chr() Returns the character for a Unicode code
num = [3, 4, 33, 3, 33, 90]
try_chr = [chr(n) for n in num]
print(try_chr)


# 6. classmethod() Makes a method receive the class instead of an instance
class Person:
    name = "sujon"
    interests = "football"

    @classmethod
    def person_details(cls):
        return cls.name, cls.interests


print(Person.person_details())

# 7. dict() Returns a dictionary
dict(name="Sam", age=30)
person = []
name = ["sujon", "ryan", "sam"]
age = [23, 23, 24]
for n, a in zip(name, age):
    person.append(dict(name=n, age=a))
print(person)

# 8. dir() Returns a list of an object's properties and methods
import builtins

print([m for m in dir(set) if not m.startswith("__")])
print([b for b in dir(builtins) if not b.startswith("__")])

# 9. enumerate() Returns each item with its index
for index, fruit in enumerate(["apple", "banana"]):
    print(index, fruit)

# 10. filter() Keeps only the items where a function returns True takes a function and iterable data
nums = [1, 2, 3, 4]
list(filter(lambda n: n % 2 == 0, nums))
x = lambda a, b: a + b
print(x(4, 5))

# 11. float() Returns a floating point number
print(type(float("3.5")))


# 12. getattr() Returns the value of an object's attribute
class Car:
    color = ["red", "blue", "orange"]
    year = [2010, 2020, 2023, 2004]


print(getattr(Car, "year"))
print(getattr(Car, "color"))

# 13. hasattr() Returns True if an object has the specified attribute
print(hasattr(Car, "color"))
print(hasattr(Car, "speed"))

# 14. help() Shows the documentation for an object
# help(abs)

# 15. input() Lets the user type a value (the script pauses until you press Enter)
# name = input("Enter your name: ")
# print(name)

# 16. int() Returns an integer number
int("42")
int(3.9)

# 17. isinstance() Returns True if an object is an instance of the specified type
print(isinstance(5, int))
print(isinstance(5, str))

# 18. iter() Returns an iterator object
it = iter([10, 20, 30])
print(type(it))

# 19. len() Returns the length of an object
len("hello")
len([1, 2, 3])

# 20. list() Returns a list
list("abc")

# 21. map() Applies a function to each item
num = list(map(lambda n: n**n, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(num)

# 22. max() Returns the largest item
max(3, 7, 2)
max([3, 7, 2])

# 23. min() Returns the smallest item
min(3, 7, 2)
min([3, 7, 2])

# 24. next() Returns the next item from an iterator
it = iter([10, 20, 30])
print(next(it))
print(next(it))

# 25. open() Opens a file and returns a file object (this creates demo.txt)
with open("demo.txt", "w") as file:
    file.write("I wrote this file using python open method")

with open("demo.txt") as file:
    file.read()

# 26. ord() Returns the Unicode code of a character
print(ord("A"))

# 27. print() Prints to the output


# 28. @property Lets you access a method like an attribute
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


c = Circle(5)
print(c.diameter)

# 29. range() Returns a sequence of numbers
print(list(range(5)))
print(list(range(2, 10, 2)))
for i in range(len(nums)):
    print(i)

# 30. repr() Returns a developer-friendly string version of an object
print(repr("hello\n"))  # here repr stands for representation and it prints \n as it is

# 31. reversed() Returns a reversed iterator
# Can use: list, tuple, str, range, dict (Python 3.8+, returns keys)
# Can't use: set, frozenset, generators and other iterators (TypeError)
print(list(reversed([1, 2, 3])))
mp = {1: "apple", 2: "banana", 3: "orange"}
for i, k in enumerate(mp):
    print(f"index {str(i)}", k, mp[k])

# 32. round to specific number if not specified it rounds to nearest whole number
print(round(3.14159, 2))
print(round(3.79888))

# 33. set() Returns a set, which removes duplicates
set([1, 1, 2, 2, 3])

# 34. sorted() Returns a sorted list
print(sorted([3, 1, 2]))
print(sorted([3, 1, 2], reverse=True))


# 35. staticmethod() Makes a method that receives neither the instance nor the class
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(2, 3))

# 36. str() Returns a string
str(100) + "%"

# 37. sum() Adds the items of an iterable
sum([1, 2, 3])


# 38. super() Gives access to the parent class
class Animal:
    def speak(self):
        return "Some sound"


class Cat(Animal):
    def speak(self):
        return super().speak() + ", then meow"


print(Cat().speak())

# 39. tuple() Returns a tuple
tuple([1, 2, 3])

# 40. type() Returns the type of an object
type(5)
type("hi")

# 41. zip() Pairs items from two or more iterables and returns tuple
names = ["Sam", "Ali"]
ages = [30, 25]
print(list(zip(names, ages)))
person = []
for n, a in zip(names, age):
    person.append(dict(name=n, age=a))
print(person)


# To print all built in methods so we can see and remind ourself
import builtins

# print(dir(builtins))
# print method that we can only use
print([d for d in dir(builtins) if not d.startswith("__")])
