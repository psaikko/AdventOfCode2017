from math import ceil, sqrt

def prime(x):
	for i in range(2, int(ceil(sqrt(x)))):
		if x % i == 0: return False
	return True

h = 0

for x in range(109900, 126900+1, 17):
	if not prime(x):
		h += 1
	else:
		print(x)

print(h)