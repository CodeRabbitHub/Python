import glob

# Use the glob.glob() function to search for all .txt files in the current directory
txt_files = glob.glob("*.txt")

# Print the list of text files
print("Text files:", txt_files)

# Use the glob.glob() function to search for all files in the current directory starting with "data"
data_files = glob.glob("data*")

# Print the list of data files
print("Data files:", data_files)

# Use the glob.glob() function to search for all files in the current directory that contain the word "example"
example_files = glob.glob("*example*")

# Print the list of example files
print("Example files:", example_files)

# Use the glob.glob() function to search for all .txt files in a subdirectory called "docs"
docs_files = glob.glob("docs/*.txt")

# Print the list of text files in the "docs" subdirectory
print("Text files in 'docs' subdirectory:", docs_files)

# Use the glob.glob() function to search for all .txt files in a subdirectory called "docs" and its subdirectories
recursive_docs_files = glob.glob("docs/**/*.txt", recursive=True)

# Print the list of text files in the "docs" subdirectory and its subdirectories
print("Recursive text files in 'docs' subdirectory:", recursive_docs_files)

# Use the glob.iglob() function to search for all .txt files in the current directory
# Note: the iglob() function returns an iterator instead of a list, which can be useful for processing large amounts of data
txt_files_iterator = glob.iglob("*.txt")

# Print the list of text files using the iterator
print("Text files (iterator):")
for file in txt_files_iterator:
    print(file)


import json

# A sample dictionary to be converted to JSON
person = {
    "name": "John Doe",
    "age": 32,
    "address": {
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
    },
    "phone_numbers": ["555-555-1212", "555-555-1213"],
}

# Convert the dictionary to a JSON string using json.dumps()
person_json = json.dumps(person)

# Print the JSON string
print("JSON representation of the dictionary:", person_json)

# Convert the JSON string back to a dictionary using json.loads()
person_dict = json.loads(person_json)

# Print the dictionary
print("Dictionary representation of the JSON:", person_dict)

# Write the JSON string to a file using json.dump()
with open("person.json", "w") as file:
    json.dump(person, file)

# Read the JSON string from a file using json.load()
with open("person.json", "r") as file:
    person_from_file = json.load(file)

# Print the dictionary read from the file
print("Dictionary read from file:", person_from_file)
