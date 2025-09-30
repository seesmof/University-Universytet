from nicegui import ui

UKRAINIAN = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
ENGLISH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# given_text: str = input("Enter the input text: ")
# key: str = input("Enter the key text: ")
given_text = "be"
key = "god"

get_letter = dict(enumerate(ENGLISH, 1))
get_number = dict(reversed(pair) for pair in get_letter.items())

given_text = given_text.replace(" ", "").upper()
key = (key * len(given_text))[: len(given_text)].upper()

answer: str = str()
for index, letter in enumerate(given_text):
    key_letter = key[index]

    key_letter_number = get_number[key_letter]
    letter_number = get_number[letter]

    new_letter_number = (key_letter_number + letter_number) % len(get_letter.keys())
    new_letter = get_letter[new_letter_number]

    answer += new_letter
print(answer)

decrypted: str = str()
for index, letter in enumerate(answer):
    key_letter = key[index]

    key_letter_number = get_number[key_letter]
    letter_number = get_number[letter]

    new_letter_number = (letter_number - key_letter_number) % len(get_letter.keys())
    new_letter = get_letter[new_letter_number]

    decrypted += new_letter
print(decrypted)


class Lang:
    ENG = "English"
    UKR = "Українська"


def render_ui(lang: Lang) -> None:
    text_input = (
        ui.input(label="Input text" if lang == Lang.ENG else "Текст для кодування")
        .classes("w-full")
        .props("outlined")
    )
    key_input = (
        ui.input(label="Key" if lang == Lang.ENG else "Ключ")
        .classes("w-full")
        .props("filled")
    )
    result_output = ui.code(content="").classes("w-full h-11 pt-1")

    with ui.button_group().classes("w-full"):
        encode_button = (
            ui.button("Encode" if lang == Lang.ENG else "Кодувати", color="lime-500")
            .props("text-color=white")
            .classes("w-full")
        )
        decode_button = (
            ui.button("Decode" if lang == Lang.ENG else "Декодувати", color="sky-400")
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

ui.run()
