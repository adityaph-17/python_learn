# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
list = [1,2,3,4,5]
greater = lambda a, b: a if a > b else b

g = reduce(greater, list)
print(g)
