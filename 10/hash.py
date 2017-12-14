num = list(range(256))
seq = (int(x) for x in input().split(','))
i = 0
skip = 0
for x in seq:
	print()
	print(num)
	for j in range(x//2):
		a = (i + j) % len(num)
		b = (i + x - 1 - j) % len(num)
		num[a], num[b] = num[b], num[a]
		print(num)
	i = (i + x + skip) % len(num)
	skip += 1

print(num[0]*num[1])
