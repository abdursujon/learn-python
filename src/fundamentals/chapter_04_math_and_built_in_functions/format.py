'''
This script covers different style of formating in python. 
'''
name = "Sujon"
favourite_num = 1918
hobby = "Football"

# 1. Old style formatinng using % operator 
print("Name: %s, Favourite Number: %d, Hobby: %s" % (name, favourite_num, hobby))

# 2. format() method 
print("Name: {}, Favourite Number: {}, Hobby: {}".format(name, favourite_num, hobby)) # index by provided order
print("Name: {0}, Favourite Number: {1}, Hobby: {2}".format(name, favourite_num, hobby)) # with index 
print("Name: {n}, Favourite Number: {fav}, Hobby: {hob}".format(n=name, fav=favourite_num, hob=hobby)) # with name hint 

# 3. f-string (modern python style)
print(f"Name: {name}, Favourite Number: {favourite_num}, Hobby: {hobby}")

# 4. String additional formatting 
print(f"{name:>10}") # right align 10 chars
print(f"{name:<10}") # left align 10 chars
print(f"{name:^10}") # center align 

# 5. number formating 
cost = 15666.9990980
print(f"Cost: £{cost:.2f}") # up to two decimal place 
print(f"Cost: £{cost:,}") # comma seperator 
percent = 0.233
print(f"Percentage: {percent:.0%}") # .0 indicates how many decimal points to display
print(f"Percentage: {percent:.1%}")