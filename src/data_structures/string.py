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

# 5. s.isalnum(): True if all chars are letters or digits

# 6. s.isalpha(): True if all chars are letters

# 7. s.isdigit(): True if all chars are digits

# 8. s.islower(): True if all letters are lowercase

# 9. s.isspace(): True if all chars are whitespace

# 10. s.isupper(): True if all letters are uppercase

# 11. sep.join(list): join a list into a string using sep

# 12. len(s): length of the string

# 13. s.lower(): convert to lowercase

# 14. s.replace(old, new): replace a substring

# 15. s.split(sep): split into a list by separator (no arg = split on whitespace)

# 16. s.startswith(prefix): check if string starts with prefix

# 17. s.strip(): remove leading/trailing whitespace

# 18. s.upper(): convert to uppercase
