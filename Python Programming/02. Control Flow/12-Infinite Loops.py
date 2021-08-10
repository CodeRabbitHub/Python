while True:
    command = input(">").lower()
    print("ECHO", command)
    if command.lower() == "quit":
        break
