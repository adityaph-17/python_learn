# What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))  # Output: 2

# Explanation:
# In Python, the integer 20 and the float 20.0 are considered equal when it comes to set membership, so they will not be added as separate elements. 
# However, the string '20' is different from the integer and float, so it will be added as a separate element. 
# Therefore, the set will contain two elements: {20, '20'}. Hence, the length of the set s will be 2.

