def placement_without_repetition(n, k):
    result = []
    helper(result, [], n, k)
    print(result)


def helper(result, temp, n, k):
    if len(temp) == k:
        result.append(temp.copy())
    else:
        for i in range(1, n+1):
            if i not in temp:
                temp.append(i)
                helper(result, temp, n, k)
                temp.pop()


def helper(result, temp, n, k):
    if len(temp) == k:
        result.append(temp.copy())
    else:
        for i in range(1, n+1):
            temp.append(i)
            helper(result, temp, n, k)
            temp.pop()


def placement_with_repetition(n, k):
    result = []
    helper(result, [], n, k)
    print(result)


def main():
    print("Select the variant of combinations:")
    print("1. Placement without repetition")
    print("2. Placement with repetition")
    print("3. Combination without repetition")
    print("4. Combination with repetition")
    print("5. Permutations of ordinary elements")
    print("6. Permutations with repetition of elements")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        n = int(input("Enter the value of n: "))
        k = int(input("Enter the value of k: "))
        placement_without_repetition(n, k)
    elif choice == 2:
        n = int(input("Enter the value of n: "))
        k = int(input("Enter the value of k: "))
        placement_with_repetition(n, k)
    elif choice == 3:
        n = int(input("Enter the value of n: "))
        k = int(input("Enter the value of k: "))
        combination_without_repetition(n, k)
    elif choice == 4:
        n = int(input("Enter the value of n: "))
        k = int(input("Enter the value of k: "))
        combination_with_repetition(n, k)
    elif choice == 5:
        n = int(input("Enter the value of n: "))
        permutations_ordinary(n)
    elif choice == 6:
        args = input(
            "Enter the values of n1, n2, ..., nk separated by commas: ")
        args = [int(x) for x in args.split(",")]
        n = sum(args)
        permutations_with_repetition(n, *args)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
