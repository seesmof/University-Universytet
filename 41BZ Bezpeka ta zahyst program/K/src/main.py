from nicegui import ui


def vigenere_process(text: str, key: str, decrypt: bool = False) -> str:
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


def main():
    ui.colors(
        primary="#5898d4", secondary="#26a69a", accent="#9c27b0", positive="#21ba45"
    )

    with ui.column().classes(
        "w-full h-[97vh] items-center justify-center bg-sky-50 dark:bg-slate-900 rounded-md"
    ):
        with ui.card().classes("w-full max-w-lg p-6 shadow-xl rounded-xl"):
            with ui.row().classes("w-full justify-center mb-4"):
                ui.icon("lock", size="3em", color="primary")
            ui.label("Vigenère Cipher").classes(
                "text-2xl font-bold text-center w-full mb-6 text-gray-700 dark:text-gray-200"
            )

            input_text = (
                ui.textarea(
                    label="Input Message",
                    placeholder="Type your secret message here...",
                )
                .classes("w-full mb-2")
                .props("outlined rounded auto-grow")
            )

            key_input = (
                ui.input(label="Secret Key", placeholder="e.g. LEMON")
                .classes("w-full mb-6")
                .props("outlined rounded")
            )

            with ui.row().classes("w-full justify-between gap-4 mb-6"):

                def run_encryption():
                    res = vigenere_process(
                        input_text.value, key_input.value, decrypt=False
                    )
                    output_text.value = res
                    ui.notify("Message Encrypted!", type="positive")

                def run_decryption():
                    res = vigenere_process(
                        input_text.value, key_input.value, decrypt=True
                    )
                    output_text.value = res
                    ui.notify("Message Decrypted!", type="info")

                ui.button(
                    "Encrypt", icon="enhanced_encryption", on_click=run_encryption
                ).classes("flex-1")
                ui.button(
                    "Decrypt", icon="no_encryption", on_click=run_decryption
                ).classes("flex-1 bg-secondary")

            ui.separator()
            ui.label("Result").classes("text-sm text-gray-500 mt-4 mb-1")

            output_text = (
                ui.textarea(placeholder="Result will appear here")
                .classes("w-full")
                .props("outlined rounded readonly bg-gray-50 dark:bg-slate-800")
            )

            with ui.row().classes("w-full justify-end mt-2"):

                async def copy_to_clipboard():
                    if output_text.value:
                        await ui.clipboard.write(output_text.value)
                        ui.notify("Copied to clipboard!", icon="content_copy")
                    else:
                        ui.notify("Nothing to copy", type="warning")

                ui.button(
                    "Copy Result", icon="content_copy", on_click=copy_to_clipboard
                ).props("flat dense size=sm")

    ui.run(title="Vigenère Tool", favicon="🔐")


if __name__ in {"__main__", "__mp_main__"}:
    main()
