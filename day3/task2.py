import re

text = "the quick brown fox jumps over the lazy dog"
sub = "fox"
match = re.search(sub, text)
start = match.start()
print(f"found at index: {start}")