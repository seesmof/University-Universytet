import re
from nicegui import ui


class Alphabet:
    ENG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UKR = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


def vigenere(text: str, key: str, alphabet: Alphabet, to_decode: bool = False) -> str:
    if not text or not key:
        return ""

    num_to_letter = dict(enumerate(alphabet))
    letter_to_num = dict(reversed(pair) for pair in num_to_letter.items())

    # Заміняє всі символи, яких немає в алфавіті
    non_letters_pattern = rf"[^{alphabet.upper()}{alphabet.lower()}]"
    clean_key = re.sub(non_letters_pattern, "", key).upper()

    resulting_string: str = str()
    key_index: int = 0

    for letter in text:
        if letter.upper() in letter_to_num:
            key_letter = clean_key[key_index % len(clean_key)]

            key_number = letter_to_num.get(key_letter)
            letter_number = letter_to_num.get(letter.upper())

            if not to_decode:
                new_number = (letter_number + key_number) % len(alphabet)
            else:
                new_number = (letter_number - key_number) % len(alphabet)

            new_letter = num_to_letter.get(new_number)
            new_letter = new_letter if letter == letter.upper() else new_letter.lower()

            resulting_string += new_letter
        else:
            resulting_string += letter
        key_index += 1

    return resulting_string


class Lang:
    ENG = "English"
    UKR = "Українська"


def render_ui(lang: Lang) -> None:
    is_english: bool = lang == Lang.ENG

    text_input = (
        ui.input(label="📃 " + ("Input text" if is_english else "Текст для кодування"))
        .classes("w-full")
        .props("outlined clearable")
    )
    key_input = (
        ui.input(label="🧷 " + ("Key" if is_english else "Ключ"))
        .classes("w-full")
        .props("outlined clearable")
    )
    with ui.input(
        label="⌨️ " + ("Encoded text" if is_english else "Шифротекст")
    ).classes("w-full").props("filled readonly") as result_output:
        result_copy_button = ui.button(
            icon="o_copy",
            on_click=lambda: ui.clipboard.write(result_output.value),
        ).props("dense flat")

    def process_text(to_decode: bool = False):
        resulting_string: str = vigenere(
            text_input.value,
            key_input.value,
            alphabet=Alphabet.ENG if is_english else Alphabet.UKR,
            to_decode=True if to_decode else False,
        )
        result_output.value = resulting_string

    with ui.button_group().classes("w-full"):
        encode_button = (
            ui.button(
                "Encode" if is_english else "Кодувати",
                color="lime-500",
                on_click=lambda: process_text(True),
            )
            .props("text-color=white")
            .classes("w-full")
        )
        decode_button = (
            ui.button(
                "Decode" if is_english else "Декодувати",
                color="sky-400",
                on_click=lambda: process_text(False),
            )
            .props("text-color=white")
            .classes("w-full")
        )


with ui.card().classes("max-w-2xl mx-auto mt-[20vh]"):
    with ui.tabs().classes("w-full") as tabs:
        eng_tab = ui.tab(Lang.ENG)
        ukr_tab = ui.tab(Lang.UKR)

    with ui.tab_panels(tabs, value=eng_tab).classes("w-full"):
        with ui.tab_panel(Lang.ENG):
            render_ui(lang=Lang.ENG)
        with ui.tab_panel(Lang.UKR):
            render_ui(lang=Lang.UKR)

if __name__ == "__main__":
    ui.run(title="Шифр Віженера", favicon="🔐")
