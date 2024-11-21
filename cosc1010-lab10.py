# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

from hashlib import sha256

def get_hash(to_hash):
    """Generate a SHA-256 hash of the given string."""
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

def crack_password():
    # Read the hash to crack
    try:
        with open("hash", "r") as hash_file:
            stored_hash = hash_file.read().strip()
    except:
        print("Error: Could not open the 'hash' file.")
        return

    # Open the password file
    try:
        with open("rockyou.txt", "r", encoding="utf-8") as passwords_file:
            for password in passwords_file:
                password = password.strip()  # Remove extra spaces or newlines
                if get_hash(password) == stored_hash:
                    print(f"Password found: {password}")
                    return
    except:
        print("Error: Could not open the 'rockyou.txt' file.")
        return

    print("Password not found.")

if __name__ == "__main__":
    crack_password()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
