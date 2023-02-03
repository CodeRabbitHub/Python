class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Title must not be empty")
        self._title = title

    @title.deleter
    def title(self):
        del self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not author:
            raise ValueError("Author must not be empty")
        self._author = author

    @author.deleter
    def author(self):
        del self._author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not pages:
            raise ValueError("Pages must not be empty")
        self._pages = pages

    @pages.deleter
    def pages(self):
        del self._pages


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(book.title)
book.title = "To Kill a Mockingbird"
print(book.title)
del book.title

"""
The property decorator in Python allows you to define a method as a property, so that it can be accessed like an attribute without 
the need for calling it as a method. You can also define getter, setter, and deleter methods for a property to control how the property 
is retrieved, set, and deleted.

In this example, the class Book has three properties: title, author, and pages. Each property is defined as a method with the property decorator. 
The getter methods are defined as simple return statements, while the setter and deleter methods are defined as title.setter and title.deleter respectively.
The setter method for the title property has a validation check to ensure that the title is not an empty string. The same validation check is applied to the 
author and pages properties.
You can access the properties of an instance of the Book class just like attributes. When you set a property, the corresponding setter method is called, 
and when you delete a property, the corresponding deleter method is called.
The output of this code will be:
    The Great Gatsby
    To Kill a Mockingbird
This example demonstrates how the property decorator, getter, setter, and deleter methods allow you to control how a property is accessed, set, and deleted. 
By using these techniques, you can add more advanced validation and control to your classes, making them more robust and flexible.

"""
