# Write a program to store seven items in a list entered by the user.

items = []
for i in range(7):
   a = input("Enter the name of an item to list: ")
   items.append(a)
print("The list of items you entered is:", items)