ASCII_LENGTH = 128


class Mode:
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


def vigenere(message: str, key: str, mode: str = "encrypt") -> str:
    # Make key as long as the message is
    key_stream = key * len(message)
    # Truncate it, so that it does not exceed the message length
    long_key = key_stream[: len(message)]

    result: str = str()
    for index, _ in enumerate(message):
        key_ascii = ord(long_key[index])
        message_ascii = ord(message[index])

        letter_ascii = 0
        if mode == Mode.ENCRYPT:
            letter_ascii = (message_ascii + key_ascii) % ASCII_LENGTH
        elif mode == Mode.DECRYPT:
            letter_ascii = (message_ascii - key_ascii) % ASCII_LENGTH
        else:
            raise ValueError("Invalid mode...")

        new_letter = chr(letter_ascii)
        result += new_letter

    return result


key = "G0D"
encrypted = vigenere("This, some message!", key, Mode.ENCRYPT)
decrypted = vigenere(encrypted, key, Mode.DECRYPT)
print(encrypted)
print(decrypted)
