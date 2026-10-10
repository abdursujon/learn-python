import re

'''
Regular Expression (re) module essential functions
p = pattern, s = string, repl = replace 
# 1. re.compile(p)
# 2. re.escape(s)
# 3. re.findall(p, s)
# 4. re.finditer(p, s)
# 5. re.fullmatch(p, s)
# 6. re.match(p, s)
# 7. re.search(p, s)
# 8. re.split(p, s)
# 9. re.sub(p, repl, s)
'''

'''
# 1. re.compile(p)
The re.compile(p) function in Python is used to compile a regular expression
pattern into a regex object. Compiling a pattern makes it more efficient when
we need to use the same pattern several times, as it avoids re-compiling the 
pattern each time.
'''
pattern = re.compile("mountain", re.IGNORECASE) # compile with flag
sentence = "The heighest Mountain, I climed- is called Ben Nevis."
search_a_word = pattern.search("mountain") 
if search_a_word:
  print("Found the word:", search_a_word.group()) # group returns the match value
# Using re.compile() for Multiple Operations
# Compile the pattern for matching words
pattern = re.compile(r"\b\w+\b")
words = pattern.findall(sentence)
print(words)

# Email Validation. Pre-compile the regex pattern to check for a valid email
email_pattern = re.compile(r"^[a-zA-Z0-9_+.-]+@[a-zA-Z0-9-]+\.[a-z-A-Z0-9-.]+$")
# Sample email addresses to validate
emails = [
    "abdursujon@example.com",
    "ryan.gmail.com",
    "a.r.sujon@domain.org",
    "sujon181819@domain,com"
]
for email in emails:
  if email_pattern.match(email):
    print(f"{email} is a valid a email address.")
  else:
    print(f"{email} is not a valid email address.")


'''
# 2. re.escape(s)
'''
sentence = "hello.*tutorialspoint."
escape_pattern = re.escape(sentence)
print(escape_pattern)

total = "Total: $5.99 (incl. tax). Price was $5x99 before."
price = "$5.99"
find = re.search(price, total) # without escape no match found
print(find)
find = re.search(re.escape(price), total) 
print(find)


# 3. re.findall(p, s)
pattern = re.compile(r"\b\w+\b")
sentence = "There is moments in life that are worth living for."
words = pattern.findall(sentence)
print(words)

# 4. re.finditer(p, s)
pattern = r"(?:music|like)"
text = "I love music, music makes me happy. I also like football. I like film too."
# find all matches of music and return start position and the matching word
match_words = re.finditer(pattern, text, re.IGNORECASE)
print(type(match_words))
for match in match_words:
  print(match.start(), match.end(), match.group())


# 5. re.fullmatch(p, s)
direction_pattern = re.compile(r"[NWES]+")
robot_dir = ["NSENWSE", "WxYxESSxI", "WWWWWW", "EEEE", "NNNN", "", "XYZ"]
for dir in robot_dir:
  if direction_pattern.fullmatch(dir):
    print(f"{dir} is valid direction")
  else:
    print(f"{dir} is invalid direction")

# 6. re.match(p, s) The re.match() method in Python is used to check whether a regular
# expression pattern matches the beginning of a string.
text = "Prices of house is going up every year. There is no way of affording house for young generation."
match_words = re.match("Prices", text)
print(match_words, "found found")
text = "123sujon8989"
match_pattern = re.match(r"\d", text) # check if the text started with a digit 
if match_pattern:
  print("Digit at the begining found")
else:
  print("Provided sentence does not start with a digit")

# 7. re.search(p, s)
text = "I have done so many pattern already! Give me a break!"
match_pattern = re.search("break", text)
if match_pattern:
  print("the word break, found")
else:
  print("not found")

# 8. re.split(p, s)
text = "I like mushroom. I like chicken tikka, I like pizza, i like wings."
words = re.split(" ", text.strip(".,; -"))
print(words)

# 9. re.sub(p, repl, s)
text = "apple banana orange milk butter milk butter orange "
replace_words = re.sub("orange", "mango", text)
print(replace_words)
text = "Python\t\tRegex\n is   great"
result = re.sub(r"\s+", " ", text)
print(result)
# Limiting the Number of Replacements in here orange is replaced only once 
text = "apple banana orange milk butter milk butter orange "
replace_words = re.sub("orange", "mango", text, count=1)
print(replace_words)
# Using Capture Groups
text = "2026-09-30"
result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\g<3>/\g<2>/\g<1>", text)
print(result)
# Using a Function as the Replacement
def divide_number(match):
  return str(int(int(match.group()) / 2))
text = "There are 12 apples and 7 oranges."
result = re.sub(r"\d+", divide_number, text, re.IGNORECASE)
print(result)


# 1. re.search(), takes the pattern, scan the text, and then return a Match object 
text = "I love football, and I love Messi. Messi is football God."
match = re.search("messi", text, flags=re.IGNORECASE)
print(match)
print(match.start())
print(match.end())


# 2. re.findall(), find all the instances of a pattern in a string and return a list 
match = re.findall("(?:messi|I|football)", text, re.IGNORECASE)
print(match)
# now we can use this to count how many match we found
print(len(match))


# 3. re.split
# In string we can make a list of words by doing this 
text_list = text.split()
print(text_list)
# we can achieve this using re as well
domain = "my verified public portfolio domain is sujons.com. I love programming, and music."
domain_list = re.split(r"[\s.,]+", domain)
print(domain_list)


# 4. re.fullmatch(pattern, text) finds the full match 
# given two string, count matching words between sentence where valid words consist of only letters. Return matching word count, if no match found, return 0. Duplicate word counts only once.
def find_match(first, second):
  def valid_words(sentence):
    result = set()
    for word in sentence.split():
      if re.fullmatch(r'[A-Za-z]+', word):
        result.add(word)
    print(result)
    return result
  return len(valid_words(first) & valid_words(second))

first_sen = "I like pizza and I like Stella"
second_sen = "I don't like pizza, but I like Stella"
print(find_match(first_sen, second_sen))


# ================= Some problem solved using regex ========================= #
def find_match_word(first, second):
  pattern = re.compile(r'\b\w+\b')
  first_sen = set(pattern.findall(first))
  second_sen = set(pattern.findall(second))
  return len(first_sen & second_sen)
                                 
print(find_match_word("I love pizza, I like football", "I like pizza, I like cricket"))

def find_match_word_two(first, second):
  first_sen = set(re.split(" ", first.strip(",.;- ")))
  second_sen = set(re.split(" ", second.strip(",.;- ")))
  return len(first_sen & second_sen)
print(f"find_match_word_two result: {(find_match_word_two("I love pizza, I like football", "I like pizza, I like cricket"))}")

 
from collections import Counter
def robot_direction(direction):
  # if s consists of char other than N, E, S, W return 0
  check_direction_s = re.fullmatch(r"[NESW]+", direction)
  if not check_direction_s:
    return 0
    
  else:
    is_lowercase = re.search(r"[a-z]", direction)
    if is_lowercase or direction=="":
      return 0
      
    #counts = Counter(direction) # return a dict with count each char
    #max_visited_direction = max(counts.values()) # max key:value 
    #return max_visited_direction

    count_second_way = {}
    for char in direction:
      count_second_way[char] = count_second_way.get(char, 0) + 1
    max_visited_dir_second = max(count_second_way.values())
    print(count_second_way)
    return max_visited_dir_second
    
  return 0
  
print(robot_direction("NWESCDE"))
print(robot_direction("NExNEx"))
print(robot_direction("NWNWNSES"))