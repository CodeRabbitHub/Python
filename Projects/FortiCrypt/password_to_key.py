import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass


def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # Adjust the number of iterations as needed
        salt=salt,
        length=256,  # Length of the derived key in bytes
    )
    key = kdf.derive(password.encode())
    return key


def save_key_to_file(username, salt, key):
    with open(f"{username}_key.bin", "wb") as file:
        file.write(salt)
        file.write(key)


def load_key_from_file(username):
    with open(f"{username}_key.bin", "rb") as file:
        salt = file.read(16)  # Read the first 16 bytes for the salt
        key = file.read(256)  # Read the next 32 bytes for the key
    return salt, key


def main():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    salt = os.urandom(16)  # Generate a random salt
    key = derive_key_from_password(password, salt)
    print(key)
    save_key_to_file(username, salt, key)
    print("Key saved to file.")
    salt, key = load_key_from_file(username)
    print(key)

    # Now you would use the username and key file for decryption


if __name__ == "__main__":
    main()
