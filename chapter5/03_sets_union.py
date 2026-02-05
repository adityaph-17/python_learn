# in this we will learn about sets operation like union in python

s = {1, 2, 3, 4, 5}
print ("Set s:", s) # print the entire set

t = {4, 5, 6, 7, 8}
print("Set t:", t) # print the entire set

# union of two sets using union() method
u = s.union(t)
print("Union of s and t using union() method:", u)
# union of two sets using | operator which combines both sets and removes duplicates

# intersection of two sets using & operator
u = s.intersection(t)
print("Intersection of s and t using & operator:", u)
#  gives common elements in both sets

# difference of two sets using - operator
u = s.difference(t)
print("Difference of s and t using - operator:", u)
# gives elements in s but not in t

# symmetric difference of two sets using ^ operator
u = s.symmetric_difference(t)
print("Symmetric difference of s and t using ^ operator:", u)
# gives elements in either s or t but not in both

