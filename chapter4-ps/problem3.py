# Check that a tuple type cannot be changed in python.

# Creating a tuple
tuple1 = (10, 20, 30, 40, 50)
print("Original Tuple:", tuple1)
# Trying to change the first element of the tuple
tuple1[1] = 100

# The above code will raise a TypeError because tuples are immutable in Python.

