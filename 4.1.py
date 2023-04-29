# Define the Vigenère cipher function
def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_index = 0
    for letter in plaintext:
        if letter.isalpha():
            # Convert the letter to its alphabetical index (A=0, B=1, etc.)
            letter_index = ord(letter.upper()) - ord('A')
            
            # Convert the key letter to its alphabetical index
            key_letter = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_letter_index = ord(key_letter.upper()) - ord('A')
            
            # Add the letter and key letter indices, and take the result mod 26
            cipher_index = (letter_index + key_letter_index) % 26
            
            # Convert the cipher index back to a letter and append it to the ciphertext
            cipher_letter = chr(cipher_index + ord('A'))
            ciphertext += cipher_letter
        else:
            # If the character isn't a letter, just append it to the ciphertext
            ciphertext += letter
    return ciphertext


# Test the function
plaintext = "HELLO WORLD"
key = "KEY"
ciphertext = vigenere_cipher(plaintext, key)
print("Ciphertext:-",ciphertext)


# Define the Vigenère cipher decryption function
def vigenere_decipher(ciphertext, key):
    plaintext = ""
    key_index = 0
    for letter in ciphertext:
        if letter.isalpha():
            # Convert the letter to its alphabetical index (A=0, B=1, etc.)
            letter_index = ord(letter.upper()) - ord('A')
            
            # Convert the key letter to its alphabetical index
            key_letter = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_letter_index = ord(key_letter.upper()) - ord('A')
            
            # Subtract the key letter index from the cipher index, and take the result mod 26
            cipher_index = (letter_index - key_letter_index) % 26
            
            # Convert the cipher index back to a letter and append it to the plaintext
            plain_letter = chr(cipher_index + ord('A'))
            plaintext += plain_letter
        else:
            # If the character isn't a letter, just append it to the plaintext
            plaintext += letter
    return plaintext


# Test the function
ciphertext = "RIJVS UYVJN"
key = "KEY"
plaintext = vigenere_decipher(ciphertext, key)
print("Plaintext:-",plaintext)
