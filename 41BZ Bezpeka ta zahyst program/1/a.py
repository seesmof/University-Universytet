import os
import streamlit as st
from nicegui import ui


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


# --- NiceGUI Interface ---
with ui.card().classes("w-2/3 mx-auto mt-10 p-6"):
    ui.label("🔐 Vigenère Cipher Tool").classes("text-2xl font-bold mb-4")

    text_area = ui.textarea("Enter text").props("outlined").classes("w-full h-40")

    # Key input with auto-uppercase
    key_input = ui.input("Enter key").props("outlined").classes("w-full")
    key_input.on("input", lambda e: key_input.set_value(e.value.upper()))

    result_area = (
        ui.textarea("Result").props("outlined readonly").classes("w-full h-40")
    )

    with ui.row().classes("justify-between w-full mt-4"):
        with ui.row():
            ui.button(
                "Encrypt",
                on_click=lambda: result_area.set_value(
                    vigenere(text_area.value, key_input.value, decrypt=False)
                ),
            )
            ui.button(
                "Decrypt",
                on_click=lambda: result_area.set_value(
                    vigenere(text_area.value, key_input.value, decrypt=True)
                ),
            )
        ui.button("Copy", on_click=lambda: os.system(f"echo {result_area.value}| clip"))

ui.run()
