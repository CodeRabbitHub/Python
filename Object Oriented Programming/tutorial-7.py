class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
        )


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 215)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

print(book1)
print(len(book2))
print(book1 == book3)
print(book1 == book2)


"""
In Python, "magic methods" or "dunder methods" are special methods that have double underscores in their name and are used to define custom 
behavior for built-in operations. 

In this example:

+ __init__ is the constructor method that initializes the title, author, and pages attributes of the class.
+ __str__ is a magic method that returns a string representation of the object. This method is called when you call the print function or use the object 
  in a string context.
+ __len__ is a magic method that returns the length of the object. This method is called when you call the len function.
+ __eq__ is a magic method that defines the behavior for the equality operator ==. This method is called when you compare two instances of the class using 
  the equality operator.

The output of this code will be:

    The Great Gatsby by F. Scott Fitzgerald, 180 pages
    215
    True
    False

This example demonstrates how magic methods allow you to define custom behavior for built-in operations. 
By using magic methods, you can make your classes more usable and more closely resemble built-in types in Python.

"""
