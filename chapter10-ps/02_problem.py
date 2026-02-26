# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is :{self.num * self.num}")

    def cube(self):
        print(f"The cube of {self.num} is :{self.num * self.num * self.num}")

    def squareroot(self):
        print(f"The squareroot of {self.num} is :{self.num **1/2}")

num = Calculator(2)
num.square()
num.cube()
num.squareroot()