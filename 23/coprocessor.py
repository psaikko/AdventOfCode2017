from itertools import takewhile
from sys import stdin

registers = { char : 0 for char in (chr(i) for i in range(ord('a'), ord('a')+8)) }
registers['pc'] = 0
registers['a'] = 1

muls = 0

def exec(line, regs):
	global muls
	tokens = line.split(' ')
	cmd = tokens[0]
	reg = tokens[1]

	if cmd == "set":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] = val
	elif cmd == "sub":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] -= val
	elif cmd == "mul":
		muls += 1
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] *= val
	elif cmd == "jnz":
		cnd = registers[reg] if reg in registers else int(reg)
		if cnd != 0:
			val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
			registers["pc"] += val
			return
	else:
		raise cmd

	registers["pc"] += 1

cmds = list(takewhile(len, (line.strip() for line in stdin)))


ct = 0
while True:
	ct += 1
	print(registers)

	i = registers["pc"]
	if i < len(cmds):
		#print(cmds[i])
		exec(cmds[i], registers)
	else:
		break

print(muls)