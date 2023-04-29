def caesar_cipher(message, key):
    """
    Applies the Caesar cipher substitution operation to the given message with the given key.
    """
    cipher_text = ""

    # Iterate over each character in the message.
    for char in message:
        # Check if the character is a letter.
        if char.isalpha():
            # Shift the character by the key amount.
            shifted_char = chr((ord(char.lower()) - 97 + key) % 26 + 97)

            # Preserve the case of the original character.
            if char.isupper():
                cipher_text += shifted_char.upper()
            else:
                cipher_text += shifted_char
        else:
            # Preserve non-letter characters as-is.
            cipher_text += char

    return cipher_text

message = "hello duniya"
key = 3
cipher_text = caesar_cipher(message, key)

print("Original message:", message)
print("Cipher text:", cipher_text)

print("............Decryption..........")
cipher_text = "Khoor gxqlbd"
shift = 3

plain_text = caesar_cipher(cipher_text, -shift)
print("Plain Text:", plain_text)
