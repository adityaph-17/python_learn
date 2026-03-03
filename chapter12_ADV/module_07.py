# __name__ is a special built-in variable.
# It tells:
# How the file is being used.

# Case: When File is Run Directly
def Func1():
    print(__name__) #Output: __main__ if run directly by file

if __name__ == "__main__":
    print("This file is running directly")
    Func1()

else:
    print("this file is running from import(__name.py)")

# Real Practical Use
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))

else:
    print("not from direct file import from __name__.py")


# Used in real projects
# Prevents test code running on import
# Very common interview question
