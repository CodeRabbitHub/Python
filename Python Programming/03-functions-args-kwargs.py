# Defining Functions
def greet(name):
    """A function that greets the person passed in as a parameter"""
    print("Hello, " + name + ". How are you today?")


# Calling Functions
greet("John")  # Output: Hello, John. How are you today?

# Naming Conventions
# Function names should be lowercase, with words separated by underscores
# (e.g. greet_person, not greetPerson or greetperson)

# Arguments
def greet_person(name, age):
    """A function that greets the person passed in as a parameter and prints their age"""
    print("Hello, " + name + ". You are " + str(age) + " years old.")


greet_person("John", 36)  # Output: Hello, John. You are 36 years old.

# Types of Functions
# 1. Function with no return value
def greet(name):
    """A function that greets the person passed in as a parameter"""
    print("Hello, " + name + ". How are you today?")


# 2. Function with return value
def sum_numbers(a, b):
    """A function that returns the sum of two numbers"""
    return a + b


# Keyword Arguments
def greet_person(name, age):
    """A function that greets the person passed in as a parameter and prints their age"""
    print("Hello, " + name + ". You are " + str(age) + " years old.")


greet_person(age=36, name="John")  # Output: Hello, John. You are 36 years old.

# Default Arguments
def greet_person(name, age=20):
    """A function that greets the person passed in as a parameter and prints their age"""
    print("Hello, " + name + ". You are " + str(age) + " years old.")


greet_person("John")  # Output: Hello, John. You are 20 years old.

# *args
def sum_numbers(*args):
    """A function that returns the sum of all the numbers passed in as arguments"""
    total = 0
    for num in args:
        total += num
    return total


print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# **kwargs
def greet_person(**kwargs):
    """A function that greets the person passed in as keyword arguments"""
    if "name" in kwargs and "age" in kwargs:
        print(
            "Hello, "
            + kwargs["name"]
            + ". You are "
            + str(kwargs["age"])
            + " years old."
        )
    else:
        print("Hello, Stranger!")


greet_person(name="John", age=36)  # Output: Hello, John. You are 36 years old.

# Global Variables
person_name = "John"


def greet_person():
    """A function that greets the person using a global variable"""
    global person_name
    print("Hello, " + person_name + ". How are you today?")


# Modifying Global Variables Inside Functions
def change_person_name(new_name):
    """A function that changes the value of a global variable"""
    global person_name
    person_name = new_name


change_person_name("Jane")
greet_person()  # Output: Hello, Jane. How are you today?

# Opening and Writing to Files
# Opening a File
file = open("test.txt", "w")  # "w" means we're opening the file in write mode

# Writing to a File
file.write("Hello, World!")

# Closing a File
file.close()

# Opening and Reading a File
file = open("test.txt", "r")  # "r" means we're opening the file in read mode

# Reading a File
print(file.read())  # Output: Hello, World!

# Closing a File
file.close()
