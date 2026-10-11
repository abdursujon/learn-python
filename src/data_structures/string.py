'''
1. s.count(sub)
2. s.endswith(suffix)
3. s.find(sub)
4. s.index(sub)
5. s.isalnum()
6. s.isalpha()
7. s.isdigit()
8. s.islower()
9. s.isspace()
10. s.isupper()
11. sep.join(list)
12. len(s)
13. s.lower()
14. s.replace(old, new)
15. s.split(sep)
16. s.startswith(prefix)
17. s.strip()
18. s.upper()
'''
s = "Here no one is equal. Here everybody wants more. More they have, the more they want."

# 1. s.count(sub): count occurrences of a substring
result = s.count("Here")
print(result)

# 2. s.endswith(suffix): check if string ends with suffix
if s.endswith("more."):
    print(s.count("more"))

# 3. s.find(sub): index of first occurrence, -1 if not found
result = s.find("more")
print(f"index of first occurrence of more {result}")

# 4. s.index(sub): same as find() but raises ValueError if not found
result = s.index("the")
print(result)

# 5. s.isalnum(): True if all chars are letters or digits
text = "1244422"
print(text.isalnum())
text = "Ak&&da333111"
print(text.isalnum())

# 6. s.isalpha(): True if all chars are letters
text = "38833yes"
print(text.isalpha())
text = "I only have letters"
text = text.replace(" ", "")
print(text.isalpha())

# 7. s.isdigit(): True if all chars are digits
text = "88djhdj"
print(text.isdigit())
text = "9898767"
print(text.isdigit())

# 8. s.islower(): True if all letters are lowercase
text = "i am in lowercase"
print(text.islower())

# 9. s.isspace(): True if all chars are whitespace
text = " kdnfka "
print(text.isspace())
text = " "
print(text.isspace())

# 10. s.isupper(): True if all letters are uppercase
text = "I AM UPPER CASE"
print(text.isupper())

# 11. sep.join(list): join a list into a string using sep
words = ["I", "like", "pizza"]
text = " ".join(words)
print(text)


# 12. len(s): length of the string
text = "What is my length?"
print(len(text))

# 13. s.lower(): convert to lowercase
text = "Capital Of ChiNA IS beijing"
text = text.lower()
print(text)

# 14. s.replace(old, new): replace a substring
text = "capital of china is beijing"
text = text.replace("china", "UK").replace("beijing", "London")
print(text)

# 15. s.split(sep): split into a list by separator (no arg = split on whitespace)
text = "China is an interesting country"
words = text.split()
print(words)

# 16. s.startswith(prefix): check if string starts with prefix
text = "China is an interesting country"
print(text.startswith("China"))

# 17. s.strip(): remove leading/trailing whitespace
text = "  China is an interesting country  "
print(text)
print(text.strip())

# 18. s.upper(): convert to uppercase
text = "  China is an interesting country  "
text = text.upper()
print(text)
