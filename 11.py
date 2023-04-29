# Define a secret key
key = b'mysecretkey'

# Define the plaintext message to be encrypted
message = b'This is my secret message.'

# Convert the key and message to binary arrays
key = bytearray(key)
message = bytearray(message)

# Generate the keystream by repeating the key
keystream = bytearray()
while len(keystream) < len(message):
    keystream += key

# Truncate the keystream to the length of the message
keystream = keystream[:len(message)]

# Encrypt the message by XORing it with the keystream
ciphertext = bytearray()
for i in range(len(message)):
    ciphertext.append(message[i] ^ keystream[i])

# Print the encrypted message
print(ciphertext)

# Decrypt the message by XORing it with the keystream again
decrypted_message = bytearray()
for i in range(len(ciphertext)):
    decrypted_message.append(ciphertext[i] ^ keystream[i])

# Print the decrypted message
print(decrypted_message)
