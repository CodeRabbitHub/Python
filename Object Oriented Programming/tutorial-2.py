class Dog:
    # Class level attribute
    species = "mammal"

    # class method
    @classmethod
    def make_sound(cls, sound):
        print(f"{cls.species} says {sound}")

    # class method as constructor
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2020 - birth_year)

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is a {self.age} years old {self.species}"


# Call class method
Dog.make_sound("Bark")

# Create a dog using class method as constructor
dog = Dog.from_birth_year("Rocky", 2015)

# Get the description of the dog
print(dog.description())

"""
Class methods are methods that are defined within a class and are usually used to operate on class attributes, rather than instance attributes. 
They are defined using the @classmethod decorator in Python, and they receive the class as the first argument, instead of an instance of the class.

Here's a brief explanation of the code:
+ @classmethod: This decorator is used to define class methods in Python.
+ def make_sound(cls, sound):: This is a class method that takes in the sound parameter and prints the species of the animal and the given sound. 
  The first parameter cls is a reference to the class itself and not the instance.
+ def from_birth_year(cls, name, birth_year):: This is a class method as a constructor. It takes in name and birth_year as parameters,
  calculates the age of the dog based on the current year and returns an instance of the Dog class.
+ dog = Dog.from_birth_year("Rocky", 2015): This creates an instance of the Dog class using the from_birth_year class method as a constructor and assigns it to the variable dog.
+ Dog.make_sound("Bark"): This line calls the make_sound class method on the Dog class and prints the sound "Bark".

"""
