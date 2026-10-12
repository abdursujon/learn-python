import re

'''Meta Characters'''
# [] set of characters
result = re.findall(r'[a-zA-Z]+', "What a lovely day")
print(result)

# \A returns if character at beginning of string 
pattern = r'\AJust'
text = "Just wait a little longer, time passes and it fixes your problems."
result = re.match(pattern, text)
print(result)

# . any character except newline 
result = re.findall(r'ab.z', "abyz")
print(result)
result = re.findall(r'ab...z', "abcxyz")
print(result)
result = re.findall(r'ab.z', "ab\nyz")
print(result)

# ^ starts with and $ means ends with 
result = re.match(r'^T.*$', "the power of consistency is enormous.", re.I)
print(result)

# | either this or that 
result = re.match(r'the|enormous', "the power of consistency is enormous.", re.I)
print(result)
result = set(re.findall(r'Cat|is', "the power of consistency is enormous.", re.I))
print(result)

# () group characters here find all words 
result = re.findall(r'(\w+)', "I like music")
print(result)

'''Special Sequence'''
# \A returns if character at the begining 
result = re.match(r'\AI', "I love football.")
print(result)

# \d returns a match if the string contains any digit 
result = re.search(r'\d', "x8989")
print(result)

# \D matches any single non-digit character
result = re.search(r'\D', "no digit")
print(result)
result = re.search(r'\D*', "I do have a digit 8")
print(result)

# \w returns a match if string contains any characters letter from a -z, digits 0-9 and underscore "_"
result = re.findall(r'\w+', "I do have a digit 8")
print(result)

# \Z if character at the end of the string 
result = re.search(r'8\Z', "I do have a digit 8")
print(result)

# \b returns a match position of given words or char
result = re.search(r'stranger\b', "Hi stranger, by stranger")
print(result)

# \s check if string has space 
result = re.search(r'\s+', "I have space.")
print(result.start())
print(result.end())
print(result.span())

# \S returns if string does not have a space 
result = bool(re.search(r'\S+', "Idon'thavespace"))
print(result)

'''Character Classes'''
# [a-z] lowercase a - z
result = (re.fullmatch(r'[a-z ]+', "all my words are in lowercase"))
print(result)

# [a-zA-Z] # a-z upper and lower
result = (re.fullmatch(r'[a-zA-Z ]+', "I have lower and Upper case"))
print(result)

# [0-9] digit 0 -9 
is_digit = bool(re.fullmatch(r'[0-9]+', "9088"))
print(is_digit)
is_digit = bool(re.fullmatch(r'[0-9]+', "9088ys"))
print(is_digit)

# [^rtw] # returns a matcch for any character except r, t, w
result = re.fullmatch(r'[^rtw]+', "xyaxyaz")
print(result)
result = re.fullmatch(r'[^rtw]+', "xyaxyaztw")
print(result)

# [abc] returns match when any given character exists 
result = bool(re.search(r'[abc]', "xyzabcxyzabc"))
print(result)

# [+*&{}()/] etc special character matches them exactly 
result = re.findall(r'[+*&%\-.,!]', "&I- love & * ! , \-")
print(result)

'''Quantifiers'''
# ? patterns occurs zero or 1 time 
result = re.search(r'(happy?)', "Are you happy?")
print(result)

# + patterns occur on or more time 
result = re.findall(r'[a-z]+', "lower case")
print(result)

# * patterns occur zero or more time 
result = re.findall(r'[0-9*]', "0988343")
print(result)
result = re.findall(r'[0-9*]', "0988xr")
print(result)
result = re.findall(r'[0-9*]', "eaxr")
print(result)

# {n} patterns occurs exactly n times 
result = re.findall(r'\d{3}', "12 123 1234")
print(result)
result = re.findall(r'\b\d{3}\b', "12 123 1234") # exactly 3 digit only 
print(result)
result = re.findall(r'\b\d{2,4}\b', "67 67 98 3345 221 43428") # 2 digit till 4 digit 
print(result)

# {n,} pattern occurs at least n or more time 
result = re.findall(r'\d{2,}', "12 33 1 333 1113 1113 2 4")
print(result)

# {n, m} pattern occurs at leas n times but not more than m times 
result = re.findall(r'\d{2,5}', "1 33 232 34343 44 2232 4532 223424234 23424")
print(result)