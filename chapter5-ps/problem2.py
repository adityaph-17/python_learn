# Write a program to input eight numbers from the user and display all the unique numbers (once).

set = set()
for i in range(8):
    num = int(input("Enter a number: "))
    set.add(num)

print("Unique numbers entered:", set)
