#  Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, values):
        self.values = values

    # Overriding len()
    def __len__(self):
        return len(self.values)
    
    # for print in readable format 
    def __str__(self):
        return str(self.values)

# Test the implementation
v1 = Vector([1, 2, 3, 4, 5])
print(len(v1))