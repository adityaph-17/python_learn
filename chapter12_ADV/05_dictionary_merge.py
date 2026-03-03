# Dictionary Merge & Update Operators in Python
# Introduced in Python 3.9
# Used to combine dictionaries easily

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

d3 = d1 | d2
print(d3)

# Update Operator |=  (Updates Existing Dictionary)

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

d1 |= d2
print(d1)

# Real Practical Example
default_settings = {"theme": "light", "font": 12}
user_settings = {"theme": "dark"}

final_settings = default_settings | user_settings
print(final_settings)