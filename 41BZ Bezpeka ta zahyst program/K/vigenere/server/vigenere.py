from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/encrypt/")
def encrypt():
    query = request.args.to_dict()
    result = vigenere_process(query["text"], query["key"], decrypt=False)
    return result


@app.route("/decrypt/")
def decrypt():
    query = request.args.to_dict()
    result = vigenere_process(query["text"], query["key"], decrypt=True)
    return result


def vigenere_process(text: str, key: str, decrypt: bool = False) -> str:
    """
    Encodes or decodes text using the Vigenère cipher.
    Preserves case and ignores non-alphabetic characters in the text.
    Ignores non-alphabetic characters in the key.
    """
    if not text:
        return ""

    clean_key = [k.upper() for k in key if k.isalpha()]

    if not clean_key:
        return text

    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(clean_key[key_index % len(clean_key)]) - ord("A")

            if decrypt:
                shift = -shift

            base = ord("A") if char.isupper() else ord("a")

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)

            key_index += 1
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=501000, debug=True)
