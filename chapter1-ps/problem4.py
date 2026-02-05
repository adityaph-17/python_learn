import os
#importing os module to interact with the operating system

directorypath = '/Users/aditya/Documents/Documents/python-learn/chapter1-ps'
#specifying the directory path

content = os.listdir(directorypath)
#listing all files and directories in the specified path

for file in content:
    #iterating through the list of files and directories
    print(file)
    #printing each file and directory name
    