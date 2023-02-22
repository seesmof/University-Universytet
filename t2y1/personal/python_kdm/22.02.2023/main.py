import random


def generate_random_number(minRange, maxRange):
    return random.randint(minRange, maxRange)


def main():
    print('Enter a range to generate in, separated by spaces')
    range = input('Enter: ')
    range = range.split(' ')
    rangeMin = int(range[0])
    rangeMax = int(range[1])
    print(f"Your number is {generate_random_number(rangeMin, rangeMax)}!")
    if 10 > rangeMin:
        print(f"Your number is {generate_random_number(rangeMin, rangeMax)}!")


if __name__ == '__main__':
    main()
