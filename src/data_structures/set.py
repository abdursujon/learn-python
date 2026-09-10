'''
A set is a collection which is unordered, unchangeagle and unindexed
1. Set has no order and items can be any data type 
2. Item that are stored can not be changed but can be remove
3. Set has no index bas access 
4. Set does not allow duplicate 
'''

set_one = {"apple", "banana", "cherry", "egg"}
print(set_one)
print(type(set_one))

# duplicate are ignored 
set_two = {"apple", "banana", "cherry", "apple"}
print(set_two)
# value True and 1 are considered to be the same value and if we add 1 and True to the set one of them will be ignored 
set_three = {True, 1, True, 1}
print(set_three) # only one item will be considered from all 4 elements


# value False and o are also considered to be same 
set_four = {False, 0, False, 0}
print(set_four)

'''
Set has 17 methods which we can use to manipulate the set list. Below the are listed as relevant group.
'''

''' Adding/Removing elements '''
set_five = {1, 88, 34, 22, 90}

set_five.add(5)
print(set_five)

set_five.remove(1) # remove returns error if the item does not exists
print(set_five)

set_five.discard(0) # discard removes item but do not return error if the item not found
print(set_five)

set_five.pop() # remove and return a arbitrary element(no gurentee it will remove first or last item)
print(set_five)

set_five.clear() # remove all elements 
print(set_five)

''' Set Copying '''
set_six = {1, 88, 34, 22, 90}
set_seven = set_six.copy() # shallow copy the origin, if change happens in original set it won't register the change 
print(set_seven)
set_six.add(55)
print(set_six)
print(set_seven) # does not register change in set six 

''' Set Operations ''' 
s8 = {1, 3, 6}
s9 = {6, 9, 11}

print(s8.union(s9)) # {1, 3, 6, 9, 11}
print(s8.intersection(s9)) # {6}
print(s8.difference(s9)) # s8 - s9 = {1, 3} elements remainded in second set does not count
print(s8.symmetric_difference(s9)) # s8 - s9 = {1, 3, 9 , 11} elements remainded in second set counts as well

''' Set Comprarions'''
s10= {9, 11}
s11 = {6, 9, 11}
print(s10.issubset(s11))   # Check if s1 is subset of s2  or s1 <= s2
print(s10.issuperset(s11))  # Check if s1 is superset of s2  or s1 >= s2
print(s10.isdisjoint(s11))  # Check if no common elements


''' In Place Operations (modify original set)'''
#update(): add elements from s2  
s10= {1, 2, 3}
s11 = {3, 4, 5}
s10.update(s11)
print(s10) 

# intersection_update(): Keep only common elements 
s10= {1, 2, 3}
s11 = {3, 4, 5}
s10.intersection_update(s11)  
print(s10)


# difference_update(): Remove elements in s2 
s10= {1, 2, 3}
s11 = {3, 4, 5}
s10.difference_update(s11)  
print(s10)

# symmetric_difference_update(): Keep only non-common elements
s10= {1, 2, 3}
s11 = {3, 4, 5}
s10.symmetric_difference_update(s11)  
print(s10)