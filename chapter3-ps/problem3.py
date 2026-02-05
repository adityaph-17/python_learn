# program to detect doulbe spaces in a string
str = 'This is a string with  double spaces.'

print(str.find('  '))  # find the index of first occurrence of double space
# if no double space found it will return -1

# string is inmutable so we cannot change it directly
print("Original string:", str)

