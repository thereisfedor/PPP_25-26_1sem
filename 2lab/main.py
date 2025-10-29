

if __name__ == "__main__":
    string_1 = input("Первая строка: ").strip()
string_2 = input("Вторая строка: ").strip()

frequency_1 = {}
for char in string_1:
    if char != ' ':
        frequency_1[char] = frequency_1.get(char, 0) + 1

frequency_2 = {}
for char in string_2:
    if char != ' ':
        frequency_2[char] = frequency_2.get(char, 0) + 1

list_1 = sorted(frequency_1.values())
list_2 = sorted(frequency_2.values())

print()
if list_1 != list_2:
    print("Соотношение невозможно: разные частоты символов.")
else:
    pairs_1 = sorted((count, char) for char, count in frequency_1.items())
    pairs_2 = sorted((count, char) for char, count in frequency_2.items())
    print("Соотношение букв:")
    for (count_1, char_1), (count_2, char_2) in zip(pairs_1, pairs_2):
        print(char_1, "=", char_2)
