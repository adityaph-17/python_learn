#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Pet(Animal):
    def play(self):
        print(f"{self.name} is playing.")

class Dog(Pet):
    def bark(self):
        print(f"{self.name} is barking. woof! woof!")

obj = Dog("dog")
obj.eat()
obj.play()
obj.bark()