try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Age should be a numeric value.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")

print("Execution continues")
