# demonstrating tuple creation and basic operations

# Creating a tuple
a = (1, 2, 3, 4, 5)
print("Original Tuple:", a)
print("Type of a:", type(a))

#tuple wit one element
b = (1,)
print("\nTuple with one element:", b)
print("Type of b:", type(b))

c = (1,2,3,4,5)
c[0] = 10  # This will raise a TypeError since tuples are immutable

