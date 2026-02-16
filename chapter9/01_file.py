# in this code we learn about file operations like read and write ,etc.


# File : A place to store data permanently (like .txt, .csv, etc.)
# File I/O means reading from and writing to files.

# Opening a File
# In Python, we use the open() function.
# open("filename", "mode")

'''

"r" : Read (default)
"w" : Write (creates new file / overwrite)
"a" : Append (add data at end)
"r+" : Read + Write

'''

f = open("demo.txt")
data = f.read()
print(data)
f.close()
