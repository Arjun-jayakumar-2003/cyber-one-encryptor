# 🔐 CyberOne Encryptor

Welcome to **CyberOne** — **Month One** of my Cybersecurity learning journey!

This project is a simple Python-based utility that lets you **encrypt and decrypt files** using symmetric key encryption with the `cryptography` library.

## 🧠 What It Does

- ✅ Generates a secret key on the first run and saves it securely as `secret.key`
- ✅ Encrypts any file you specify and deletes the original
- ✅ Decrypts the encrypted file back to its original form

## 🚀 How to Use

Run the program:

```bash
python file_lock.py
```

Then follow the prompts:

```bash
Choose an option:
1. Encrypt a file
2. Decrypt a file
Enter 1 or 2: 1
Enter the filename to encrypt: yourfile.txt
Encrypted and saved as: yourfile.txt.arjunrocks
```

## 📂 Files

| File           | Description                                  |
|----------------|----------------------------------------------|
| `file_lock.py` | Main Python script with encryption logic     |
| `README.md`    | Project documentation                        |

## 🔐 Notes

- The first time you run the program, it will **generate and save** a `secret.key` file, which is used for encryption and decryption.
- The original file is **deleted** after encryption for better security.
- Keep your `secret.key` file **safe and private** — without it, you cannot decrypt your files.
- Encrypted files are saved with a `.arjunrocks` extension (you can change it).

Stay tuned for more projects in **CyberOne** as I continue exploring the world of cybersecurity with hands-on Python projects! 🧑‍💻
