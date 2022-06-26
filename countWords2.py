from collections import Counter

def count_words(filename):
    words_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_words = [
                word for word in line.lower().split() if word.isalpha()
            ]
            print(line_words)
            words_counter.update(Counter(line_words))
    return words_counter


words_counter = count_words("pyzen.txt")
print(words_counter)
for word, count in words_counter.items():
    print(word, "->", count)


print("-----------------")

print(words_counter.most_common(5))

for word, count in words_counter.most_common(5):
    print(word, "->", count)