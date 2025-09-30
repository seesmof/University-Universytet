from collections import Counter
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(current_dir, "text.md")
    with open(text_file, encoding="utf-8", mode="r") as f:
        text = f.read().strip().replace("\n", " ")

    letters = [char.upper() for char in text if char.isalpha() and char != "ʼ"]
    most_common_letters = [letter for letter, number in Counter(letters).most_common()]
    result = "".join(most_common_letters)
    print(result)


if __name__ == "__main__":
    main()
