from collections import Counter

def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            print(line_letters)
            letter_counter.update(Counter(line_letters))
    return letter_counter


letter_counter = count_letters("pyzen.txt")
for letter, count in letter_counter.items():
    print(letter, "->", count)


print("-----------------")

for letter, count in letter_counter.most_common(5):
    print(letter, "->", count)


