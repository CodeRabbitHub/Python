import argparse
import string
import random
import hashlib


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


def main():
    """
    Main function to generate a deterministic password based on an input string.
    Reads command line arguments and prints the generated password.
    """
    parser = argparse.ArgumentParser(
        description="Generate a deterministic password based on an input string."
    )
    parser.add_argument("-s", "--string", type=str, required=True, help="Input string")
    args = parser.parse_args()

    password = generate_password(args.string)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
