# in this we will learn about sets in python
# sets are unordered collections of unique elements
# sets are mutable, meaning we can add or remove elements from a set
#sets do not allow duplicate elements

s = {1, 2, 3, 4, 5}
print("Set s:", s) # print the entire set
print("Type of s:", type(s)) # print the type of s

# creating an empty set
empty_set = set()
print("Empty set:", empty_set)
print("Type of empty_set:", type(empty_set))


#methods of sets
# adding elements to a set
s.add(6)
print("Set s after adding 6:", s)

# removing elements from a set
s.remove(3) # raises KeyError if element not found
print("Set s after removing 3:", s)

s.discard(4) # does not raise error if element not found
print("Set s after discarding 4:", s)


