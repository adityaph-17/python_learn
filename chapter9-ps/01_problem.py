# 1. Write a program to read the text from a given file ‘poems.txt’ and find outwhether it contains the word ‘twinkle’.


with open("txt_files/01_demo.txt", "r") as f:
    content = f.read()
    if ("danger" in content):
        print ("The word is present in file")

    else:
        print ("The word is not present in file")