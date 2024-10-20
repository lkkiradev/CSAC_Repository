import random as r
import math as m

def randomize_number(min,max):
    return r.randint(min,max)

min_base = 1
max_base = 32
random_number = randomize_number(min_base,max_base)

def encrypt_half(message, is_first_half):
    encrypted_keys = []
    keys = []
    
    n = len(message)
    for i in range(n):
       
        shift_temp = 6 + i 
        if shift_temp % 2 == 0: 
            if is_first_half:
                shift = shift_temp + (i + (i ** 2))
            else:
                shift = shift_temp + 2 * (i + (i ** 2))
        else: 
            if is_first_half:
                shift = shift_temp + (i + (i ** 3))
            else:
                shift = shift_temp + 2 * (i + (i ** 3))
    
        ascii_value = (ord(message[i]) + shift) - int(m.log(shift))
       
        while ascii_value > 126:
            ascii_value = 31 + (ascii_value - 126)
        
        print(f"[Encrypt] Char: {message[i]}, Shift: {shift}, Encrypted ASCII: {ascii_value}")  # for tracking
   
        encrypted_keys.append(ascii_value)
        keys.append(ord(message[i]))

    return keys, encrypted_keys

def decrypt_half(encrypted_keys, is_first_half):
    decrypted_message = ""
    
    n = len(encrypted_keys)
    for i in range(n):
        shift_temp = 6 + i
        if shift_temp % 2 == 0: 
            if is_first_half:
                shift = shift_temp + (i + (i ** 2))
            else:
                shift = shift_temp + 2 * (i + (i ** 2))
        else:  
            if is_first_half:
                shift = shift_temp + (i + (i ** 3))
            else:
                shift = shift_temp + 2 * (i + (i ** 3))

        ascii_value = (encrypted_keys[i] - shift) + int(m.log(shift))
        
        while ascii_value < 32:
            ascii_value = 126 - (31 - ascii_value)

        decrypted_message += chr(ascii_value)

    return decrypted_message

def main():
    while True:
        action = input("Would you like to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if action == 'e':

            while True:
                message = input("Enter the message to encrypt: ")
                if len(message) <= 20:

                    midpoint = len(message) // 2
                    
                    first_half = message[:midpoint]
                    second_half = message[midpoint:]

                    keys1, encrypted_keys1 = encrypt_half(first_half, is_first_half=True)
                    keys2, encrypted_keys2 = encrypt_half(second_half, is_first_half=False)

                    final_keys = keys1 + keys2
                    final_encrypted_keys = encrypted_keys1 + encrypted_keys2
                    ciphered_text = ''.join(chr(key) for key in final_encrypted_keys)

                    print("Original message:", message)
                    print("Keys (ASCII):", final_keys)
                    print("Encrypted keys:", final_encrypted_keys)
                    print("Ciphered text:", ciphered_text)
                    print("Random number:", 6)
                    break
                else:
                    print("ERROR: Limit reached. Shorten your message to 20 characters.")

        elif action == 'd':

            while True:
                encrypted_message = input("Enter the ciphered text to decrypt: ")

                if len(encrypted_message) <= 20:
                    encrypted_keys = [ord(char) for char in encrypted_message]

                    midpoint = len(encrypted_keys) // 2
                    
                    first_half_encrypted = encrypted_keys[:midpoint]
                    second_half_encrypted = encrypted_keys[midpoint:]

                    decrypted_first_half = decrypt_half(first_half_encrypted, is_first_half=True)
                    decrypted_second_half = decrypt_half(second_half_encrypted, is_first_half=False)

                    decrypted_message = decrypted_first_half + decrypted_second_half
                    print("Decrypted message:", decrypted_message)
                    break
                else:
                    print("ERROR: Limit reached. Shorten your message to 20 characters.")

        elif action == 'q':
            print("Aww :((")
            break
        else:
            print("ERROR: Invalid input, please choose 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
