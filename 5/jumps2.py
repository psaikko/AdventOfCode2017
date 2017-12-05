from itertools import takewhile
from sys import stdin

T = list(map(int, takewhile(len, (l.strip() for l in stdin))))

i = 0
c = 0

while i < len(T):
	o = T[i]
	if o < 3:
		T[i] += 1
	else:
		T[i] -= 1
	i += o
	c += 1

print(c)
