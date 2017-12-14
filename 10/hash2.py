from functools import reduce

num = list(range(256))
seq = [ord(x) for x in input()]
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

print(''.join( s if len(s) == 2 else '0'+s for s in hexes))
