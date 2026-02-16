# Built in functions (Already present in python)
# len(), range(), print()

# User defined functions (Defined by the user)
# like avg():

def avg():
    a = int(input('Enter first num :'))
    b = int(input('Enter second num :'))
    c = int(input('Enter third num :'))

    avg = (a+b+c)/3
    print (avg)
    print("\n")

avg()