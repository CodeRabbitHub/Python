number = 10

while number > 0:
    print(number)
    number -= 1

command = ""

while command != "quit":
    command = input(">").lower()
    print("ECHO", command)
