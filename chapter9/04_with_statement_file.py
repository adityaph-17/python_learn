# with statement is used to open a file safely.

# It automatically:
# ✅ Opens the file
# ✅ Closes the file
# ✅ Even closes if error occurs


f = open("demo_with.txt", "w")
f.write("Hello Aditya")
str = " hi i am aditya learning python language\n"
f.write(str)
f.close()

#old without with statement
f = open("demo_with.txt")
data = f.read()
print(data)
f.close()



with open("demo_with.txt", "r") as f:
    data = f.read()
    print(data)