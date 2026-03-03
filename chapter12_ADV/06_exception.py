try:
    a = int(input("Enter a number :"))
    print(a)
except Exception as e:
    print("enter a valid number", e)


# raising the error

a = int(input("enter a number:"))
b = int(input("enter a number:"))

if (b == 0):
    raise ZeroDivisionError("we canot divide any number by zero.")
else:
    print (f'division is {a/b}')

# try-except-else : goes inside else when ever try execute if except then else not execute

try:
    a = int(input("Enter a number :"))
    print(a)
except Exception as e:
    print("enter a valid number", e)

else: # if try execute then enter to else
    print("thx")


# finally ---

try:
    a = int(input("Enter a number :"))
    print(a)
except Exception as e:
    print("enter a valid number", e)

finally:
    print("i am finally") # get use in function when return it execute every time try or exception

