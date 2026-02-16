# Function with arguments
def goodDay(name, ending):
    print("Good Morning, " + name + ", " + ending)

goodDay(
    input("Enter name: ").upper(),
    input("Enter ending greetings: ").upper()
)
print('\n')

# Function without arguments
def goodDay_no_arg():
    return "done"

b = goodDay_no_arg()
print(b)

print('\n')

# Default argument function
def goodDay1(name, ending="thanks"):
    print("Good Morning, " + name + "\n " + ending)

goodDay1(input("Enter name: ").upper())
print('\n')

goodDay1((input("Enter name: ").upper()),"thx")