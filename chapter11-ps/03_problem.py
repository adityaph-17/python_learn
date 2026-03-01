# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def apply_increment(self, incre):
        self.oldsalary = self.salary
        self.inc = incre
        self.salary = self.salary +self.inc

    @property
    def increment(self):
        print (f"increment ={((self.salary-self.oldsalary)/self.oldsalary)*100}")

    def show_details(self):
        print(f"old salay :{self.oldsalary}")
        print(f"increment :{self.inc}\nsalary after increment : {self.salary} ")

o = Employee(10000)

o.apply_increment(2010)
o.show_details()
o.increment