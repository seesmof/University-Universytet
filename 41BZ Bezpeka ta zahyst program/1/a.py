import streamlit as st


def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    """
    Encrypts or decrypts text using the Vigenère cipher.

    :param text: The input string (plaintext or ciphertext).
    :param key: The keyword used for encryption/decryption.
    :param decrypt: If True, performs decryption; otherwise encryption.
    :return: The resulting string.
    """
    result = []
    key = key.lower()
    key_len = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            # Shift amount based on key letter
            shift = ord(key[key_index % key_len]) - ord("a")
            if decrypt:
                shift = -shift

            # Preserve case
            base = ord("A") if char.isupper() else ord("a")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)

            key_index += 1  # Only advance key on letters
        else:
            result.append(char)  # Leave non-letters unchanged

    return "".join(result)


st.title("🔐 Vigenère Cipher Tool")

# Input text
text = st.text_area("Enter text:", height=150)

# Key input (auto-uppercase)
raw_key = st.text_input("Enter key (auto uppercased):", "")
key = raw_key.upper()

# Two buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Encrypt"):
        if text and key:
            st.code(vigenere(text, key))

with col2:
    if st.button("Decrypt"):
        if text and key:
            st.code(vigenere(text, key, decrypt=True))
