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
# 1. re.escape(s)
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
# 4. re.finditer(p, s)
# 5. re.fullmatch(p, s)
# 6. re.match(p, s)
# 7. re.search(p, s)
# 8. re.split(p, s)
# 9. re.sub(p, repl, s)


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
