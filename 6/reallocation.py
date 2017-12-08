import re
banks = list(map(int, re.split('\s', input())))

def tostr(b):
	return '|'.join(map(str, b))

def reallocate(b):
	m = max(b)
	i = b.index(m)
	b[i] = 0;
	while m > 0:
		i += 1
		b[i % len(b)] += 1
		m -= 1
	return b


C = set()
C.add(tostr(banks))
steps = 0

while True:
	steps += 1
	banks = reallocate(banks)
	if tostr(banks) in C:
		break
	C.add(tostr(banks))


print(steps)