import os  # For interacting with the file system (e.g., checking file existence, deleting files)
from cryptography.fernet import Fernet  # For secure symmetric encryption/decryption

# Define the name of the file where the encryption key will be saved
KEY_FILE = "secret.key"

# Function to generate a new encryption key and save it to a file
def generate_and_save_key():
    key = Fernet.generate_key()  # Generate a new secure key
    with open(KEY_FILE, "wb") as f:  # Open the key file in write-binary mode
        f.write(key)  # Write the key to the file
    return key  # Return the generated key

# Function to load the existing key or create a new one if not found
def load_key():
    if not os.path.exists(KEY_FILE):  # If the key file does not exist
        return generate_and_save_key()  # Generate and save a new key
    with open(KEY_FILE, "rb") as f:  # Open the key file in read-binary mode
        return f.read()  # Return the key read from the file

# Function to encrypt a file
def encrypt_file(filename):
    key = load_key()  # Load the encryption key
    cipher = Fernet(key)  # Create a cipher object using the key

    with open(filename, "rb") as f:  # Open the target file in read-binary mode
        data = f.read()  # Read the contents of the file

    encrypted = cipher.encrypt(data)  # Encrypt the file contents

    encrypted_filename = filename + ".arjunrocks"  # Create a new filename by adding ".arjunrocks"
    with open(encrypted_filename, "wb") as f:  # Open a new file to save encrypted data
        f.write(encrypted)  # Write the encrypted data to the new file

    os.remove(filename)  # Delete the original unencrypted file
    print(f"Encrypted and saved as: {encrypted_filename}")  # Notify user of success

# Function to decrypt an encrypted file
def decrypt_file(encrypted_filename):
    key = load_key()  # Load the encryption key
    cipher = Fernet(key)  # Create a cipher object using the key

    with open(encrypted_filename, "rb") as f:  # Open the encrypted file
        encrypted_data = f.read()  # Read the encrypted data

    decrypted = cipher.decrypt(encrypted_data)  # Decrypt the data

    # Remove ".myext" from filename to restore original name
    if encrypted_filename.endswith(".arjunrocks"):  # Check if file ends with ".arjunrocks"
        original_filename = encrypted_filename[:-11]  # Remove last 11 characters
    else:
        original_filename = "decrypted_output.txt"  # Default name if not found

    with open(original_filename, "wb") as f:  # Open the file to write decrypted data
        f.write(decrypted)  # Write decrypted content to file

    print(f"Decrypted and saved as: {original_filename}")  # Notify user of success

# --------------- Main Program Flow ---------------

# Prompt the user to choose between encryption or decryption
print("Choose an option:")
print("1. Encrypt a file")
print("2. Decrypt a file")
choice = input("Enter 1 or 2: ")  # Read user input

# If user chooses to encrypt
if choice == "1":
    filename = input("Enter the filename to encrypt: ")  # Ask for file to encrypt
    encrypt_file(filename)  # Call the encryption function

# If user chooses to decrypt
elif choice == "2":
    filename = input("Enter the filename to decrypt (with .myext): ")  # Ask for file to decrypt
    decrypt_file(filename)  # Call the decryption function

# If user enters anything else
else:
    print("Invalid choice.")  # Notify of invalid input
