# To create a module, we need to write some functions or classes in a separate file with a `.py` extension.
# For example, let's create a module called `my_module.py` with a function `say_hello()`


def say_hello():
    print("Hello from my_module!")


# To use this module in another script, we can import it using the `import` statement.
# Let's create a new script called `main.py` and import `my_module`

import my_module

my_module.say_hello()
# Output: Hello from my_module!

# We can also use the `from ... import ...` statement to import specific functions or classes from a module
# For example, let's import the `say_hello` function directly into the `main` script

from my_module import say_hello

say_hello()
# Output: Hello from my_module!

# We can also give an alias to a module when we import it using the `as` keyword.
# For example, let's give the alias `mm` to `my_module`

import my_module as mm

mm.say_hello()
# Output: Hello from my_module!

# It is also possible to import multiple modules in one line

import my_module, math, sys

# We can use the functions and classes from these modules now

my_module.say_hello()
# Output: Hello from my_module!

print(math.pi)
# Output: 3.14...

print(sys.version)
# Output: 3.x.x (the version of Python you're using)
