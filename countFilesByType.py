import pathlib
from collections import Counter


entries = pathlib.Path("/Users/I865343/Pictures/").iterdir()

print(entries)

extensions = [entry.suffix for entry in entries if entry.is_file() and entry.suffix != "" ]

print(extensions)

print(Counter(extensions))

