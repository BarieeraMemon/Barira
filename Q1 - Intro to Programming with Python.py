#Q1: The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

import string

def caesar_cipher(message, key, mode):
    result = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65) if mode == 'e' else chr((ord(char) - 65 - shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97) if mode == 'e' else chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("The Caesar Cipher Program")
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    mode = input("> ").lower()

    if mode not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        return

    key = int(input("Please enter the key (0 to 25) to use.\n> "))

    if not 0 <= key <= 25:
        print("Invalid key. Exiting.")
        return

    message = input("Enter the message to {}.\n> ".format("encrypt" if mode == 'e' else "decrypt"))

    result = caesar_cipher(message, key, mode)

    print("Result:")
    print(result)

if __name__ == "__main__":
    main()
