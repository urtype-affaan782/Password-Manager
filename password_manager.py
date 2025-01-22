import os
import base64
from cryptography.fernet import Fernet
import json

# Constants
DATA_FILE = "passwords.json"
KEY_FILE = "key.key"

# Generate or load the encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return key

# Initialize encryption
key = load_key()
cipher_suite = Fernet(key)

# Load passwords from file
def load_passwords():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        encrypted_data = file.read()
        if encrypted_data:
            decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
            return json.loads(decrypted_data)
    return {}

# Save passwords to file
def save_passwords(passwords):
    encrypted_data = cipher_suite.encrypt(json.dumps(passwords).encode()).decode()
    with open(DATA_FILE, 'w') as file:
        file.write(encrypted_data)

# Add a new password
def add_password(account, username, password):
    passwords = load_passwords()
    passwords[account] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"Password for account '{account}' added successfully!")

# Retrieve a password
def get_password(account):
    passwords = load_passwords()
    if account in passwords:
        account_data = passwords[account]
        print(f"Account: {account}\nUsername: {account_data['username']}\nPassword: {account_data['password']}")
    else:
        print(f"No password found for account '{account}'.")

# List all accounts
def list_accounts():
    passwords = load_passwords()
    if passwords:
        print("Accounts saved:")
        for account in passwords.keys():
            print(f" - {account}")
    else:
        print("No accounts saved.")

# Delete a password
def delete_password(account):
    passwords = load_passwords()
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print(f"Password for account '{account}' deleted successfully!")
    else:
        print(f"No password found for account '{account}'.")

# Main menu
def main():
    while True:
        print("\n=== Password Manager ===")
        print("By: Affaan Nadeem")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. List all accounts")
        print("4. Delete a password")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            account = input("Enter account name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(account, username, password)
        elif choice == "2":
            account = input("Enter account name to retrieve: ")
            get_password(account)
        elif choice == "3":
            list_accounts()
        elif choice == "4":
            account = input("Enter account name to delete: ")
            delete_password(account)
        elif choice == "5":
            print("Exiting Password Manager. Stay secure!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
