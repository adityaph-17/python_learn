# A constructor is a special method in a class that: Executes automatically when an object is created Is used to initialize (assign values to) object variables

class Employee:

    name = "aditya"
    age = 18

    def get(self):
        print(f"name is {self.name} and age is {self.age}")

    def __init__(self): # dunder method which is automatically called.
        print("it will call auto matically when object is created ")     

e1 = Employee()
e1.get()

e2 = Employee()# contructor (dunder method ) called 


class Student:

    def __init__(self, name, age): # with parameters
        self.name = name
        self.age = age

    def show_data(self): 
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Aditya", 20)
s1.show_data()


# Constructor → Process of setting initial values when object is created



