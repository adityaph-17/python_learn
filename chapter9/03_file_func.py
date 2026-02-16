# in this file we learn about differnt function of file 

# read() :  Read full file
# readline() :  Read one line
# readlines() :  Read all lines (list)

# write() :  Write text
# writelines() :  Write multiple lines

# close() :  Close file

# tell() :  Current pointer position
# seek() :  Move pointer
# flush() :  Save data immediately

# readable() :  Check readable
# writable() :  Check writable

# 1️⃣ Write to file (overwrite mode)
with open("demo_func.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("Data written successfully.\n")


# 2️⃣ Read complete file
with open("demo_func.txt", "r") as f:
    print("Full file content using read():")
    print(f.read())

print("-------------------")


# 3️⃣ Read line by line
with open("demo_func.txt", "r") as f:
    print("Using readline():")
    print(f.readline())   # First line
    print(f.readline())   # Second line

print("-------------------")


# 4️⃣ Read all lines as list
with open("demo_func.txt", "r") as f:
    print("Using readlines():")
    print(f.readlines())

print("-------------------")


# 5️⃣ Using tell() and seek()
with open("demo_func.txt", "r") as f:
    print("Current pointer position:", f.tell())
    
    f.read(5)
    print("Pointer after reading 5 characters:", f.tell())
    
    f.seek(0)   # Move pointer to start
    print("Pointer after seek(0):", f.tell())

print("-------------------")


# 6️⃣ Append new data
with open("demo_func.txt", "a") as f:
    f.write("Line 4- append\n")

print("Data appended successfully.\n")


# 7️⃣ Check readable and writable
with open("demo_func.txt", "r") as f:
    print("Is file readable?", f.readable())
    print("Is file writable?", f.writable())

