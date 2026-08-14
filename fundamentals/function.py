# function with return 
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
