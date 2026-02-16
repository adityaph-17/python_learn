#Loops in Python are used to repeat a block of code multiple times

#For loop : Used when you know how many times you want to repeat something.

# syntax:--
# for variable in sequence:
#     statement(s)

for i in range(1,6):
    print(i)
print("\n")

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# While Loop : Used when you want to repeat code as long as a condition is true.

# syntax--
# while condition:
#     statement(s)


i =1
while(i <= 6):
    print(i)
    i+= 1