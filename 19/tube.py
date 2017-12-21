from itertools import takewhile
from sys import stdin

M = list(takewhile(len, (l.strip('\n') for l in stdin)))

# padding
n = len(M[0])
M = [' '*n] + M + [' '*n]
M = [' '+line+' ' for line in M]

start = M[1].index('|')
start = (1, start)

location = start
direction = (1, 0)

letters = set(chr(i) for i in range(ord('A'), ord('A')+26))

word = ''
steps = 0

for _ in range(1000000):
	(y, x) = location
	(dy, dx) = direction

	if M[y][x] in letters:
		word += M[y][x]

	if M[y][x] == '+':
		#print("turn")
		# turn
		if dx:
			if M[y+dx][x] != ' ':
				(dy, dx) = (dx, dy)
			elif M[y-dx][x] != ' ':
				(dy, dx) = (-dx, dy)
			else:
				raise "turn to y"
		elif dy:
			if M[y][x+dy] != ' ':
				(dy, dx) = (dx, dy)
			elif M[y][x-dy] != ' ':
				(dy, dx) = (dx, -dy)
			else:
				raise "turn to x"
		else:
			raise (dx, dy)

	location = (y+dy, x+dx)
	direction = (dy, dx)

	if y < 0 or y > len(M) or x < 0 or x > len(M[0]) or M[y][x] == ' ':
		print("done")
		break

	steps += 1

	#for (y_, line) in enumerate(M):
	#	if y_ != y:
	#		print(line)
	#	else:
	#		print(''.join((char if x_ != x else "#") for (x_, char) in enumerate(line)))

print(word)
print(steps,"steps")