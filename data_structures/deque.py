from collections import deque
'''
deque (pronounced "deck") is a data structure in Python available 
in the standard collections module.  It stands for double-ended queue
and is designed for O(1) time complexity when appending and popping
elements from both ends, making it significantly more efficient than 
standard Python lists for these operations.
Implementation: It is implemented as a doubly linked list, allowing efficient 
and deletion at both the front and rear. 
Versatility: It can be used to implement both stacks (LIFO) and queues (FIFO). 
Bounded Size: We can specify a maxlen parameter to create a fixed-size deque that automatically discards older items when full.
'''

# Initialize deques
dq = deque()
dq2 = deque(["Drawing", "Music", "Football", "Cricket"])
dq3 = deque([1, "Mix type allowed", 55.6, 8j])

# Common Methods 

# 1. append: add an element at the right 
dq.append(1999)
dq.append(1999)
print(dq)

# 2. appendleft: add an element at the left end
dq.appendleft(2000)
print(dq)

# 3. extend: add multiple items to the right end
dq.extend([2001, 2002])
print(dq)

# 4. extendleft: add multiple items to the left end (reverses order)
dq.extendleft([2003, 2004])
print(dq)

# 5. pop: remove from right end
dq.pop()
print(dq)

# 6. popleft: remove from left end
dq.popleft()
print(dq)

# 7. remove: remove first occurrence of an element 
dq.remove(1999)
print(dq)

# 8. index: find index of item
print(dq.index(1999))

# 9. count: count occurrences of item
print(dq.count(1999))

# 10. rotate: rotate elements (positive = right, negative = left)
dq.rotate(2) # Takes last 2 elements and moves them to front
print(dq, "Moved last two element to the front of the deque")
dq.rotate(-2)  # Takes first 2 element and moves it to end
print(dq ,"Moved first two element to the end of the deque")

# 11. reverse: reverse the deque in-place
dq.reverse()
print(dq, "reverse of original dq list")

# 12. copy: create a copy of the deque
dq_copy = dq.copy()
print(dq_copy)

# 13. len: check number of items in deque
print(len(dq))

# 14. clear: remove all items from deque
dq.clear()
print(dq)