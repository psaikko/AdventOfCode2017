from itertools import takewhile
from sys import stdin

def parse_vec3(s):
	return list(map(int, s.strip("<>").split(",")))

def abs_vec3(v):
	return sum(map(abs, v))

lines = list(takewhile(len, map(str.strip, stdin)))

particle_data = [ [ parse_vec3(v) for (k,v) in (t.split("=") for t in line.split(", ")) ] for line in lines]

for i in range(10000):
	positions = {}
	remove = set()
	# check
	for (j, d) in enumerate(particle_data):
		d2 = ','.join(map(str, d[0]))
		if d2 not in positions:
			positions[d2] = j
		else:
			remove.add(j)
			remove.add(positions[d2])

	remove = reversed(sorted(list(remove)))
	for r in remove:
		del particle_data[r]
		print("collision ", r)

	# update
	for d in particle_data:
		d[1] = [v+a for (v,a) in zip(d[1], d[2])]
		d[0] = [p+v for (p,v) in zip(d[0], d[1])]

print(len(particle_data))

