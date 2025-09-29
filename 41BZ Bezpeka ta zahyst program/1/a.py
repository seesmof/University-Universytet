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

with ui.card().classes("max-w-2xl mx-auto"):
    text_input = ui.input(label="Input text").classes("w-full").props("outlined")
    key_input = ui.input(label="Key").classes("w-full").props("filled readonly")

    with ui.button_group().classes("w-full"):
        ui.button("Encode")
        ui.button("Decode")
        ui.button("Copy")

ui.run()
