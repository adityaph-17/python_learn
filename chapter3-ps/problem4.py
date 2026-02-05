# in this code we replace double spaces with single spaces in a string
str = 'This  is a string with  double spaces.'
print("Original string:", str)
str = str.replace('  ', ' ')
print("String after replacing double spaces with single spaces:", str)
