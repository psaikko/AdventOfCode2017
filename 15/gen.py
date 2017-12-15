from itertools import islice

def gen(start, mul):
	mask = ((2**16)-1)
	mod = 2147483647
	val = start
	while True:
		val *= mul
		val %= mod
		yield val & mask

gen_a = gen(516, 16807)
gen_b = gen(190, 48271)

match = 0

for i in range(40000000):
	if gen_a.__next__() == gen_b.__next__():
		match += 1

print(match)