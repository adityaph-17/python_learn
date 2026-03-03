# Comprehension means:
# Create list / set / dictionary in one line using loop.
# Cleaner + Professional way.

# normal way
# squares = []
# for i in range(1, 6):
#     squares.append(i*i)
# print(squares)

# Using Comprehension

squares = [i*i for i in range(1, 6)]
print(squares)

even = [i for i in range(10) if i % 2 == 0]
print(even)


numbers = [1, 2, 3]
square_dict = {i: i*i for i in numbers}
print(square_dict)

nums = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 10]
unique_set = {i for i in nums}
print(unique_set)

