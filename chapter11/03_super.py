# super() is used to call parent class methods explicitly.

class A():
    def __init__(self):
        print("constructor of class A")

class B(A):
    def __init__(self):
        print ("printing this following by super keyword access the constuctor of super class :")
        super().__init__()
        print("constructor of class B")

obj = B()