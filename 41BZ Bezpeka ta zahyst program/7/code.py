def plus(text: str, other: str) -> str:
    return text + ", and also: " + other


def main():
    some_text = "Jesus is LORD"
    other_text = "Worship Him only"

    result: str = plus(some_text, other_text)
    print(result)


if __name__ == "__main__":
    main()
