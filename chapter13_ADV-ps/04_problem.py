# Write a program to filter a list of numbers which are divisible by 5.

nums = [1,2,3,4,5,6]
a = lambda x: x % 5 == 0
even = list(filter(a, nums ))
print(even)
