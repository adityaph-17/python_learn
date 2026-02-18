# Write a program to find out the line number where python is present from ques 6.

with open ("txt_files/06_demo.txt") as f:
    lines = f.readlines()

lineno = 1 # We create this variable to count which line we are checking Because: for line in lines: gives us the line content But it does NOT tell us the line number

for line in lines :
    if ("python" in line.lower()):
        print (f"yes python present on line no :{lineno}")
        break
    lineno +=1
else:
    print ("python is not present")


'''

linemo += 1 :


Start → lineno = 1
Check first line → not found → increase → lineno = 2
Check second line → not found → increase → lineno = 3
Check third line → found → print 3

'''