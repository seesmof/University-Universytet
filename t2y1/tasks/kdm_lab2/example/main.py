def placement_without_repetition(n, k, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], n, k)
        print(result)
    else:
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(1, n+1):
                if i not in temp:
                    temp.append(i)
                    helper(result, temp, n, k, True)
                    temp.pop()


def placement_with_repetition(n, k, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], n, k)
        print(result)
    else:
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(1, n+1):
                temp.append(i)
                helper(result, temp, n, k, True)
                temp.pop()


def combination_without_repetition(n, k, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], n, k, 1)
        print(result)
    else:
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(start, n+1):
                temp.append(i)
                helper(result, temp, n, k, i+1, True)
                temp.pop()


def combination_with_repetition(n, k, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], n, k, 1)
        print(result)
    else:
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(start, n+1):
                temp.append(i)
                helper(result, temp, n, k, i, True)
                temp.pop()


def permutations_ordinary(n, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], [False]*n, n)
        print(result)
    else:
        if len(temp) == n:
            result.append(temp.copy())
        else:
            for i in range(1, n+1):
                if not used[i-1]:
                    temp.append(i)
                    used[i-1] = True
                    helper(result, temp, used, n, True)
                    temp.pop()
                    used[i-1] = False


def permutations_with_repetition(n, args, is_helper=False):
    result = []
    if not is_helper:
        helper(result, [], args, [0]*n, n)
        print(result)
    else:
        if len(temp) == n:
            result.append(temp.copy())
        else:
            for i in range(len(args)):
                if count[i] < n:
                    temp.append(args[i])
                    count[i] += 1
                    helper(result, temp, args, count, n, True)
                    temp.pop()
                    count[i] -= 1


def helper(result, temp, *args, is_placement=False, is_combination=False, is_permutation=False):
    if is_placement:
        n, k = args
        start = 1
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(start, n+1):
                if i not in temp:
                    temp.append(i)
                    helper(result, temp, n, k, True, False, False)
                    temp.pop()
    elif is_combination:
        n, k, start = args
        if len(temp) == k:
            result.append(temp.copy())
        else:
            for i in range(start, n+1):
                temp.append(i)
                helper(result, temp, n, k, i+1, False, True, False)
                temp.pop()
    elif is_permutation:
        n, used = args
        if len(temp) == n:
            result.append(temp.copy())
        else:
            for i in range(1, n+1):
                if not used[i-1]:
                    temp.append(i)
                    used[i-1] = True
                    helper(result, temp, used, n, False, False, True)
                    temp.pop()
                    used[i-1] = False


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
