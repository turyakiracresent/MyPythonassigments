def encrypt_message(plain_text, shift):
    encrypted_text = []
    for char in plain_text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(encrypted_text)

def decrypt_message(encrypted_text, shift):
    return encrypt_message(encrypted_text, -shift)  # Decrypting is just encrypting with a negative shift

def main():
    print("Welcome to the Caesar Cipher Program!")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    
    if choice not in ('E', 'D'):
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    if choice == 'E':
        result = encrypt_message(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt_message(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
