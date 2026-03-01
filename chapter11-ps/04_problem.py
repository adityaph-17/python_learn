# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading + operator
    def __add__(self, other):# take other because it internally become c1.__add__(c2) c2 has 2 number
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    # Overloading * operator
    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    # For printing
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = Complex(2,3)
c2 = Complex(4,5)
print (c1+c2)