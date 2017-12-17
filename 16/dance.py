from functools import reduce

def parse_operation(l):
	cmd, args = l[0], l[1:]
	if cmd == 's':
		rot = int(args)
		def rotate(X):
			amt = rot % len(X)
			X = X[-amt:] + X[:-amt]
			return X
		return rotate
	elif cmd == 'x':
		args = [int(t) for t in args.split("/")]
		i, j = args[0], args[1]
		def swap_index(X):
			X[args[0]], X[args[1]] = X[args[1]], X[args[0]]
			return X
		return swap_index
	elif cmd == 'p':
		args = args.split("/")
		def swap_value(X):
			a = X.index(args[0])
			b = X.index(args[1])
			X[a], X[b] = X[b], X[a]
			return X
		return swap_value
	else:
		raise "invalid cmd " + cmd

P = [chr(ord('a')+i) for i in range(16)]

ops = list(map(parse_operation, input().split(',')))
apply = lambda X, f: f(X)
result = reduce(apply, ops, P)

print(''.join(result))

def cycle_length():
	start = [chr(ord('a')+i) for i in range(16)]
	curr = [chr(ord('a')+i) for i in range(16)]
	length = 0
	while True:
		curr = reduce(apply, ops, curr)
		length += 1
		if curr == start:
			return length

length = cycle_length()
print(length)

for i in range((1000000000 - 1) % length):
	result = reduce(apply, ops, result)

print(''.join(result))


#for i in range((1000000000 - 1)):
#	result = apply_permutation(dance, result)

#print(''.join(result))