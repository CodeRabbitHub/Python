import os

# Get the current working directory using os.getcwd()
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Change the current working directory using os.chdir()
os.chdir("/tmp")
print("Current working directory after change:", os.getcwd())

# Get the list of files and directories in the current directory using os.listdir()
files_and_dirs = os.listdir()
print("Files and directories in the current directory:", files_and_dirs)

# Create a new directory using os.mkdir()
os.mkdir("test_dir")
print("Directory created:", "test_dir")

# Remove a directory using os.rmdir()
os.rmdir("test_dir")
print("Directory removed:", "test_dir")

# Rename a file or directory using os.rename()
with open("test_file.txt", "w") as file:
    file.write("Test content")
os.rename("test_file.txt", "renamed_file.txt")
print("File renamed from test_file.txt to renamed_file.txt")

# Remove a file using os.remove()
os.remove("renamed_file.txt")
print("File removed:", "renamed_file.txt")

# Get the details of a file or directory using os.stat()
file_stat = os.stat("/tmp")
print("Details of the directory /tmp:", file_stat)

# Get the absolute path of a file or directory using os.path.abspath()
abs_path = os.path.abspath("/tmp")
print("Absolute path of the directory /tmp:", abs_path)

# Check if a path exists using os.path.exists()
print("/tmp exists:", os.path.exists("/tmp"))
print("/nonexistent_path exists:", os.path.exists("/nonexistent_path"))

# Check if a path is a file using os.path.isfile()
print("/tmp is a file:", os.path.isfile("/tmp"))
print("/etc/passwd is a file:", os.path.isfile("/etc/passwd"))

# Check if a path is a directory using os.path.isdir()
print("/tmp is a directory:", os.path.isdir("/tmp"))
print("/etc/passwd is a directory:", os.path.isdir("/etc/passwd"))

# Get the base name and directory name of a file using os.path.basename() and os.path.dirname()
file_path = "/etc/passwd"
base_name = os.path.basename(file_path)
dir_name = os.path.dirname(file_path)
print("Base name of", file_path, ":", base_name)
print("Directory name of", file_path, ":", dir_name)

# Join paths using os.path.join()
joined_path = os.path.join("/tmp", "test_dir")
print("Join path:", joined_path)

# Split a file extension from its name using os.path.splitext()
file_name, file_ext = os.path.splitext("/etc/passwd")
print("File name:", file_name)
print("File extension:", file_ext)

# Get the size of a file using os.path.getsize()
file_size = os.path.getsize("/etc/passwd")
print("Size of /etc/passwd:", file_size, "bytes")

# Check if a path is an absolute path using os.path.isabs()
print("/tmp is an absolute path:", os.path.isabs("/tmp"))
print("tmp is an absolute path:", os.path.isabs("tmp"))

# Change the current working directory back to the original directory
os.chdir(current_dir)
print("Current working directory after change back:", os.getcwd())
