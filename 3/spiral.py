from itertools import takewhile

n = int(input())

outer_radius = 0
square_radius = 0

for i in range(1,n+n,2):
	if i**2 >= n:
		outer_radius = i
		square_radius = (i-1)//2
		break

inner_radius = outer_radius - 2

inner_square = inner_radius**2
outer_square = outer_radius**2

# distance along s-square
i = n - inner_square
# end of s-square
m = outer_square -inner_square
# distance to middle of edge
edge_distance = abs((i % (m // 4)) - (m // 8))

print(square_radius + edge_distance)