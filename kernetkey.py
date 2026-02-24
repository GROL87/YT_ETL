from cryptography.fernet import Fernet

# Generate and print a new key
key = Fernet.generate_key()
print(key.decode())  # Decode to string for easy copying
