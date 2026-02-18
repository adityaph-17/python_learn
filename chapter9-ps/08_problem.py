# Write a program to make a copy of a text file “this. txt”

with open ("txt_files/08_demo.txt") as f:
    content = f.read()

with open ("txt_files/08_demo_copy.txt", "w") as f:
    f.write(content)