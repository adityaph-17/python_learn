# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}
print(s)
# Output will be an error:
# TypeError: unhashable type: 'list'
# Explanation:
# In Python, sets are collections of unique and unordered elements.
# However, all elements in a set must be hashable (immutable).
# Lists are mutable and therefore unhashable, which means they cannot be added to a set
# If we try to add a list to a set, it will raise a TypeError.
# Therefore, we cannot change the values inside a list that is contained in a set,
# because we cannot even add a list to a set in the first place.
