# The pathlib module in Python provides an object-oriented interface for working with file paths. The Path objects created by pathlib
# are designed to make common file system tasks, such as working with directories and files, reading and writing to files, and accessing
# file metadata, easier and more efficient.

# Import the pathlib module
import pathlib

# Creating a Path object representing a file path
file_path = pathlib.Path("test_file.txt")
print("File path:", file_path)

# Creating a Path object representing a directory path
dir_path = pathlib.Path("test_dir")
print("Directory path:", dir_path)

# Joining multiple paths into a single path
joined_path = dir_path / "test_file.txt"
print("Joined path:", joined_path)

# Getting the parent directory of a path
parent_dir = file_path.parent
print("Parent directory of", file_path, ":", parent_dir)

# Getting the name of the file or directory
name = file_path.name
print("Name of", file_path, ":", name)

# Checking if a path exists
print(file_path, "exists:", file_path.exists())

# Checking if a path represents a file
print(file_path, "is a file:", file_path.is_file())

# Checking if a path represents a directory
print(dir_path, "is a directory:", dir_path.is_dir())

# Getting the absolute path of a path
abs_path = file_path.resolve()
print("Absolute path of", file_path, ":", abs_path)

# Creating a new file using path object
file_path.touch()
print(file_path, "created")

# Writing content to a file using path object
file_path.write_text("Test content")
print("Content written to", file_path)

# Reading content from a file using path object
file_content = file_path.read_text()
print("Content of", file_path, ":", file_content)

# Creating a new directory using path object
dir_path.mkdir()
print(dir_path, "created")

# Removing a file or directory using path object
file_path.unlink()
dir_path.rmdir()
print(file_path, "removed")
print(dir_path, "removed")

# Create a Path object from a string
path = pathlib.Path("/tmp/test_file.txt")

# Get the absolute path
abs_path = path.resolve()
print("Absolute path:", abs_path)

# Get the parent directory
parent_dir = path.parent
print("Parent directory:", parent_dir)

# Get the name of the file or directory
name = path.name
print("Name:", name)

# Get the suffix of the file
suffix = path.suffix
print("Suffix:", suffix)

# Get the stem of the file (name without suffix)
stem = path.stem
print("Stem:", stem)

# Check if the path exists
print("Exists:", path.exists())

# Check if the path is a file
print("Is a file:", path.is_file())

# Check if the path is a directory
print("Is a directory:", path.is_dir())

# Check if the path is symbolic link
print("Is a symbolic link:", path.is_symlink())

# Get the owner of the file or directory
owner = path.owner()
print("Owner:", owner)

# Get the permissions of the file or directory
permissions = oct(path.stat().st_mode & 0o777)
print("Permissions:", permissions)

# Get the size of the file or directory
size = path.stat().st_size
print("Size:", size)

# Get the creation time of the file or directory
ctime = path.stat().st_ctime
print("Creation time:", ctime)

# Get the modification time of the file or directory
mtime = path.stat().st_mtime
print("Modification time:", mtime)

# Get the access time of the file or directory
atime = path.stat().st_atime
print("Access time:", atime)

# Create a new file
path.touch()
print("File created:", path)

# Create a directory
new_dir = pathlib.Path("/tmp/test_dir")
new_dir.mkdir()
print("Directory created:", new_dir)

# Rename a file or directory
renamed_path = path.with_name("renamed_file.txt")
path.rename(renamed_path)
print("File renamed from", path, "to", renamed_path)

# Remove a file or directory
renamed_path.unlink()
print("File removed:", renamed_path)

# List all the files in a directory
for child in new_dir.iterdir():
    print("Child:", child)

# Search for a file with a certain suffix
for file in new_dir.glob("*.txt"):
    print("Matching file:", file)

# Search for a file recursively
for file in new_dir.rglob("*.txt"):
    print("Recursively matching file:", file)
