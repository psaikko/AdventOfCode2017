from math import sqrt

n = int(input())
s = int(sqrt(n))
if s % 2 == 0: s += 1
s += 2

A = [[0]*s for i in range(s)]

mid = s // 2
A[mid][mid] = 1

y = mid
x = mid + 1

def adj(x, y):
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			if i or j:
				yield (x+i,y+j)

v = 0
while v < n:

	v = sum(A[yn][xn] for (yn,xn) in adj(y,x))
	A[y][x] = v

	if A[y - 1][x] and not A[y][x+1]: # above
		x += 1
	elif A[y][x - 1] and not A[y-1][x]: # left
		y -= 1
	elif A[y + 1][x] and not A[y][x-1]: # below
		x -= 1
	elif A[y][x + 1] and not A[y+1][x]: # right
		y += 1

print(v)
