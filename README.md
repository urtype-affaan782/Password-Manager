---

# **Password Manager**

A secure and user-friendly password management tool built with Python. This program encrypts your sensitive data using the `cryptography` library, ensuring that your passwords remain safe. 

## **Features**
- **Encryption**: All passwords are encrypted using AES encryption provided by the `cryptography` library.
- **Add Passwords**: Save account credentials securely.
- **Retrieve Passwords**: Access stored account details easily.
- **List Accounts**: View all accounts stored in the password manager.
- **Delete Passwords**: Remove account credentials when no longer needed.
- **File-Based Storage**: All data is stored locally in an encrypted JSON file.

---

## **Requirements**
- Python 3.7 or above
- `cryptography` library

Install the required library by running:
```bash
pip install cryptography
```

---

## **How to Use**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/password-manager.git
   cd password-manager
   ```

2. **Run the Program**:
   ```bash
   python password_manager.py
   ```

3. **Main Menu Options**:
   - **1. Add a password**: Enter the account name, username, and password to save.
   - **2. Retrieve a password**: Enter the account name to view saved credentials.
   - **3. List all accounts**: View a list of all stored accounts.
   - **4. Delete a password**: Enter the account name to remove its credentials.
   - **5. Exit**: Quit the application.

---

## **File Structure**
- `password_manager.py`: The main script.
- `passwords.json`: The encrypted file where passwords are stored (auto-generated).
- `key.key`: The encryption key file (auto-generated).

---

## **Security Notes**
- **Encryption Key**: The key is stored in the `key.key` file. Do not delete or share this file. Without it, your encrypted data cannot be decrypted.
- **Local Storage**: All data is stored locally, ensuring that your passwords are not shared online.

---

## **Future Enhancements**
- Implement a **Graphical User Interface (GUI)** using Tkinter or PyQt.
- Add a **password generator** to create strong, unique passwords.
- Introduce **multi-user support** for shared systems.
- Enable **cloud backup** with end-to-end encryption.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## **Contributing**
Contributions are welcome! If you'd like to improve this project, fork the repository and submit a pull request. 

---

## **Contact**
For any questions or feedback, please reach out:
- **Name**: Affaan
- **GitHub**: [urtype-affaan782](https://github.com/urtype-affaan782)

Stay secure and happy coding! 😊

---
