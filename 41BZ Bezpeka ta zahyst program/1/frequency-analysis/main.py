import collections


cipher_text = "Игрр Тпхосао ОЛРБЛҐЇ"
frequent_alphabet = "ОАИВНЕТСІРДЛМУПКГБЇЙЗЯЬХЖЧЮШЩЦЄФҐ"
regular_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

"""
code taken from:

https://stackoverflow.com/questions/29797475/python-frequency-analysis
"""


def generate_caesar_key(offset):
    dictionary = {}
    index = 0
    for letter in regular_alphabet:
        if index + offset >= len(regular_alphabet):
            index -= len(regular_alphabet)
        dictionary.update({letter: regular_alphabet[index + offset]})
        index += 1
    return dictionary


def switch_encode(string, key):
    encoded = ""
    for letter in string.lower():
        if letter in key.keys():
            encoded += key[letter]
        else:
            encoded += letter
    return encoded


def switch_decode(string, key):
    key = dict(zip(key.values(), key.keys()))
    decoded = ""
    for letter in string.lower():
        if letter in key.keys():
            decoded += key[letter]
        else:
            decoded += letter
    return decoded


def switch_crack(string):
    key = {}
    frequent_letters = collections.Counter(string).most_common()
    index = 0
    for letter in frequent_letters:
        if letter[0] in regular_alphabet:
            key[frequent_alphabet[index]] = letter[0]
            index += 1
    return key


key = generate_caesar_key(3)
res = switch_decode(cipher_text, key)
print(res)
