import argparse

# A class that represents a person with a name and age
class Person:
    def __init__(self, name, age):
        # Initialize the name and age of the person
        self.name = name
        self.age = age

    def read_data(self):
        # Print a message indicating that the data is being read
        print(f"Reading data of {self.name}, age {self.age}")

    def write_data(self):
        # Print a message indicating that the data is being written
        print(f"Writing data of {self.name}, age {self.age}")


if __name__ == "__main__":
    # Create an argument parser object
    parser = argparse.ArgumentParser(
        # A short name for the script
        prog="Person Data Management",
        # A description of the script
        description="A tutorial on argparse",
        # A message to be displayed after the help message
        epilog="This script helps manage person data",
        # Disable the help message
        add_help=False,
    )

    # Add arguments to the parser object
    parser.add_argument("-n", "--name", type=str, help="Name of the person")
    parser.add_argument("-a", "--age", type=int, help="Age of the person")

    # Add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--read", action="store_true", help="Read the data")
    group.add_argument("-w", "--write", action="store_true", help="Write the data")

    # Parse the arguments
    args = parser.parse_args()

    # Create an instance of the Person class
    person = Person(args.name, args.age)

    # Call the read_data() or write_data() method based on the parsed arguments
    if args.read:
        person.read_data()
    elif args.write:
        person.write_data()
