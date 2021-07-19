def greet(name):
    print(f"hi {name}")


def get_greet(name):
    return f"hi {name}"


message = get_greet("tom")
file = open("context.txt", "w")
file.write(message)
file.close()

print(greet("Tom"))
greet("Tom")

# Functions can be used to carry
# out a task or return a value.
