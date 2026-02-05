a =5 
t = type(a)
print("The type of a is:", t)  # The type of a is: <class 'int'>

b = 3.14
t = type(b)
print("The type of b is:", t)  # The type of b is: <class 'float'>

c = "Hello, World!"
t = type(c)
print("The type of c is:", t)  # The type of c is: <class 'str'>

is_active = True
t = type(is_active)
print("The type of is_active is:", t)  # The type of is_active is: <class 'bool'>

fruits = ["apple", "banana", "cherry"]
t = type(fruits)
print("The type of fruits is:", t)  # The type of fruits is: <class 'list'>

person = {"name": "Alice", "age": 25}
t = type(person)
print("The type of person is:", t)  # The type of person is: <class 'dict'>

c = None
t = type(c)
print("The type of c is:", t)  # The type of c is: <class 'NoneType'>
# This code demonstrates how to check the data types of various variables in Python using the type() function.

# typecasting
x = 10        # integer
print("Original types:", type(x))
# Converting integer to float
x_float = float(x)
print("x as float:", x_float, type(x_float))
# Converting integer to string
x_str = str(x)
print("x as string:", x_str, type(x_str))
y = 3.14      # float
print("Original types:"+ str(type(y)))
print("Original types:", type(y))
# Converting float to integer
y_int = int(y)
print("y as integer:", y_int, type(y_int))
