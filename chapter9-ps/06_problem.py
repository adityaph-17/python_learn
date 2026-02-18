# Write a program to mine a log file and find out whether it contains ‘python’.

with open ("txt_files/06_demo.txt") as f:
   content =  str.lower(f.read())

if ("python" in content):
    print ("yes python is present in 06_demo.txt file !")
else:
    print ("No , python is not present in file")