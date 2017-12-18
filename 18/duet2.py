from itertools import takewhile
from sys import stdin

def make_registers(i):
	registers = { char : 0 for char in (chr(i) for i in range(ord('a'), ord('a')+26)) }
	registers['pc'] = 0
	registers['snd'] = 0
	registers['p'] = i
	return registers

def token_value(token, regs):
	return regs[token] if token in regs else int(token)

def exec(line, regs, snd, rcv):
	tokens = line.split(' ')
	cmd = tokens[0]
	reg = tokens[1]

	if cmd == "snd":
		snd += [token_value(tokens[1], regs)]
	elif cmd == "set":
		regs[reg] = token_value(tokens[2], regs)
	elif cmd == "add":
		regs[reg] += token_value(tokens[2], regs)
	elif cmd == "mul":
		regs[reg] *= token_value(tokens[2], regs)
	elif cmd == "mod":
		regs[reg] %= token_value(tokens[2], regs)
	elif cmd == "rcv":
		if len(rcv):
			regs[reg]= rcv[0]
			rcv[:] = rcv[1:]
		else:
			return False
	elif cmd == "jgz":
		if token_value(tokens[1], regs) > 0:
			regs["pc"] += token_value(tokens[2], regs)
			return True
	else:
		raise cmd

	regs["pc"] += 1
	return True


cmds = list(takewhile(len, (line.strip() for line in stdin)))

reg0 = make_registers(0)
reg1 = make_registers(1)

pipe01 = []
pipe10 = []

ctr = 0

running0 = True
running1 = True

waiting0 = False
waiting1 = False

while True:

	tmp = len(pipe01)

	while running0:
		i = reg0["pc"]
		if i < len(cmds):
			#print(i, cmds[i])
			if not exec(cmds[i], reg0, pipe01, pipe10):
				waiting0 = True
				break
		else:
			running0 = False

	sent0 = (len(pipe01) - tmp)

	if waiting1 and not len(pipe01):
		break

	tmp = len(pipe10)

	while running1:
		i = reg1["pc"]
		if i < len(cmds):
			#print(i, cmds[i])
			if not exec(cmds[i], reg1, pipe10, pipe01):
				waiting1 = True
				break
		else:
			running1 = False

	sent1 = (len(pipe10) - tmp)
	ctr += sent1

	if waiting0 and not len(pipe10):
		break


print(ctr)