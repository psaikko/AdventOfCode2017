from itertools import takewhile
from sys import stdin

T = list(map(int, takewhile(len, (l.strip() for l in stdin))))

i = 0
c = 0

while i < len(T):
	T[i] += 1
	i += T[i] - 1
	c += 1

print(c)
