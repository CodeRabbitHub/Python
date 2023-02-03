class Dog:
    # Class level attribute
    species = "mammal"

    # Initializer / Instance Attributes
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # instance method
    def bark(self):
        print(f"{self.name} barks.")

    # instance method
    def description(self):
        return f"{self.name} is a {self.age} years old {self.breed}"


# Instantiate the Dog object
dog = Dog("Rocky", "Bulldog", 5)

# Access the instance attributes
print(dog.name)
print(dog.breed)
print(dog.age)

# Call instance method
dog.bark()

# Get the description of the dog
print(dog.description())

# Access the class attribute
print(dog.species)

"""
+ In object-oriented programming (OOP), a class is a blueprint for creating objects (instances), providing initial values for state (member variables or attributes), 
  and implementations of behavior (member functions or methods).
+ A class attribute is a variable that is shared by all instances of a class. It is defined outside of any method in the class and is usually  used to store information that is common 
  to all instances of a class, such as a default value for a property.
+ An instance is an individual object created from a class. Each instance of a class has its own unique set of attributes and can have its own behavior.
+ Instance attributes are variables that are specific to each instance of a class. They store information that is unique to each instance,  such as the name of an animal. 
  They are defined within the __init__ method of a class and are created when an instance of the class is created.
+ Instance methods are methods that operate on instance attributes. They are defined within a class, just like class methods, but they receive an 
  instance of the class as the first argument, and they can access and modify the instance attributes.
+ In this simple examples: 
  We have a python class named Dog. The class has three instance attributes: name, breed, and age, which are initialized when an 
  instance of the class is created. The class also has two instance methods: bark and description.
+ The bark method simply prints a string that includes the dog's name. The description method returns a string that describes the dog, 
  including its name, age, and breed.
+ An instance of the Dog class is created and stored in the dog variable. The instance attributes are accessed using dot notation, and the instance 
  methods are called using dot notation and parentheses.
+ Finally, the class attribute species is accessed using dot notation, and its value is printed. 

"""
