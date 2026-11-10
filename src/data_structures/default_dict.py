from collections import defaultdict

# 1. Avoid KeyError crashes 
d = defaultdict(int)
print(d["missing"]) # prints 0, no keyerror even though k does not exists, this calls also automatically adds missing as a k in the dict
print(dict(d)) # prints normal dict 
d["orange"] += 6 # works even though orange is not in the dict 
print(dict(d))
print(d["orange"])

# 2. Automatically create starting values 
lists = defaultdict(list)
counts = defaultdict(int)
uniques = defaultdict(set)
# creates three empty dictionary of the specified data type 
print(dict(lists), dict(counts), dict(uniques))
lists["a"] # creates {"a":[]}
print(dict(lists))
counts["orange"] # creates {"orange":0}
print(dict(counts))

# 3. shorter and cleaner loop 
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
# without defaultdict 
groups = {}
for w in words: 
  if w[0] not in groups:
    groups[w[0]] = []
  groups[w[0]].append(w)
print(groups)

groups2 = defaultdict(list)
# with defaultdict 
for w in words:
  groups2[w[0]].append(w)
print(dict(groups2))
