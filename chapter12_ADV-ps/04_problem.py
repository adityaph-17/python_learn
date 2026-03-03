# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’

try:
    a= int(input("enter a number:"))
    b= int(input("enter a number:"))

    c= a/b
    print (f"division :{c}")

except ZeroDivisionError as e:
    print("infinite")
