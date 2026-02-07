# Write a program which finds out whether a given name is present in a list or not.

# List of names
names = ["Aditya", "Rahul", "Amit", "Neha", "Priya"]

# Input name to search
name = input("Enter the name to check: ")
# Check presence
if name in names:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")

