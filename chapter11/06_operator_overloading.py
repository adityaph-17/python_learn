# Operator Overloading means giving special meaning to operators (+, -, *, <, etc.) when used with objects.

class Number :
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        sub = self.n - num.n
        if sub <0:
            return f"negative {sub}"
    
n = Number(2)
m = Number(10)
    
print (n + m)
print (n - m)

# Real Example – Adding Two Vectors
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)

