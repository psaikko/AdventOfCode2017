from itertools import takewhile
from sys import stdin

regs = dict()

def parse_action(s):
	global regs
	tokens = s.split(" ")
	reg = tokens[0]
	if reg not in regs: regs[reg] = 0
	arg = int(tokens[2])
	op = tokens[1]
	if op == "inc":
		return lambda: regs.__setitem__(reg, regs[reg] + arg)
	elif op == "dec":
		return lambda: regs.__setitem__(reg, regs[reg] - arg)
	else:
		raise "unknown op "+op

def parse_condition(s):
	global regs
	tokens = s.split(" ")
	reg = tokens[0]
	if reg not in regs: regs[reg] = 0
	arg = int(tokens[2])
	cond = tokens[1]
	op = None
	if cond == "<":
		op = int.__lt__
	elif cond == ">":
		op = int.__gt__
	elif cond == ">=":
		op = int.__ge__
	elif cond == "<=":
		op = int.__le__
	elif cond == "!=":
		op = int.__ne__
	elif cond == "==":
		op = int.__eq__
	else:
		raise "unknown cond "+cond
	return lambda: op(regs[reg], arg)

def parse_statement(s):
	action, condition = s.split(" if ")
	return (parse_action(action), parse_condition(condition))

lines = map(parse_statement, takewhile(len, (l.strip() for l in stdin)))

maxval = 0
for line in lines:
	if line[1](): line[0]()
	maxval = max(maxval, max(item[1] for item in regs.items()))

print(regs)
print(max(item[1] for item in regs.items()))
print(maxval)