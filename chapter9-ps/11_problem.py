# 11. Write a python program to rename a file to “renamed_by_ python.txt".

import os

# old file name
old_name = "txt_files/11_demo.txt"

# new file name
new_name = "txt_files/11_demo_renamed.txt"

os.rename(old_name, new_name)

print("File renamed successfully.")