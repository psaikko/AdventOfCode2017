from itertools import takewhile
from sys import stdin

G = dict()

def parseline(l):
	name_str, neighbor_str = l.strip().split("<->")
	name = int(name_str.strip())
	neighbors = list(map(int, (t.strip(",") for t in
		neighbor_str.strip().split(" "))))
	return (name, set(neighbors))

def populate(node, component):
	global G
	component.add(node)
	for neighbor in G[node] - component:
		populate(neighbor, component)

lines = list(takewhile(len, (l.strip() for l in stdin)))
G = { name : neighbors for (name, neighbors) in map(parseline, lines) }

count = 0
while len(G):
	count += 1
	n = list(G.keys())[0]
	component = set()
	populate(n, component)
	print(n, len(component))
	for c in component:
		del G[c]

print(count)