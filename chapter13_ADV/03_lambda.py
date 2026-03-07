# lambda is used to create a small anonymous function (function without name).

# Normal Function
def add(a,b):
    return a+b

print (add(3,4))

#  Using lambda
add = lambda a, b: a + b
print(add(3, 4))

# real example
students = [("Aditya", 80), ("Rahul", 60), ("Priya", 90)]

students.sort(key=lambda x: x[1])

print(students)
print(type(students))

# def get_marks(student):
#     return student[1]
