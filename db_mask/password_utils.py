from cryptography.fernet import Fernet   

class CustomFernet(str):
    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()
    def __bytes__(self):
        return super().__bytes__()

def load_key():
    """Loads the encryption key from the secret.key file."""
    return open("db_mask/secret.key", "rb").read()


def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())


def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode())
    return CustomFernet(decrypted_password.decode())

def get_decrypt_password():
    with open("db_mask/encrypt.key", "rb") as file:
        encrypted_password = file.read().strip()
    return decrypt_password(encrypted_password)