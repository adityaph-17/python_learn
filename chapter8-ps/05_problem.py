'''
Write a python function to print first n lines of the following pattern:
***
** 
*

- for n = 3
'''


def pattern(n):
    if n == 0:     # Base case
        return
    print("*" * n)
    pattern(n - 1) # Recursive call

n = int(input("Enter number of lines: "))
pattern(n)

# using loop Right Aligned Pattern

def pattern(n):
    for i in range(n, 0, -1):
        spaces = n - i
        print(" " * spaces + "*" * i)

n = int(input("Enter number of lines: "))
pattern(n)
