import random
from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():
    U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    A = {1, 2, 3, 4, 5, 6, 7}
    B = {4, 5, 6, 7, 8, 9, 10}
    C = {1, 3, 5, 7, 9}
    print(A, B, C, U)
    resultA = A - (B - C)
    resultB = (U - C) ^ B
    print(f"\na) A - (B - C) = {sorted(resultA)}")
    print(f"B - C = {B - C}")
    print(f"b) C` ^ B = {sorted(resultB)}")
    print(f"C` = {U - C}")
    print(f"B = {B}")
    print(f"C` ^ B = {(U - C) ^ B}")
    resultC = list(powerset((A & (B | C)) - C))
    print(f"\n(A & (B | C)) - C = {resultC}")
    print(f"Power = {len(resultC)}")
    print(f"B | C = {B | C}")
    print(f"A & (B | C) = {A & (B | C)}")
    print(f"(A & (B | C)) - C = {(A & (B | C)) - C}")


if __name__ == '__main__':
    print("")
    main()
    print("")
