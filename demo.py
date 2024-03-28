import string
import random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES, DES3
import math
import secrets

def shift_cipher_encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                encrypted_message += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            encrypted_message += char
    return encrypted_message

def shift_cipher_decrypt(message, shift):
    return shift_cipher_encrypt(message, -shift)

def generate_key():
    alphabet = string.ascii_letters
    key = list(alphabet)
    random.shuffle(key)
    print("Key: ",''.join(key))
    return ''.join(key)

def permutation_cipher_encrypt(message, key):
    ciphertext = ''
    for char in message:
        if char in string.ascii_letters:
            index = string.ascii_letters.index(char)
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def permutation_cipher_decrypt(message, key):
    plaintext = ''
    for char in message:
        if char in key:
            index = key.index(char)
            plaintext += string.ascii_letters[index]
        else:
            plaintext += char
    return plaintext


def simple_transposition_encrypt(message,key):
     # Simulates columns in the matrix by using string array.
    ciphertext = [''] * key
    # Iterates through each column in the ciphertext.
    for column in range(key):
        index = column
        # Iterates until the plaintext end.
        while index < len(message):
            # Places the character at the end of the column:
            ciphertext[column] += message[index]
            # Moves the index to the next symbol.
            index += key
    # Returns the ciphertext array as a single string.
    return ''.join(ciphertext)

def simple_transposition_decrypt(message,key):
    nrows = key
    ncols = math.ceil(len(message) / key)
    empty_positions = nrows * ncols - len(message)
    plaintext = [''] * ncols
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if column == ncols or (column == ncols - 1 and row >= nrows - empty_positions):
            column = 0
            row += 1
    return ''.join(plaintext)

def double_transposition_encrypt(message,key):
    return simple_transposition_encrypt(simple_transposition_encrypt(message,key),key)

def double_transposition_decrypt(message,key):
    return simple_transposition_decrypt(simple_transposition_decrypt(message,key),key)

def vigenere_cipher_encrypt(message, key):
    encrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            if char.islower():
                encrypted_message += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                encrypted_message += chr(((ord(char) - 65 + shift) % 26) + 65)
            key_index += 1
        else:
            encrypted_message += char
    return encrypted_message

def vigenere_cipher_decrypt(message, key):
    decrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            if char.islower():
                decrypted_message += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                decrypted_message += chr(((ord(char) - 65 - shift) % 26) + 65)
            key_index += 1
        else:
            decrypted_message += char
    return decrypted_message

def aes_encrypt(message, key):
    key = key.encode()  # Encode the key to bytes
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(pad(message.encode(), AES.block_size)) # Pad message before encryption
    nonce = cipher.nonce
    return ciphertext, tag, nonce

def aes_decrypt(ciphertext, tag, nonce, key):
    key = key.encode()  # Encode the key to bytes
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plain_text = unpad(cipher.decrypt_and_verify(ciphertext, tag), AES.block_size).decode() # Unpad after decryption
    return plain_text


def pad_message(message):
    while len(message) % 8 != 0:
        message += ' '
    return message

def des_encrypt(message, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_message = pad_message(message)
    ciphertext = des.encrypt(padded_message.encode('utf-8'))
    return ciphertext

def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_message = des.decrypt(ciphertext).decode('utf-8')
    return decrypted_message.strip()

def triple_des_encrypt(message, key):
    des3 = DES3.new(key, DES3.MODE_ECB)
    padded_message = pad_message(message)
    ciphertext = des3.encrypt(padded_message.encode('utf-8'))
    return ciphertext

def triple_des_decrypt(ciphertext, key):
    des3 = DES3.new(key, DES3.MODE_ECB)
    decrypted_message = des3.decrypt(ciphertext).decode('utf-8')
    return decrypted_message.strip()

def main():
    print("Encryption Techniques:")
    print("1. Substitution cipher")
    print(" - Shift Cipher")
    print(" - Permutation Cipher")
    print("2. Transposition ciphers")
    print(" - Simple Transposition")
    print(" - Double Transposition")
    print("3. Vigenere Cipher")
    print("4. AES Encryption")
    print("5. DES Encryption/Decryption")
    print("6. 3DES Encryption/Decryption")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sub_choice = int(input("Enter Substitution Cipher type (1 for Shift Cipher, 2 for Permutation Cipher): "))
        if sub_choice == 1:
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = shift_cipher_encrypt(message, shift)
            print("Encrypted Message:", encrypted_message)
            decrypted_message = shift_cipher_decrypt(encrypted_message, shift)
            print("Decrypted Message:", decrypted_message)
        elif sub_choice == 2:
            choice = input("Would you like to enter a key manually? (y/n): ")
            if choice.lower() == 'y':
                key = input("Enter the key (leave empty for random key generation): ").strip()
                if not key:
                    key = generate_key()
                elif len(key) < 52:
                    print("The key should be at least 52 characters long (the length of the alphabet), generating a random key instead.")
                    key = generate_key()
                elif len(key) > 52:
                    print("The key length exceeds the required length (52 characters). Only the first 52 characters will be considered.")
                    key = key[:52]
            else:
                key = generate_key()

            plaintext = input("Enter the plaintext: ")
            print("Plaintext:", plaintext)

            ciphertext = permutation_cipher_encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)

            decrypted_text = permutation_cipher_decrypt(ciphertext, key)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid choice for Substitution Cipher.")

    elif choice == 2:
        trans_choice = int(input("Enter Transposition Cipher type (1 for Simple Transposition, 2 for Double Transposition): "))
        if trans_choice == 1:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter a key (a number)"))
            encrypted_message = simple_transposition_encrypt(message,key)
            print("Encrypted Message:", encrypted_message)
            decrypted_message = simple_transposition_decrypt(encrypted_message, key)
            print("Decrypted Message:", decrypted_message)
        elif trans_choice == 2:
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter a key (a number)"))
            encrypted_message = double_transposition_encrypt(message,key)
            print("Encrypted Message:", encrypted_message)
            decrypted_message = double_transposition_decrypt(encrypted_message, key)
            print("Decrypted Message:", decrypted_message)
        else:
            print("Invalid choice for Transposition Cipher.")

    elif choice == 3:
        message = input("Enter the message to encrypt: ")
        key = input("Enter the Vigenere Cipher key: ")
        encrypted_message = vigenere_cipher_encrypt(message, key)
        print("Encrypted Message:", encrypted_message)
        decrypted_message = vigenere_cipher_decrypt(encrypted_message, key)
        print("Decrypted Message:", decrypted_message)

    elif choice == 4:
        print("AES Encryption selected:")
        message = input("Enter the message to encrypt: ")
        demo_key = get_random_bytes(16).hex() 
        print("Example: d546e37a49480827554fc72df8a715e5")       
        key = input("Enter the encryption key (16 bytes) Or Enter if you don't want to enter: ").encode()
        print("Default_Key: ",demo_key)       
        if len(key) > 0:
            key=demo_key
        try:
            print("Nothing ?",key)
            ciphertext, tag, nonce = aes_encrypt(message, key)
            print("Encrypted Message:", ciphertext.hex())
            
            decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").lower()
            if decrypt_choice == 'yes':
                decrypted_message = aes_decrypt(ciphertext, tag, nonce, key)
                print("Decrypted Message:", decrypted_message)
        
        except ValueError as e:
            print("Error:", e)
    elif choice == 5:
        print("DES Encryption selected:")
        message = input("Enter the message to encrypt: ")
        demo_key = secrets.token_bytes(8)
        print("Demo Key:", (demo_key.hex())[:8])
        key_input = input("Enter the encryption key (8 bytes) or press Enter to generate a random key: ").strip()
        if key_input:
            key = key_input.encode()
            if len(key) != 8:
                print("Error: The key must be exactly 8 bytes long.")
                return
        else:
            key = demo_key
        try:
            des_ciphertext = des_encrypt(message, key)
            print("Encrypted Message:", des_ciphertext.hex())
            
            decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").lower()
            if decrypt_choice == 'yes':
                des_decrypted = des_decrypt(des_ciphertext, key)
                print("Decrypted Message:", des_decrypted)
        except ValueError as e:
            print("Error:", e)

    elif choice == 6:
        print("3DES Encryption selected:")
        message = input("Enter the message to encrypt: ")
        demo_key = secrets.token_bytes(16)
        print("Demo Key:", (demo_key.hex())[:16])
        key = input("Enter the encryption key (16 or 24 bytes) or press Enter for a random key: ").encode()
        
        if len(key) == 16:
            demo_key = key + key[:8]  # Extend 16-byte key to 24 bytes for Triple DES
        elif len(key) == 24:
            demo_key = key
        else:
            print("Invalid key length. Key must be 16 or 24 bytes long.")
            return

        try:
            des3_ciphertext = triple_des_encrypt(message, demo_key)
            print("Encrypted Message:", des3_ciphertext.hex())
            
            decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").lower()
            if decrypt_choice == 'yes':
                des3decrypted = triple_des_decrypt(des3_ciphertext, demo_key)
                print("Decrypted Message:",des3decrypted)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()  