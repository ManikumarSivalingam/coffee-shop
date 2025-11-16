from password_utils import encrypt_password
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("db_mask/secret.key", "wb") as key_file:
        key_file.write(key)
        print("Encryption key generated and saved to secret.key")


if __name__ == "__main__":
    generate_key()
    encrypted_password = encrypt_password("manikumar")
    encrypted_password = encrypt_password(input("Enter password to encrypt: "))
    with open("db_mask/encrypt.key", "wb") as enc_file:
        enc_file.write(encrypted_password)
    print("Encrypted Password:", encrypted_password)