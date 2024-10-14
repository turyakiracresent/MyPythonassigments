
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key(password):
    return get_random_bytes(32)  # Generate 256-bit key

def encrypt_message(message, password):
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return cipher.nonce + tag + ciphertext

def decrypt_message(ciphertext, password):
   

