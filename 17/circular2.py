def spin(value):
	# init
	count = 1
	pos   = 0
	after = 0

	for i in range(50000000):
		insert = (pos + value) % count
		if insert == 0:
			after = i + 1
		count += 1
		pos = insert + 1

	return after

print(spin(363))