import sys
import string
import random
import hashlib
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)


def generate_password(input_string):
    """
    Generates a secure password based on the combination of an input string.

    Args:
        input_string (str): The input string used for generating the password.

    Returns:
        str: A securely generated password.
    """
    # Create a SHA-256 hash object and encode the input string as bytes.
    hash_object = hashlib.sha256(input_string.encode())
    # Calculate the hash value (digest) and convert it to hexadecimal representation.
    hash_value = hash_object.hexdigest()
    # Seed the random generator with the hash value.
    random.seed(hash_value)

    # Define the set of characters for generating the password.
    password_characters = string.ascii_letters + string.digits + string.punctuation

    # Define the minimum number of characters needed of each kind.
    min_chars_each_kind = 2

    # Define the total length of the password.
    total_password_length = 12

    # Generate the required characters of each kind.
    symbols = [random.choice(string.punctuation) for _ in range(min_chars_each_kind)]
    uppercase = [
        random.choice(string.ascii_uppercase) for _ in range(min_chars_each_kind)
    ]
    lowercase = [
        random.choice(string.ascii_lowercase) for _ in range(min_chars_each_kind)
    ]
    digits = [random.choice(string.digits) for _ in range(min_chars_each_kind)]

    # Calculate the remaining password length after generating the required characters.
    remaining_password_length = total_password_length - len(
        symbols + uppercase + lowercase + digits
    )

    # Generate the remaining characters to complete the password.
    remaining_characters = [
        random.choice(password_characters) for _ in range(remaining_password_length)
    ]

    # Combine all generated characters and shuffle them to create the final password.
    password = symbols + uppercase + lowercase + digits + remaining_characters
    random.shuffle(password)

    return "".join(password)


# Define a class named PasswordGeneratorApp that inherits from QWidget
class PasswordGeneratorApp(QWidget):
    # Constructor method
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.setWindowTitle("Password Generator")  # Set the window title
        self.init_ui()  # Call the init_ui method to initialize the user interface

    # Method to initialize the user interface
    def init_ui(self):
        layout = QVBoxLayout()  # Create a vertical layout for the widgets

        # Create a label to prompt the user for input
        label = QLabel("Enter Input String:")
        # Create a line edit widget for user input
        self.input_line_edit = QLineEdit()

        # Create a button widget for generating passwords
        self.generate_button = QPushButton("Generate Password")
        # Connect the button's click event to the generate_password method
        self.generate_button.clicked.connect(self.generate_password)

        # Create a button widget for copying generated passwords to clipboard
        self.copy_button = QPushButton("Copy")
        # Connect the button's click event to the copy_to_clipboard method
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        # Create a label to display the "Generated Password" text
        self.password_label = QLabel("Generated Password: ")
        # Create a QLabel to display the actual generated password
        self.password_output = QLabel("")

        # Add the widgets to the layout in the desired order
        layout.addWidget(label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_output)

        # Set the layout of the main widget (PasswordGeneratorApp)
        self.setLayout(layout)

    # Method to generate a password based on user input
    def generate_password(self):
        input_string = (
            self.input_line_edit.text()
        )  # Get the text from the input line edit
        if input_string:
            # Call a function (not shown) to generate a password based on the input string
            password = generate_password(input_string)
            self.password_output.setText(
                password
            )  # Set the generated password text in the QLabel
        else:
            # Show a warning message if no input string is provided
            QMessageBox.warning(self, "Input Error", "Please enter an input string.")

    # Method to copy the generated password to the clipboard
    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()  # Get a reference to the clipboard
        generated_password = self.password_output.text()  # Get the generated password
        clipboard.setText(
            generated_password
        )  # Set the generated password as the clipboard text


# Check if the script is being run as the main program
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create a PyQt application object

    window = (
        PasswordGeneratorApp()
    )  # Create an instance of the PasswordGeneratorApp class
    window.show()  # Display the main window

    sys.exit(
        app.exec_()
    )  # Start the event loop and exit the application when it's done

# Steps to create a simple exe file for windows

# Create a virtual environment (venv) to isolate the project's dependencies.
# Run this command in your terminal or command prompt to create a virtual environment named "venv":
# python -m venv venv

# Activate the virtual environment.
# After creating the virtual environment, activate it using this command:
# On Windows:
# venv\Scripts\activate

# Install the required dependencies into the virtual environment.
# You need to install PyQt5 and PyInstaller in your virtual environment.
# Use this command to install the dependencies:
# pip install PyQt5 pyinstaller

# Generate the standalone executable using PyInstaller.
# This command will package your PyQt5 application script (password_generator_ui.py)
# into a single executable file. It will also include the necessary PyQt5 binaries
# and disable the console window when the executable is run.
# Replace the path to the PyQt5 binaries with the actual path on your system.
# Run this command in your terminal or command prompt:
# pyinstaller --onefile --add-binary "C:\Path\PasscodeGenerator\venv\Lib\site-packages\PyQt5\Qt5\bin\*;\Qt5\bin" --noconsole password_generator_ui.py
