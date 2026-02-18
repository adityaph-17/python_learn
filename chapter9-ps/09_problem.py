# Write a program to find out whether a file is identical & matches the content of another file.

with open ("txt_files/08_demo.txt") as f:
    content1 = f.read()

with open ("txt_files/08_demo_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print ("file is identical & matches the content of another file")
else :
    print ("file is not identical & matches the content of another file")
