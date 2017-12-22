from itertools import takewhile
from functools import reduce
from sys import stdin

state = [
list(".#."),
list("..#"),
list("###")]

def parse_rule(line):
	head, target = line.split(" => ")
	head_lines = list(map(list, head.split("/")))
	target_lines = list(map(list, target.split("/")))
	return (head_lines, target_lines)

def flip_x(rule_in):
	rule = [line[:] for line in rule_in]
	W = len(rule[0])
	H = len(rule)
	for x in range(W//2):
		for y in range(H):
			rule[y][x], rule[y][W-1-x] = rule[y][W-1-x], rule[y][x]
	return rule

def flip_y(rule_in):
	rule = [line[:] for line in rule_in]
	W = len(rule[0])
	H = len(rule)
	for x in range(W):
		for y in range(H//2):
			rule[y][x], rule[H-1-y][x] = rule[H-1-y][x], rule[y][x]
	return rule

def rotate_right(rule_in):
	rule = [line[:] for line in rule_in]
	W = len(rule[0])
	H = len(rule)
	for x in range(W):
		for y in range(H):
			rule[x][y] = rule_in[y][W-1-x]
	return rule

def orientations(rule):
	rotations = [rule,
		rotate_right(rule),
		rotate_right(rotate_right(rule)),
		rotate_right(rotate_right(rotate_right(rule)))]
	x_flips = [flip_x(r) for r in rotations]
	y_flips = [flip_y(r) for r in rotations]
	return rotations + x_flips + y_flips

lines = list(takewhile(len, (line.strip() for line in stdin)))
rules = [parse_rule(line) for line in lines]

#for x in orientations(state):
#	print()
#	for line in x:
#		print(''.join(line))

def state_to_string(state):
	return "/".join("".join(l) for l in state)

def substate(state, x, y, w, h):
	return [state[i][x:x+w] for i in range(y,y+h)]
	pass

transformed_rules = { state_to_string(o) : body for (head, body) in rules for o in orientations(head)}

for k in transformed_rules:
	print(k, transformed_rules[k])

def flatten(G):
	m = len(G)
	n = len(G[0][0])
	G = [list(reduce(list.__add__, (G[i][j][k] for j in range(m)))) for i in range(m) for k in range(n)]
	return G

def print_state(state):
	for line in state:
		print(''.join(line))

for i in range(18):
	chunksize = 0
	if len(state) % 2 == 0:
		chunksize = 2
	elif len(state) % 3 == 0:
		chunksize = 3
	else:
		raise state

	if len(state) != len(state[0]):
		raise state

	chunkdim = len(state) // chunksize

	chunks = [[0] * chunkdim for _ in range(chunkdim)]

	for x in range(chunkdim):
		for y in range(chunkdim):
			sub = substate(state, x*chunksize, y*chunksize, chunksize, chunksize)
			chunks[y][x] = transformed_rules[state_to_string(sub)]

	state = flatten(chunks)
	print_state(state)
	print(i)

print(len([c for c in reduce(list.__add__, state) if c == '#']))
