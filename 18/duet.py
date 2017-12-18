from itertools import takewhile
from sys import stdin

registers = { char : 0 for char in (chr(i) for i in range(ord('a'), ord('a')+26)) }
registers['pc'] = 0
registers['snd'] = 0

def exec(line, regs):
	tokens = line.split(' ')
	cmd = tokens[0]
	reg = tokens[1]

	if cmd == "snd":
		registers["snd"] = registers[reg]
	elif cmd == "set":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] = val
	elif cmd == "add":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] += val
	elif cmd == "mul":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] *= val
	elif cmd == "mod":
		val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
		registers[reg] %= val
	elif cmd == "rcv":
		if registers[reg] > 0:
			print(registers["snd"])
			raise 0
	elif cmd == "jgz":
		if registers[reg] > 0:
			val = registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
			registers["pc"] += val
			return
	else:
		raise cmd

	registers["pc"] += 1


cmds = list(takewhile(len, (line.strip() for line in stdin)))

print(cmds)

while True:
	i = registers["pc"]
	if i < len(cmds):
		print(i, cmds[i])
		exec(cmds[i], registers)
	else:
		break
