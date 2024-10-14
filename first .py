import rsa
import os

def generate_keys():
    # Generate a new RSA key pair
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def encrypt(message, public_key):
    # Encrypt the message using the public key
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    # Decrypt the encrypted message using the private key
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message

# Example usage:
public_key, private_key = generate_keys()

message = "Hello, World!"
print("Original Message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message.hex())

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)