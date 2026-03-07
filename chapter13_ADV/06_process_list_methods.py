#  map(), filter(), reduce() in Python
# These are used to process lists quickly.

from functools import reduce

# map() :- Used to apply a function to every element.
nums = [1,2,3,4,5,6]

square = list(map(lambda x: x*x, nums))
print(square)

#without map()
square = []
for i in nums:
    square.append(i*i)

print(square)


# filter() :- Used to select elements based on condition.
nums = [1,2,3,4,5,6]

even = list(filter(lambda x: x % 2 == 0, nums ))
print(even)

# Without filter()
even = []
for i in nums:
    if i % 2 ==0 :
        even.append(i)

print(even)


# reduce() :- Used to reduce list to single value.
list = [1,2,3,4,5]
add = lambda a,b : a+b
mul = lambda a,b : a*b

addReduce = reduce(add, list)
mulReduce = reduce(mul, list)
print(addReduce)
print(mulReduce)