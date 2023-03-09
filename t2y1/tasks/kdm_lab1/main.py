import random


def main():
    # output menu to user
    print("Як би ви хотіли отримати множини?")
    print("1. Ввести самостійно")
    print("2. Згенерувати випадкові")
    # ask user to choose an option
    userDecision = int(input("Вибір: "))
    # ask user to enter number of
    numberOfElements = int(
        input(f"\nВведіть кількість елементів в множинах: "))
    print("")

    # declare sets for future filling in
    setA = set()
    setB = set()
    # if user chose to generate nubmers randomly
    if userDecision == 2:
        # execute twitce
        for setNumber in range(2):
            # for all items
            for itemNumber in range(numberOfElements):
                # generate random item
                elementHolder = random.randint(10, 100)
                # add item to a corresponding set
                if setNumber == 0:
                    setA.add(elementHolder)
                elif setNumber == 1:
                    setB.add(elementHolder)
    # if user chose to enter numbers individually
    elif userDecision == 1:
        # execute twice
        for setNumber in range(2):
            # for all items
            for itemNumber in range(numberOfElements):
                # ask user to enter an item manually
                elementHolder = int(
                    input(f"{setNumber+1}.{itemNumber+1}. Введіть: "))
                # add item to a corresponding set
                if setNumber == 0:
                    setA.add(elementHolder)
                elif setNumber == 1:
                    setB.add(elementHolder)
            print("")

    # output input sets to user
    print(f"A: {setA}")
    print(f"B: {setB}")

    # create a sets for holding result pairs
    outputPairs = set()
    # for each combination of two items
    for a in setA:
        for b in setB:
            # check if the formula applies
            if (2*a - b) % 3 == 0:
                # add pair to a results set
                outputPairs.add((a, b))

    # print out results
    print(f"\nРезультат: {outputPairs}")


# execute main function
if __name__ == '__main__':
    print("")
    main()
    print("")
