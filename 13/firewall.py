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
scanner_pos = [[i, modwrap(i, size), size] for (i, size) in firewalls]

print(scanner_pos)

print(sum(i*k for (i, j, k) in scanner_pos if j == 0))
