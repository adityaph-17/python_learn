# Can we have a set with 18 (int) and '18' (str) as a value in it

set = set()
set.add(18)
set.add('18')

print(set)  # Output: {18, '18'}

# set can contain both int and str values, as they are different types.


