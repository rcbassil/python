from collections import Counter

words = ['hello', 'goodbye', 'howdy', 'hello', 'hello', 'hi', 'bye']

word_counts = Counter(words)

print(word_counts)

print(f'"hello" appears {word_counts["hello"]} time(s)')
print(f'"howdy" appears {word_counts["howdy"]} time(s)')