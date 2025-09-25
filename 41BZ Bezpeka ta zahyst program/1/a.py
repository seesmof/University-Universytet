import string


get_letter = dict(enumerate(string.ascii_uppercase, 1))
get_number = dict(reversed(item) for item in get_letter.items())
print(get_number)

key: int = 3
input_text = "Some unimportant stuff"


def transform_text(given_text: str):
    return given_text.upper().replace(" ", "")


transformed_text = transform_text(input_text)
result: str = str()
for letter in transformed_text:
    new_number = get_number[letter] + key
    new_letter = get_letter[new_number]
    result += new_letter
print(transformed_text)
print(result)

key = "some"
length = 17
keystream: str = str()
iterator: int = 0
while length > 0:
    keystream += key[iterator]

    length -= 1
    iterator = (iterator + 1) % len(key)
print(keystream)
