# in this code we understand str() function

str = '0123456789'
print("Original String:", str)

# using len() function to get the length of the string
print("Length of the string:", len(str))  # output: 10

# using endswith() function to check if the string ends with a specific substring
print("Does the string end with '9'?:", str.endswith('9'))  # output: True
print("Does the string end with '5'?:", str.endswith('5'))  # output: False

#using count() function to count occurrences of a substring in the string
print("Count of '2' in the string:", str.count('2'))  # output: 1

str1 = 'hello world'

# using capitalize() function to capitalize the first character of the string
capitalized_str = str1.capitalize()
print("Capitalized String:", capitalized_str)  # output:   Hello world  

# usint title() function to convert the first character of each word to uppercase
titled_str = str1.title()
print("Titled String:", titled_str)  # output: Hello World

# using find() function to find the index of the first occurrence of a substring
index = str1.find('l')
print("Index of first occurrence of 'l':", index)  # output: 2

# using replace() function to replace occurrences of a substring with another substring
replaced_str = str1.replace('world', 'there')
print("Replaced String:", replaced_str)  # output: hello there

str1.replace('world', 'python')  # this will not change str1 as strings are immutable
print("Original String after replace attempt:", str1)  # output: hello world

# usin upper() function to convert the string to uppercase
upper_str = str1.upper()
print("Uppercase String:", upper_str)  # output: HELLO WORLD