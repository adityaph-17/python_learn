# Walrus Operator (:=)

# Introduced in Python 3.8
# It lets you assign and use a variable in the same line

# normal way
# name = input("Enter name: ")
# if name != "":
#     print(name)

# walrus operator assign and use at same time
if(name := input("Enter name :")) != "":
    print(name)

# without walurs
# line = input("Enter: ")
# while line != "quit":
#     print(line)
#     line = input("Enter: ")

# using walurs
while (line := str.lower(input("Enter: "))) != "quit":
    print(line)