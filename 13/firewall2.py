from sys import stdin
from itertools import takewhile

def parseline(line):
	return list(map(int, line.split(": ")))

def modwrap(i, n):
	j = i % (2*n - 2)
	if j >= n:
		return n - (j - n + 2)
	else:
		return j

firewalls = list(map(parseline, takewhile(len, (l.strip() for l in stdin))))

for w in range(10000000):
	scanner_pos = [[i+w, modwrap(i+w, size), size] for (i, size) in firewalls]
	s = sum(i*k for (i, j, k) in scanner_pos if j == 0)
	if s == 0:
		print(w)
		break