# Importing the necessary libraries
import requests
import wget
import unzip

# Downloading a file using the requests library
# You can use the get method to download a file from a URL
url = "https://www.example.com/file.txt"
response = requests.get(url)

# Writing the content of the response to a file
with open("file.txt", "wb") as file:
    file.write(response.content)

# Downloading a file using the wget library
# You can use the wget.download method to download a file from a URL
url = "https://www.example.com/file.txt"
filename = wget.download(url)

# Extracting the contents of a ZIP file using the unzip library
# You can use the extractall method to extract all the files from a ZIP archive
with unzip.ZipFile("file.zip", "r") as zip_file:
    zip_file.extractall("extracted_files")

# You can also extract individual files from the ZIP archive
with unzip.ZipFile("file.zip", "r") as zip_file:
    zip_file.extract("file.txt", "extracted_files")
