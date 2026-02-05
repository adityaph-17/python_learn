# If the names of 2 friends are same; what will happen to the program in problem 6?

a= {
    "Aditya": "Python",
    "Rahul": "Java",
    "Priya": "C++",
    "Aditya": "JavaScript"  # This overwrites the previous value for "Aditya"
}

print("Favorite languages of friends:", a)
# Output will be:
# Favorite languages of friends: {'Aditya': 'JavaScript', 'Rahul': 'Java', 'Priya': 'C++'}
# Explanation:
# In a dictionary, keys must be unique. If the same key is used more than once
# (in this case, the name "Aditya"), the last value assigned to that key will
# overwrite any previous values. Therefore, only the last entry for "Aditya"
# ("JavaScript") is retained in the dictionary.
# The program will overwrite the value for the duplicate name key.
# The dictionary will only keep the last entry for the duplicate key.
# So, the output will show only one entry for "Aditya" with the value "JavaScript".
# The program will not throw an error, but the earlier value will be lost.



# If languages of two friends are same; what will happen to the program in problem 6?
b= {
    "Aditya": "Python",
    "Rahul": "Java",
    "Priya": "Python",  # Same language as Aditya
    "Sneha": "C++"
}

print("Favorite languages of friends:", b)
# Output will be:
# Favorite languages of friends: {'Aditya': 'Python', 'Rahul': 'Java', 'Priya': 'Python', 'Sneha': 'C++'}
# Explanation:
# In a dictionary, values do not need to be unique. Multiple keys can have the
# same value. In this case, both "Aditya" and "Priya" have "Python" as their favorite
# language. The dictionary will store both entries without any issues.
# The program will work normally and store all entries.
# The output will show both friends with the same favorite language.
# There will be no overwriting since the keys (names) are unique.
# So, the output will show both "Aditya" and "Priya" with the value "Python".
# The program will not throw an error, and all entries will be retained.    

