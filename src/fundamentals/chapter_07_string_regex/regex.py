import re
# re module offers set of functions that allows us to search int the text

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
