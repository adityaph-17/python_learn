# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.

with open ("txt_files/04_demo.txt", "r") as f:
    content = f.read()

contentnew= content.replace("donkey", "######")

with open ("txt_files/04_demo.txt", "w") as f:
    f.write(contentnew)