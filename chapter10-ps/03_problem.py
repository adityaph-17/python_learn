# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’ . Does this change the class attribute?

class Demo:
    a =11

o = Demo()
print(o.a) # prints the class attribute because instance attribute in not present 

o.a = 15 # it set the instance attribute
print(o.a) # it prints the instaance attribute (prioprity)
print (Demo.a)# internally

# not change the class attribute 