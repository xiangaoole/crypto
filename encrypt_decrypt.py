from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass

def get_key_from_password(password: str, salt: bytes = b'salt_') -> bytes:
    """Derive encryption key from password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt(message: str, password: str) -> str:
    """Encrypt a message using a password"""
    key = get_key_from_password(password)
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return base64.urlsafe_b64encode(encrypted).decode()

def decrypt(encrypted_message: str, password: str) -> str:
    """Decrypt a message using a password"""
    key = get_key_from_password(password)
    f = Fernet(key)
    decrypted = f.decrypt(base64.urlsafe_b64decode(encrypted_message))
    return decrypted.decode()

def main():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '3':
            break

        if choice == '1':
            message = input("Enter message to encrypt: ")
            password = getpass.getpass("Enter password: ")
            try:
                encrypted = encrypt(message, password)
                print(f"\nEncrypted message: {encrypted}")
            except Exception as e:
                print(f"Encryption error: {e}")

        elif choice == '2':
            encrypted_message = input("Enter encrypted message: ")
            password = getpass.getpass("Enter password: ")
            try:
                decrypted = decrypt(encrypted_message, password)
                print(f"\nDecrypted message: {decrypted}")
            except Exception as e:
                print(f"Decryption error: {e}")

if __name__ == "__main__":
    main() 