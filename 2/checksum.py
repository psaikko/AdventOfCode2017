from itertools import takewhile
from sys import stdin

lines = list(takewhile(len, (l.strip() for l in stdin)))
intlines = [list(map(int, line.split('\t'))) for line in lines]

print(sum(max(line) - min(line) for line in intlines))