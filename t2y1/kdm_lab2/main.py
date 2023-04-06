from itertools import combinations_with_replacement

print("")
n = int(input("Введіть N: "))
k = int(input("Введіть K: "))
print("")

combinations = combinations_with_replacement(range(1, n+1), k)

count = 0
for combination in combinations:
    count += 1
    combination_str = "".join(str(i) for i in combination)
    print(f"{count} - {combination_str}")

print(f"\nЗагальна кількість комбінацій = {count}")
print("")
