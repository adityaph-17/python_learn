# Types of Inheritance in Python

# 1. single inheritance - one childe inherit from one parent
# 2. multiple inheritance - one child inherit from more than one parent 
# 3. multilevel inheritance - one child inherit from one class which is already inherit from another (in level)

class A():
    def fun1(self):
        print ("hello from class A")

class B(A): # single inheritance
    def fun2(self):
        print ("hello from class B")

# -----------------------------------------------

class C():
    def fun3(self):
        print ("hello from class C")

class D(A, C): # multiple inheritance
    def fun4(self):
        print ("hello from class D")

# -----------------------------------------------

class E(B): # multi level inheritance (b is already inherit by A)

    def fun5(self):
        print("hello from class E")


o1 = B()
o1.fun1()
o1.fun2()

o2 = D()
o2.fun1()
o2.fun3()
o2.fun4()

o3 = E()
o3.fun1()
o3.fun2()
o3.fun5()
