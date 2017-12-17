class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def insertAfter(a, b):
	b.next = a.next
	a.next = b

def traverse(start):
	c = start
	while True:
		yield c.value
		c = c.next
		if c == start:
			break

def spin(value):
	# init
	start = Node(0)
	start.next = start

	curr = start

	for i in range(1, 2017+1):
		for j in range(value):
			curr = curr.next
		insertAfter(curr, Node(i))
		curr = curr.next

	return curr.next.value

print(spin(363))