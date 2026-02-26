# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    Company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name 
        self.salary = salary
        self.pin = pin 

    def get(self):
        print(f"for programmer :{self.name}, salary is :{self.salary} and pin is :{self.pin}.")

p1 = Programmer("aditya", 2000000, 431401)
p1.get()

p2 = Programmer("demo1",20008499, 123123)
p2.get()

p3 = Programmer("demo2", 3000000, 98098)
p3.get()