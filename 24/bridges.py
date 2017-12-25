from itertools import takewhile
from sys import stdin
from operator import add
from functools import reduce

lines = list(takewhile(len, (line.strip() for line in stdin)))

def parse(line):
	return list(int(t) for t in line.split('/'))

E = list(map(parse, lines))

V = set(reduce(add, E))

print(V, E)

G = { v : set() for v in V }

for (a,b) in E:
	G[a].add(b)
	G[b].add(a)

print(G)

strength = 0
E_seen = set()
best = (0,0)
length = 0

def search(path, node):
	global E_seen
	global strength
	global best
	global length

	if ((length, strength) > best):
		best = (length, strength)
		print(best, path)

	for neighbor in G[node]:
		if (node, neighbor) not in E_seen and (neighbor, node) not in E_seen:
			path += [neighbor]
			strength += (neighbor + node)
			E_seen.add((node, neighbor))
			length += 1

			search(path, neighbor)

			length -= 1
			strength -= (neighbor + node)
			E_seen.remove((node, neighbor))
			path = path[:-1]

search([0], 0)

print(best)