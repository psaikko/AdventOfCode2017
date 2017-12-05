from itertools import takewhile
from sys import stdin
import re

def div(x,y):
	return y % x == 0

def div_some(xs):
	for y in xs[1:]:
		if div(xs[0], y):
			return [y // xs[0]]
	return xs[1:]

def find_div(xs):
	while len(xs) > 1:
		xs = div_some(xs)
	return xs[0]


lines = list(takewhile(len, (l.strip() for l in stdin)))
intlines = [sorted(map(int, re.split('\s', line))) for line in lines]

print(sum(map(find_div, intlines)))