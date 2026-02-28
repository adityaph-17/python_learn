# Inheritance is a feature of OOP that allows one class to acquire (reuse) the properties and methods of another class.

# We reuse existing code
# We reduce duplication
# We improve maintainability
# We can extend functionality

class car():

    def fun1(self):
        speed = 300
        print (f"car mak spped is :{speed} km/hr")

class contesta(car):

    def fun2(self):
        print(f"contesta max speed is 330 km/hr")

a = contesta()
a.fun1()
a.fun2()



# -------------------------------------------------------------------------------------------------

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is : {self.num * self.num}")

    def cube(self):
        print(f"The cube of {self.num} is : {self.num * self.num * self.num}")

    def squareroot(self):
        print(f"The squareroot of {self.num} is : {self.num ** 0.5}")


class Cal(Calculator):

    def __init__(self, num, distance, time):
        super().__init__(num)   # Call parent constructor
        self.distance = distance
        self.time = time

    def speed(self):
        print(f"Speed is : {self.distance / self.time} km/hr")


num = Cal(4, 100, 20)

num.square()
num.cube()
num.squareroot()
num.speed()