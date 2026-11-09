# list comprehension, when no else the template is
# 1. [expression + for loop]
email = [
    "example.+@gmail.com",
    "sujon@com.su",
    "ryan.eccles@gmail.com",
    "ryan.ecc.les@gmail.com",
]
valid_local = [e.split("@")[0].split("+")[0].replace(".", "") for e in email]
domain = [e.split("@")[1] for e in email]
valid_unique_email = set()
for l in range(len(valid_local)):
    valid_unique_email.add(valid_local[l] + "@" + domain[l])
print(valid_unique_email)

# with if
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in num if n % 2 == 0]
odd = [n for n in num if n % 2 != 0]
print(even, odd)

# with else if
num = [-3, 3, -30, 3, 3, 2]
filter_num = [True if n > 0 else False for n in num]
print(filter_num)
ages = [12, 18, 25, 16, 40]
ages_filter = ["Adult" if a >= 18 else "Minor" for a in ages]
print(ages_filter)
