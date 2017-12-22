from itertools import takewhile
from sys import stdin

lines = list(takewhile(len, (l.strip() for l in stdin)))

W = len(lines[0])
H = len(lines)

x_mid = W//2
y_mid = H//2

D = [(1,0),(0,-1),(-1,0),(0,1)] # +1 : turn right

M = {}

for y in range(H):
	for x in range(W):
		M[(y,x)] = lines[y][x]

d = 2
p = (y_mid, x_mid)

y_min = 0
y_max = H
x_min = 0
x_max = W

inf = 0

for i in range(10000000):
	if p not in M: M[p] = '.'
	c = M[p]

	if c == '.':
		M[p] = 'W'
		d = (d - 1) % 4
	elif c == '#':
		M[p] = 'F'
		d = (d + 1) % 4
	elif c == 'W':
		inf += 1
		M[p] = '#'
	elif c == 'F':
		M[p] = '.'
		d = (d + 2) % 4


	(dy, dx) = D[d]

	"""
	for y in range(y_min, y_max+1):
		for x in range(x_min, x_max+1):
			if (y,x) == p:
				print('X', end='')
			else:
				c = '.' if (y,x) not in M else M[(y,x)]
				print(c, end='')
		print()
	print()
	"""

	p = (p[0]+dy, p[1]+dx)

	y_min = min(y_min, p[0])
	x_min = min(x_min, p[0])
	y_max = max(y_max, p[1])
	x_max = max(x_max, p[1])

print(inf)