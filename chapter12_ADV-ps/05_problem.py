# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n= int(input("enter a number :"))

tables = [n*i for i in range(1,11)]

with open("05_2file.txt", "a") as f:
    f.write(f"table of :{n} is : {str(tables)}\n")
