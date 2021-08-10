message = "a"


def greet(name):
    message = "a"


def send_email(name):
    global message  # modifying global message value.
    message = "b"


# name and message are called as local variabels
# Outside the functions they are called global variables

# bad practice to modify global variables inside function
