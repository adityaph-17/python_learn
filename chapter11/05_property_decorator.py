# A property decorator is used to:

# Control access to attributes
# Add validation logic
# Implement getter, setter, and deleter methods
# Provide data encapsulation

# It allows you to call a method without parentheses like an attribute.

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property # @property makes the method behave like a variable. We write s.marks NOT s.marks().
    def marks(self):
        return self._marks

s = Student(85)
print(s.marks)



#-----------------------------------------------------------------------------

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter           #To allow modification with validation:
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks")
        else:
            self._marks = value

s = Student(80)
s.marks = 95
print(s.marks)



#-------------------------------------------------------------------------
#Property with Deleter

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.deleter
    def marks(self):
        print("Deleting marks...")
        del self._marks

s = Student(90)
del s.marks



# Real-Life Example

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self._salary = value

emp = Employee(50000)
emp.salary = -2000
emp.salary = 60000
print(emp.salary)


# @property → getter
# @variable.setter → setter
# @variable.deleter → deleter
# Method name must be same



