# self is a reference to the current object of a class.

# When we create multiple objects from one class, each object has its own data. self helps Python understand: 👉 Which object’s data we are referring to.

# 1.	self represents current object.
# 2.	It must be first parameter in instance method.
# 3.	It is passed automatically.
# 4.	It is used to access object attributes and methods.
# 5.	It helps differentiate between instance variables and local variables

# class Student:
#     def show(name):
#         print(name)

# s1 = Student()
# s1.show("Aditya")  this will give error because Python automatically sends the object, but method is not ready to receive it

class Student:
    def show(self, name):
        print(name)


    @staticmethod #Static method = Normal function inside class without using object data. 	It does not take self or cls.
    def great():
        print("hello world")

s1 = Student()
s1.show("Aditya")

s1.great()