# A class method is a method that is bound to the class, not the object (instance).

# It works with class variables
# It uses cls instead of self
# It is defined using the @classmethod decorator

class A():
    a= 10
    @classmethod # without this is assign new value to "a" by obj 100
    def get(cls):
        print(f"The value of a is : {cls.a}")

obj = A()
obj.a = 100
print(f"the a value of instance attribute is :{obj.a}")

obj.get()