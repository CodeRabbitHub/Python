class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Sound"


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


dog = Dog("Max", "Canine")
cat = Cat("Mia", "Feline")

print(f"{dog.name} is a {dog.species} and makes the sound {dog.make_sound()}")
print(f"{cat.name} is a {cat.species} and makes the sound {cat.make_sound()}")

"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create new classes that are based on existing classes, 
inheriting their attributes and methods. The new class is called a subclass, and the existing class is called the superclass. The subclass can use the 
attributes and methods from the superclass, and also add or override them if necessary.

This enables you to reuse code and avoid duplicating it, making your code more maintainable and organized. You can also use inheritance to model 
real-world relationships between objects. For example, you can create a Person class as a superclass, and then create subclasses for specific types 
of people, such as Student or Teacher.

In this example:

+ Animal is a class that defines basic attributes for animals, name and species, and a method make_sound that returns the string "Sound".
+ Dog and Cat are classes that inherit from Animal. They both have their own implementation of the make_sound method, which returns "Bark" and "Meow" respectively.
+ dog = Dog("Max", "Canine") creates an instance of the Dog class, with the name "Max" and species "Canine".
+ cat = Cat("Mia", "Feline") creates an instance of the Cat class, with the name "Mia" and species "Feline".
The output of this code will be:

    Max is a Canine and makes the sound Bark
    Mia is a Feline and makes the sound Meow
    
"""
