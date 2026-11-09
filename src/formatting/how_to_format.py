"""
There is messy and unformatted code here, and import that we do not use
we can use ruff to fix this automatically
ruff check messy.py
ruff check messy.py --fix
ruff format messy.py
"""

def get_user(name, age):
    data = {"name": name, "age": age}
    unused = 42
    if age == None:
        return None
    print("Getting user")
    return data


add = lambda a, b: a + b


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "hi " + self.name
