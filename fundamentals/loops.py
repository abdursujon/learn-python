# For loops 
items = [44, 44.5, "Orange", "Apple"]

# index base for loop 
for i in range(len(items)):
    print(items[i])

for i in range(1, 10):
    print(i * 3)

# enhanced for loop
for i in items: 
    print(i)

# enumerate for loop which access index and value at the same time 
for index, item in enumerate(items):
    print(index, item)

# break and continue keyword to stop a loop or continue without accessing some items
# pass keyword does nothing while continue skips an iteration in a loop 
for i in items:
    if i == 44: 
        continue
    print(i)
    if i == "Orange": 
        break    

# while loop 
i = 0
while(i <= 20):
    print(i)
    i += 1

# python has no do while but we can create do while behaviour like below 
print(i)
i += 1
while i < 5: 
    print(i)
    i  += 1