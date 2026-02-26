# Object Oriented Programming (OOP) is a programming concept where we create programs using objects and classes instead of only functions and variables.

# It focuses on:
# Data (variables)
# Behavior (functions)
# Combining both into a single unit called an object

# In normal programming (procedural programming):
# Code becomes large Difficult to manage Hard to reuse Hard to maintain

# OOP helps to: Organize code properly Make code reusable Improve security Reduce duplication Make large projects easier to handle

# pillars of oop :
# 	1.	Class
# 	2.	Object
# 	3.	Encapsulation
# 	4.	Abstraction
# 	5.	Inheritance
# 	6.	Polymorphism

# Class: A class is a blueprint or template used to create objects. It defines: Variables (data) Functions (methods)
# Object : An object is an instance of a class.

# Class = Design
# Object = Real thing created from design

class Employee:
    print ("hi, from class employee")
    name = "aditya" # this is an class attribute 
    age = 18

e1 = Employee()
e1.language = "python" # this is an instance (object) attribute

print (e1.name , e1.age)
print (e1.language)



# preferance of class vs instance attribute
class Show:
    age = 18
    language = "python"

show = Show()
show.language = "java" # this will print instance attribute takes priority

print (show.age , show.language)

