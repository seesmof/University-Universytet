import pprint
import string


letters_data = dict(enumerate(string.ascii_uppercase, 1))
numbers_data = dict(reversed(item) for item in letters_data.items())
print(numbers_data)

key: int = 3
input_text = "Some unimportant stuff"


def transform_text(given_text: str):
    return given_text.upper().replace(" ", "")


transformed_text = transform_text(input_text)
result: str = str()
for letter in transformed_text:
    new_number = numbers_data[letter] + key
    new_letter = letters_data[new_number]
    result += new_letter
print(transformed_text)
print(result)
