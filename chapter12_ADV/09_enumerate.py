# enumerate() is used to get:
# Index
# Value
# while looping

#without enumerate

# fruits = ["apple", "banana", "mango"]
# index = 0
# for fruit in fruits:
#     print(index, fruit)
#     index += 1

# with enumerate

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index,fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


students = ["Aman", "Rahul", "Priya", "Aditya"]

for roll_no, name in enumerate(students, start=101):
    print(f"Roll No: {roll_no} Name: {name}")
