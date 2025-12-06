ASCII_LENGTH = 128

message = "This, it is glorious!"
key = "G0D"

# Make key as long as the message is
key_stream = key * len(message)
# Truncate it, so that it does not exceed message length
long_key = key_stream[: len(message)]

cipher_text: str = str()
for index, message_char in enumerate(message):
    key_ascii_value = ord(long_key[index])
    message_ascii_value = ord(message[index])

    new_letter_ascii = (message_ascii_value + key_ascii_value) % ASCII_LENGTH
    new_letter = chr(new_letter_ascii)
    cipher_text += new_letter

deciphered_text: str = str()
for index, cipher_letter in enumerate(cipher_text):
    key_ascii_value = ord(long_key[index])
    cipher_ascii_value = ord(cipher_text[index])

    original_letter_ascii = (cipher_ascii_value - key_ascii_value) % ASCII_LENGTH
    original_letter = chr(original_letter_ascii)
    deciphered_text += original_letter
