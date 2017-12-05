from itertools import takewhile
from sys import stdin

valid = 0
lines = takewhile(len, (l.strip() for l in stdin))
for line in lines:
	words = line.split(" ")
	wordset = set(words)
	if len(words) == len(wordset):
		valid += 1
print(valid)