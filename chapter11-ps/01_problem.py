# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDvector:
    def __init__(self,i, j):
        self.i = i
        self.j = j

    def show(self):
        print (f"the 3d vector is i = {self.i}, j = {self.j}")

class ThreeDvector(TwoDvector):
    def __init__(self,i, j, k):
        super().__init__(i , j)
        self.k = k
    
    def show(self):
        print (f"the 3d vector is i = {self.i}, j = {self.j}, k = {self.k}")


a = TwoDvector(2,3)
b = ThreeDvector(7,5,6)

a.show()
b.show()