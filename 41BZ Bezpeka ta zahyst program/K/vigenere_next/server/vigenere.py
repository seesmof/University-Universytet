from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
ASCII_LENGTH = 128


class Mode:
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


@app.route("/encrypt/")
def encrypt():
    query = request.args.to_dict()
    result = vigenere(query["text"], query["key"], Mode.ENCRYPT)
    return result


@app.route("/decrypt/")
def decrypt():
    query = request.args.to_dict()
    result = vigenere(query["text"], query["key"], Mode.DECRYPT)
    return result


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=501000, debug=True)
