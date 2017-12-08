from itertools import takewhile
from sys import stdin

def parseline(l):
	tokens = l.strip().split(" ")
	children = []
	if "->" in tokens:
		children = [t.strip(',') for t in tokens[3:]]
	name = tokens[0]
	weight = int(tokens[1].strip("()"))
	return [name, weight, children]


T = list(map(parseline, takewhile(len, (l.strip() for l in stdin))))

names = set(t[0] for t in T)
children = set(c for t in T for c in t[2])

root = list(names - children)[0]

M = {t[0] : (t[1], t[2]) for t in T}

def weight(n):
	return M[n][0] + sum(map(weight, M[n][1]))

L = {n : M[n][1] for n in names}
W = {n : M[n][0] for n in names}
CW = {n : weight(n) for n in names}

for n in names:
	cws = set(CW[l] for l in L[n])
	if len(cws) > 1:
		print(n, L[n])
		for l in L[n]:
			if len(list(l2 for l2 in L[n] if CW[l] == CW[l2])) == 1:
				other_weight = cws - set([CW[l]])
				diff = CW[l] - list(other_weight)[0]
				print(W[l] - diff)
