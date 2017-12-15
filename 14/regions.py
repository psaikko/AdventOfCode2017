from functools import reduce

def hash(X):
	num = list(range(256))
	seq = [ord(x) for x in X]
	seq += [17, 31, 73, 47, 23]

	i = 0
	skip = 0
	for r in range(64):
		for x in seq:
			for j in range(x//2):
				a = (i + j) % len(num)
				b = (i + x - 1 - j) % len(num)
				num[a], num[b] = num[b], num[a]
			i = (i + x + skip) % len(num)
			skip += 1

	blocks = [0] * 16

	for i in range(16):
		blocks[i] = reduce(int.__xor__, num[ 16*i : 16*(i+1) ])

	hexes = (s[2:] for s in  map(hex, blocks))

	return ''.join(s.zfill(2) for s in hexes)


k = "hwlqcszp"
used = 0
G = []

for i in range(128):
	h = hash("%s-%d" % (k, i))
	b = bin(int(h, 16))[2:].zfill(128)
	G += [b]

A = dict()

adj = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(128):
	for j in range(128):
		if G[i][j] == '1':
			A[(i,j)] = set()

for i in range(128):
	for j in range(128):
		if (i,j) in A:
			for (k, l) in adj:
				if (i+k, j+l) in A:
					A[(i,j)].add((i+k, j+l))

for k in A:
	print(k, A[k])

components = 0

while len(A):
	components += 1
	node = A.__iter__().__next__()

	stack = [node]
	visited = set()

	while len(stack):
		nxt, stack = stack[0], stack[1:]
		if nxt not in visited:
			visited.add(nxt)
			for adj in A[nxt]:
				stack += [adj]
			del A[nxt]

print(components)